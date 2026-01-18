import sys
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text

class RichReporter:
    def __init__(self):
        self.console = Console()
        self.results = []
        self._progress = None
        self._task_id = None

    def start_progress(self, total):
        self._progress = Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=self.console
        )
        self._progress.start()
        self._task_id = self._progress.add_task("Running Tests...", total=total)

    def update_progress(self, advance=1):
        if self._progress:
            self._progress.advance(self._task_id, advance)

    def stop_progress(self):
        if self._progress:
            self._progress.stop()

    def update_status(self, status_text):
        if self._progress and self._task_id is not None:
             self._progress.update(self._task_id, description=f"Running Tests... [dim]({status_text})[/dim]")

    def add_result(self, result):
        self.results.append(result)
        # Optional: Print immediate failure info? No, keep it clean until end.
    
    def print_summary(self):
        self.console.print("\n")
        
        # 1. Summary Table
        table = Table(title="Test Results", expand=True)
        table.add_column("Case", style="cyan", no_wrap=True)
        table.add_column("Engine", style="magenta")
        table.add_column("Status", justify="center")
        table.add_column("Time", justify="right")
        table.add_column("Info")

        passed = 0
        failed = 0
        env_issues = 0

        for res in sorted(self.results, key=lambda x: x.case_name):
            status_style = "green" if res.success else "red"
            status_text = "PASS" if res.success else "FAIL"
            
            info = ""
            if not res.success:
                failed += 1
                info = f"[{res.error_type}] {res.error_detail or ''}"
                if res.error_type == "FONT":
                    env_issues += 1
                    status_style = "yellow" # Warn for env issues
            else:
                passed += 1

            table.add_row(
                res.case_name, 
                res.engine, 
                Text(status_text, style=status_style), 
                f"{res.duration:.2f}s", 
                info
            )

        self.console.print(table)
        
        # 2. Detailed Failures
        if failed > 0:
            self.console.print("\n[bold red]Failure Details:[/bold red]")
            for res in self.results:
                if not res.success:
                    self._print_failure_detail(res)

        # 3. Final Stats
        self.console.print("\n[bold]Summary:[/bold]")
        self.console.print(f"Total: {len(self.results)}")
        self.console.print(f"Passed: [green]{passed}[/green]")
        self.console.print(f"Failed: [red]{failed}[/red]")
        if env_issues > 0:
             self.console.print(f"  (Includes {env_issues} Environment/Font issues)")

        if failed == 0:
            self.console.print("\n[bold green]:sparkles: All tests passed! :sparkles:[/bold green]")
        elif failed == env_issues:
             self.console.print("\n[bold yellow]Only environment issues detected.[/bold yellow]")

    def _print_failure_detail(self, res):
        title = f"{res.case_name} @ {res.engine}"
        subtitle = f"[{res.error_type}] {res.error_detail}"
        
        log_content = res.log_tail or "(No log content)"
        # clean up null bytes if any
        log_content = log_content.replace('\0', '')
        
        syntax = Syntax(log_content, "tex", theme="ansi_dark", line_numbers=False)
        
        # Prepare footer text for log file location
        footer = Text("Log: ", style="dim")
        if res.log_file:
             footer.append(res.log_file, style="blue underline")
        
        panel = Panel(
            syntax,
            title=f"[bold red]{title}[/bold red]",
            subtitle=subtitle,
            border_style="red",
            expand=False,
            subtitle_align="left",
            title_align="left"
        )
        self.console.print(panel)
        if res.log_file:
            self.console.print(f"    [dim]See full log at: [blue]{res.log_file}[/blue][/dim]\n")

class PlainReporter:
    """Fallback if rich is not available"""
    def __init__(self):
        self.results = []
    
    def start_progress(self, total):
        print(f"Running {total} tests...")

    def update_progress(self, advance=1):
        sys.stdout.write(".")
        sys.stdout.flush()

    def stop_progress(self):
        print()

    def update_status(self, status_text):
        pass

    def add_result(self, result):
        self.results.append(result)

    def print_summary(self):
        # ... (Simple print logic similar to original)
        pass # Not implemented fully as user asked for Rich
