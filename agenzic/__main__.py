import typer
from .commands import commit, summarize, review, version

app = typer.Typer(help="Agenzic CLI - AI assistant for developers")

commit.register(app)
summarize.register(app)
review.register(app)
version.register(app)

def main():
    """Entry point for console_scripts"""
    app()

if __name__ == "__main__":
    main()