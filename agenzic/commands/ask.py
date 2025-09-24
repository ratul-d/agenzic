import os
import typer
from agenzic.utils.ai_client import ask_ai

def register(app: typer.Typer):
    @app.command()
    def ask(question: str,
            file: str = typer.Option(None,help="Path to specific file to search"),
            dir: str = typer.Option(".",help="Path folder to search if no file specified")
    ):
        """
        Ask AI a question about your project or a specific file. |
        Defaults to current directory. Use --file or --dir to override.
        """
        if file:
            if not os.path.exists(file):
                typer.echo(f"File not found: {file}")
                raise typer.Exit(1)
            with open(file, "r", encoding="utf-8") as f:
                code_content = f.read()
        else:
            code_content=""
            for root, _, files in os.walk(dir):
                for f in files:
                    if f.endswith((".py", ".txt", ".md")):
                        path = os.path.join(root, f)
                        with open(path, "r", encoding="utf-8") as file_f:
                            code_content += f"\n\n# File: {path}\n"
                            code_content += file_f.read()

        if not code_content.strip():
            typer.echo("No code content found to analyze.")
            raise typer.Exit(1)

        prompt = f"""
            You are an expert Python developer. Answer the question based only on the code below.
            Do not make assumptions beyond the provided code.

            Code:
            {code_content}

            Question:
            {question}
            """

        typer.echo("Thinking...")
        answer=ask_ai(prompt)
        typer.echo("\nAI Answer:\n")
        typer.echo(answer)