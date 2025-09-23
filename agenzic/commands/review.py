import subprocess
import typer
from agenzic.utils.ai_client import ask_ai
import os

def register(app: typer.Typer):
    @app.command()
    def review(file: str = typer.Option(None, help="Path to a specific code file to review")):
        """
        Generate AI-powered code review |
        By default, reviews staged git change.
        Optionally, review a specific file using --file.
        """
        if file:
            if not os.path.exists(file):
                typer.echo(f"File not found: {file}")
                raise typer.Exit(1)
            with open(file, "r", encoding="utf-8") as f:
                code_content = f.read()
            prompt = (
                "You are an expert Python code reviewer.\n"
                "Review the following code and provide a structured review:\n"
                "- Security issues\n"
                "- Style suggestions\n"
                "- Possible bugs\n\n"
                f"{code_content}"
            )
            typer.echo(f"Reviewing File: {file}...")
        else:
            diff = subprocess.getoutput("git diff --staged")
            if not diff:
                typer.echo("No staged changes found. Stage your changes with `git add` or specify a file.")
                raise typer.Exit(1)
            prompt = (
                "You are an expert code reviewer.\n"
                "Analyze the following git diff and provide a structured review:\n"
                "- Security issues\n"
                "- Style suggestions\n"
                "- Possible bugs\n\n"
                f"{diff}"
            )
            typer.echo("Reviewing staged git changes...")

        review_output = ask_ai(prompt)
        typer.echo("\nAI Review:")
        typer.echo(review_output)