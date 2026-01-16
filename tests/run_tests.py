import os
import subprocess
import glob
import concurrent.futures
import shutil

# Configuration
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
CASES_DIR = os.path.join(TEST_DIR, "cases")
TEMPLATES_DIR = os.path.join(TEST_DIR, "templates")
PROJECT_ROOT = os.path.dirname(TEST_DIR)
OUTPUT_DIR = os.path.join(TEST_DIR, "build")

# Template specific paths (name -> path)
TEMPLATE_PATHS = {
    "ext-ucasthesis": os.path.join(TEMPLATES_DIR, "ucasthesis"),
    "ext-ustcthesis": os.path.join(TEMPLATES_DIR, "ustcthesis"),
    "ext-hithesis": os.path.join(TEMPLATES_DIR, "hithesis"),
    "ext-hithesis-en": os.path.join(TEMPLATES_DIR, "hithesis"),
    "ext-elegantpaper": os.path.join(TEMPLATES_DIR, "elegantpaper"),
    "ext-elegantpaper-en": os.path.join(TEMPLATES_DIR, "elegantpaper"),
    "ext-cjc": os.path.join(TEMPLATES_DIR, "cjc"),
}

def clean_build_dir():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

def run_test_case(case_path, engine):
    case_name = os.path.basename(case_path).replace(".tex", "")
    job_name = f"{case_name}_{engine}"
    output_subdir = os.path.join(OUTPUT_DIR, job_name)
    os.makedirs(output_subdir, exist_ok=True)
    
    # Construct TEXINPUTS
    # 1. Project Root (for otex.sty and otex/ submodules)
    # 2. Template Dir (if applicable)
    # 3. System defaults (empty trailing : inherits system paths)
    texinputs_parts = [PROJECT_ROOT]
    if case_name in TEMPLATE_PATHS:
        texinputs_parts.append(TEMPLATE_PATHS[case_name])
    # Add empty string at end to inherit system defaults
    texinputs = ":".join(texinputs_parts) + ":"

    env = os.environ.copy()
    env["TEXINPUTS"] = texinputs

    cmd = [
        "latexmk",
        f"-{engine}",
        "-shell-escape",
        "-interaction=nonstopmode",
        "-file-line-error",
        f"-outdir={output_subdir}",
        case_path
    ]

    print(f"Running {job_name}...")
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            timeout=180  # 3 minutes timeout per test
        )
        
        # Check for actual output files - latexmk may return non-zero
        # even when output is successfully generated (due to warnings)
        pdf_file = os.path.join(output_subdir, f"{case_name}.pdf")
        xdv_file = os.path.join(output_subdir, f"{case_name}.xdv")
        dvi_file = os.path.join(output_subdir, f"{case_name}.dvi")
        
        has_output = os.path.exists(pdf_file) or os.path.exists(xdv_file) or os.path.exists(dvi_file)
        
        # Analyze log file for errors
        log_file = os.path.join(output_subdir, f"{case_name}.log")
        error_type = None
        error_detail = None
        has_fatal_error = False
        
        if os.path.exists(log_file):
            with open(log_file, 'r', errors='ignore') as f:
                log_content = f.read()
                
                # Check for font-related errors (environment issues)
                font_error_patterns = [
                    "fontspec Error:",
                    "cannot be found",
                    "Font \\",
                    "not loadable",
                    "cannot resolve font",
                    "Could not resolve font",
                ]
                for pattern in font_error_patterns:
                    if pattern.lower() in log_content.lower():
                        error_type = "FONT"
                        # Extract the specific font error
                        for line in log_content.split('\n'):
                            if pattern.lower() in line.lower():
                                error_detail = line.strip()[:80]
                                break
                        break
                
                # Check for missing file errors
                if "File `" in log_content and "' not found" in log_content:
                    error_type = "MISSING_FILE"
                    for line in log_content.split('\n'):
                        if "not found" in line:
                            error_detail = line.strip()[:80]
                            break
                
                # Check for actual fatal errors (not just warnings)
                if "! LaTeX Error:" in log_content:
                    has_fatal_error = True
                    if not error_type:
                        error_type = "LATEX_ERROR"
                        for line in log_content.split('\n'):
                            if "! LaTeX Error:" in line:
                                error_detail = line.strip()[:80]
                                break
                
                if "! Emergency stop." in log_content:
                    has_fatal_error = True
                    if not error_type:
                        error_type = "EMERGENCY_STOP"
                
                # Also check for "No pages of output" which indicates failure
                if "No pages of output." in log_content:
                    has_fatal_error = True
                    if not error_type:
                        error_type = "NO_OUTPUT"
        
        # Success if we have output AND no fatal errors
        success = has_output and not has_fatal_error
        
        # Build error info string
        error_info = ""
        if not success and error_type:
            error_info = f"[{error_type}] {error_detail or ''}"
        
        return job_name, success, result.stdout.decode('utf-8', errors='ignore'), result.stderr.decode('utf-8', errors='ignore'), error_info
    except subprocess.TimeoutExpired:
        return job_name, False, "TIMEOUT", "TIMEOUT", "[TIMEOUT]"
    except Exception as e:
        return job_name, False, str(e), str(e), f"[EXCEPTION] {str(e)}"

def main():
    clean_build_dir()
    test_cases = sorted(glob.glob(os.path.join(CASES_DIR, "*.tex")))
    engines = ["xelatex", "lualatex"]
    
    results = []
    
    
    # Optimize parallelism: Use CPU count (or default to 4 if indeterminate)
    # We use a slight multiplier because some tests might be waiting on I/O, but latex is mostly CPU bound.
    cpu_count = os.cpu_count()
    max_workers = cpu_count if cpu_count else 4
    # Cap at 16 to avoid system overload on very large machines
    max_workers = min(max_workers, 16)
    
    print(f"Running tests with {max_workers} workers...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for case in test_cases:
            for engine in engines:
                futures.append(executor.submit(run_test_case, case, engine))
        
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    # Report
    print("\n" + "="*40)
    print("TEST REPORT")
    print("="*40)
    
    passed = 0
    failed = 0
    env_issues = 0  # Track environment-related failures
    
    results.sort(key=lambda x: x[0])
    
    for job_name, success, stdout, stderr, error_info in results:
        status = "PASS" if success else "FAIL"
        if success:
            passed += 1
            print(f"[{status}] {job_name}")
        else:
            failed += 1
            # Check if it's an environment issue (strictly FONTs as requested)
            is_env_issue = error_info.startswith("[FONT]")
            if is_env_issue:
                env_issues += 1
                
            print(f"[{status}] {job_name}")
            if error_info:
                print(f"    {error_info}")
            else:
                # Fallback to stdout tail if no error info
                print("    Error tail:")
                print("\n".join(stdout.splitlines()[-3:]))

    print("-" * 40)
    print(f"Total: {len(results)}, Passed: {passed}, Failed: {failed}")
    if env_issues > 0:
        print(f"  (including {env_issues} environment issues - missing fonts, etc.)")
    
    # Exit with non-zero only if there are non-environment failures
    code_failures = failed - env_issues
    if code_failures > 0:
        exit(1)
    elif env_issues > 0:
        print("\nNote: All failures are environment-related (missing fonts).")
        print("Install required fonts or skip these tests for your environment.")
        exit(0)

if __name__ == "__main__":
    main()
