import typer
from agenzic.commands import commit, summarize, review, docgen, tests
import agenzic
import platform

app = typer.Typer(help="Agenzic CLI - AI assistant for developers")

@app.command()
def version():
    """Show Agenzic version and environment info"""
    try:
        import typer as typer_lib
        typer.echo(f"Agenzic v{agenzic.__version__}")
        typer.echo(f"Python: {platform.python_version()}")
        typer.echo(f"Typer: {typer_lib.__version__}")
    except Exception:
        typer.echo(f"Agenzic v{agenzic.__version__} (environment details unavailable)")

@app.command()
def about():
    """Show information about Agenzic CLI"""
    typer.echo(
        f"""
    Agenzic CLI v{agenzic.__version__}
    AI-powered assistant for developers.

    Features:
      - AI commit message generator
      - AI code summarizer
      - AI-powered code review
      - Documentation generator
      - Test case generator

    Repository: https://github.com/ratul-d/agenzic
    """
    )

@app.command()
def help():
    """Show available commands and usage examples"""
    typer.echo(typer.style("\nAgenzic CLI - Help", fg=typer.colors.BRIGHT_CYAN, bold=True))
    typer.echo("=" * 18)

    typer.echo(typer.style("\nAvailable Commands:", fg=typer.colors.BRIGHT_RED, bold=True))
    commands = {
        "commit": "Generate AI commit message(s) for staged changes",
        "summarize": "Summarize a code file with AI",
        "review": "Review code (staged diff or specific file)",
        "docgen": "Generate project or file documentation",
        "tests": "Generate unit tests for your code",
        "version": "Show Agenzic version and environment info",
        "about": "Show project information",
        "help": "Show this help message",
    }
    for cmd, desc in commands.items():
        typer.echo(f"  {typer.style(cmd, fg=typer.colors.BRIGHT_RED, bold=True)}  {desc}")

    typer.echo(typer.style("\nUsage Examples:", fg=typer.colors.BRIGHT_BLUE, bold=True))
    usage_examples = [
        ("Commit", "agenzic commit"),
        ("Summarize", "agenzic summarize myscript.py"),
        ("Review", "agenzic review\n  agenzic review --file utils/helpers.py"),
        ("Docgen", "agenzic docgen --file myscript.py\n  agenzic docgen --dir <folder>"),
        ("Tests", "agenzic tests myscript.py"),
        ("Version", "agenzic version"),
        ("About", "agenzic about"),
        ("Help", "agenzic help"),
    ]
    for title, example in usage_examples:
        typer.echo(
            f"{typer.style(title + ':', fg=typer.colors.BRIGHT_BLUE, bold=True)}\n  {example}"
        )


commit.register(app)
summarize.register(app)
review.register(app)
docgen.register(app)
tests.register(app)

def main():
    """Entry point for console_scripts"""
    app()

if __name__ == "__main__":
    main()