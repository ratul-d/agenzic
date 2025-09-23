import os
import typer
from agenzic.utils.ai_client import ask_ai

def register(app: typer.Typer):
    @app.command()
    def tests(file: str):
        """
        Generate AI-powered unit test suggestions for a Python file.
        """
        if not os.path.exists(file):
            typer.echo(f"File not found: {file}")
            raise typer.Exit(1)

        with open(file, "r", encoding="utf-8") as f:
            code_content = f.read()

        prompt = (
            "You are an expert Python developer and testing engineer.\n"
            "Generate pytest unit tests for the following code.\n"
            "IMPORTANT:\n"
            "- Every single line of the output must be valid Python code.\n"
            "- Any explanations must appear ONLY as Python comments (lines starting with #).\n"
            "- Do NOT include plain English outside comments. End the response with code only, no summary text.\n\n"
            f"{code_content}"
        )

        typer.echo(f"Generating test cases for {file} ...")
        test_output = ask_ai(prompt)

        file_dir = os.path.dirname(file)
        file_base = os.path.basename(file).replace(".py", "")
        out_path = os.path.join(file_dir, f"{file_base}_tests.py")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(test_output)

        typer.echo(f"Test suggestions written to: {out_path}")