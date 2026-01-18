#!/usr/bin/env python3
import sys
import os
import glob
import argparse
from lib.config import TestConfig
from lib.runner import TestRunner
from lib.reporter import RichReporter

def main():
    parser = argparse.ArgumentParser(description="Otex Test Runner")
    parser.add_argument("--filter", "-f", help="Filter test cases by name substring")
    parser.add_argument("--jobs", "-j", type=int, help="Number of parallel jobs")
    parser.add_argument("--engine", "-e", choices=["pdfxe", "pdflua", "all"], default="all", help="Engine to run")
    parser.add_argument("--no-clean", action="store_true", help="Do not clean build directory before running")
    
    args = parser.parse_args()

    # 1. Discovery
    all_cases = sorted(glob.glob(os.path.join(TestConfig.CASES_DIR, "*.tex")))
    
    if args.filter:
        cases = [c for c in all_cases if args.filter in os.path.basename(c)]
    else:
        cases = all_cases

    if not cases:
        print("No test cases found matching criteria.")
        sys.exit(0)

    # 2. Setup
    reporter = RichReporter()
    runner = TestRunner(reporter, jobs=args.jobs)

    if not args.no_clean:
        runner.clean_build()
    
    # 3. Execution
    engines = TestConfig.ENGINES if args.engine == "all" else [args.engine]
    
    # Ensure build dir exists if we didn't clean
    if not os.path.exists(TestConfig.OUTPUT_DIR):
        os.makedirs(TestConfig.OUTPUT_DIR)

    runner.run_suite(cases, engines=engines)

    # 4. Report
    reporter.print_summary()
    
    # Exit code
    failures = [r for r in reporter.results if not r.success and r.error_type != "FONT"]
    if failures:
        sys.exit(1)

if __name__ == "__main__":
    main()
