import re

class LogParser:
    @staticmethod
    def parse_log(log_path):
        """
        Parses the LaTeX log file to identify errors.
        Returns: (error_type, error_detail, is_fatal)
        """
        if not os_path_exists(log_path):
            return "MISSING_LOG", "Log file not found", True

        try:
            with open(log_path, 'r', errors='ignore') as f:
                content = f.read()
        except:
             return "READ_ERROR", "Could not read log file", True

        is_fatal = False
        
        # Check Fatal Symptoms first to establish if the test FAILED
        if "! LaTeX Error:" in content or "! Emergency stop." in content or "No pages of output." in content:
            is_fatal = True

        # Now identify the *cause* (prioritize specific issues over generic symptoms)

        # 1. Font Errors
        font_patterns = [
            "fontspec Error:", "cannot be found", "Font \\", "not loadable", 
            "cannot resolve font", "Could not resolve font"
        ]
        for pattern in font_patterns:
            if pattern.casefold() in content.casefold():
                detail = LogParser._extract_line(content, pattern)
                # If it was fatal (no output), we return True. If it wasn't (PDF generated), we return False.
                return "FONT", detail, is_fatal 

        # 2. Missing Files
        if "File `" in content and "' not found" in content:
             detail = LogParser._extract_line(content, "' not found")
             return "MISSING_FILE", detail, is_fatal
        
        # 3. Fatal LaTeX Errors (Generic)
        if "! LaTeX Error:" in content:
            detail = LogParser._extract_line(content, "! LaTeX Error:")
            return "LATEX_ERROR", detail, True # Always fatal if we found this tag
        
        # 4. Emergency Stop (Generic)
        if "! Emergency stop." in content:
            return "EMERGENCY_STOP", "Process aborted abruptly", True
            
        # 5. No Output (Fallback symptom if no specific cause found)
        if "No pages of output." in content:
            return "NO_OUTPUT", "No PDF pages generated", True

        return None, None, False

    @staticmethod
    def _extract_line(content, pattern):
        for line in content.split('\n'):
            if pattern.casefold() in line.casefold():
                 return line.strip()[:100] # Cap length
        return pattern

def os_path_exists(path):
    # Helper to avoid importing os at top level if we want this pure logic, 
    # but actually we can just import os.
    import os
    return os.path.exists(path)
