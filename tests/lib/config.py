import os

class TestConfig:
    # Directories
    TEST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LIB_DIR = os.path.join(TEST_DIR, "lib")
    CASES_DIR = os.path.join(TEST_DIR, "cases")
    TEMPLATES_DIR = os.path.join(TEST_DIR, "templates")
    PROJECT_ROOT = os.path.dirname(TEST_DIR)
    OUTPUT_DIR = os.path.join(TEST_DIR, "build")

    # Engines
    ENGINES = ["pdfxe", "pdflua"]
    
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

    @staticmethod
    def get_texinputs(case_name):
        """Construct TEXINPUTS environment variable"""
        parts = [TestConfig.PROJECT_ROOT]
        if case_name in TestConfig.TEMPLATE_PATHS:
            parts.append(TestConfig.TEMPLATE_PATHS[case_name])
        # Add empty string at end to inherit system defaults
        return ":".join(parts) + ":"
