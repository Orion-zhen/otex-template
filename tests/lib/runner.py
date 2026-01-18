import os
import subprocess
import time
import shutil
import concurrent.futures
from .config import TestConfig
from .validators import Validator

class TestRunner:
    def __init__(self, reporter, jobs=None):
        self.reporter = reporter
        self.max_workers = jobs or self._get_optimal_workers()

    def _get_optimal_workers(self):
        try:
            cpu = os.cpu_count()
            return min(cpu or 4, 16)
        except:
            return 4

    def clean_build(self):
        if os.path.exists(TestConfig.OUTPUT_DIR):
            shutil.rmtree(TestConfig.OUTPUT_DIR)
        os.makedirs(TestConfig.OUTPUT_DIR)

    def run_suite(self, cases, engines=None):
        if engines is None:
            engines = TestConfig.ENGINES
        
        # Prepare workload
        work_items = []
        for case in cases:
            for engine in engines:
                work_items.append((case, engine))
        
        self.reporter.start_progress(len(work_items))
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._run_single_case, case_path, engine): (case_path, engine)
                for case_path, engine in work_items
            }
            
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                self.reporter.add_result(result)
                self.reporter.update_progress()
        
        self.reporter.stop_progress()

    def _run_single_case(self, case_path, engine):
        start_time = time.time()
        case_name = os.path.basename(case_path).replace(".tex", "")
        
        # Map engine to display name if needed? 
        # Actually standardizing on: pdfxe->xelatex, pdflua->lualatex
        engine_map = {"pdfxe": "xelatex", "pdflua": "lualatex"}
        engine_display = engine_map.get(engine, engine)

        job_name = f"{case_name}@{engine_display}"
        output_subdir = os.path.join(TestConfig.OUTPUT_DIR, job_name)
        
        if not os.path.exists(output_subdir):
             os.makedirs(output_subdir)

        # Environment
        env = os.environ.copy()
        env["TEXINPUTS"] = TestConfig.get_texinputs(case_name)

        cmd = [
            "latexmk",
            f"-{engine}",
            "-shell-escape",
            "-interaction=nonstopmode",
            "-file-line-error",
            f"-outdir={output_subdir}",
            case_path
        ]

        try:
            # Update progress bar description with current job
            self.reporter.update_status(job_name)
            
            # We don't really care about stdout/stderr unless it crashes hard,
            # because we rely on the log file.
            subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env,
                timeout=240 # 4 minutes
            )
        except subprocess.TimeoutExpired:
             return Validator.validate(case_name, engine_display, output_subdir, 240.0) # Will fail on log check likely

        duration = time.time() - start_time
        
        # Validate
        return Validator.validate(case_name, engine_display, output_subdir, duration)
