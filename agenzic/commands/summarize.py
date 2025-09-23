import typer
from agenzic.utils.ai_client import ask_ai
import os

def register(app: typer.Typer):
    @app.command()
    def summarize(file: str):
        """Summarize a file with AI"""
        if not os.path.exists(file):
            typer.echo(f"File not found: {file}")
            raise typer.Exit(1)
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()

        prompt = f"Summarize the following code/file in a concise, human readable way:\n{content}"
        typer.echo("Summarizing...")
        summary = ask_ai(prompt)
        typer.echo("\n Summary:")
        typer.echo(summary)