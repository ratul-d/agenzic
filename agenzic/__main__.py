import typer
from agenzic.commands import commit, summarize, review, version, docgen, tests

app = typer.Typer(help="Agenzic CLI - AI assistant for developers")

version.register(app)
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