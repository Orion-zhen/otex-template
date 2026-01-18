import os
from .parser import LogParser

class TestResult:
    def __init__(self, case_name, engine, success, duration, error_type=None, error_detail=None, log_tail=None, log_file=None):
        self.case_name = case_name
        self.engine = engine
        self.success = success
        self.duration = duration
        self.error_type = error_type
        self.error_detail = error_detail
        self.log_tail = log_tail
        self.log_file = log_file

class Validator:
    @staticmethod
    def validate(case_name, engine, output_dir, duration, strict=False):
        pdf_file = os.path.join(output_dir, f"{case_name}.pdf")
        log_file = os.path.join(output_dir, f"{case_name}.log")
        
        # 1. Check strict PDF existence
        has_pdf = os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 0
        
        # 2. Parse Log for Errors
        error_type, error_detail, is_fatal_log = LogParser.parse_log(log_file)
        
        # Get log tail for reporting
        log_tail = ""
        if os.path.exists(log_file):
            with open(log_file, 'r', errors='ignore') as f:
                lines = f.readlines()
                log_tail = "".join(lines[-20:]) # Last 20 lines

        # 3. Specific Checks
        # Glossary Check
        if "glossary" in case_name:
             gls_file = os.path.join(output_dir, f"{case_name}.gls")
             if not (os.path.exists(gls_file) and os.path.getsize(gls_file) > 0):
                 if not (error_type and is_fatal_log): # Don't override existing fatal error
                     return TestResult(case_name, engine, False, duration, 
                                     "MISSING_GLOSSARY", "Glossary index (.gls) file missing or empty", log_tail, log_file)

        # 4. Final Verification
        if has_pdf and not is_fatal_log:
            return TestResult(case_name, engine, True, duration, log_file=log_file)
        
        # Fallback for failure
        if not error_type:
            if not has_pdf:
                error_type = "NO_PDF"
                error_detail = "PDF file was not generated"
            else:
                # PDF exists but maybe something subtle? 
                # Actually if has_pdf and not is_fatal_log, we passed above.
                pass
        
        return TestResult(case_name, engine, False, duration, error_type, error_detail, log_tail, log_file)
