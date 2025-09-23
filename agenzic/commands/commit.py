import subprocess
import typer
from agenzic.utils.ai_client import ask_ai

def register(app: typer.Typer):
    @app.command()
    def commit(alt: int = 1):
        """Generate AI commit message"""
        diff = subprocess.getoutput("git diff --staged")

        if not diff:
            typer.echo("No staged changes found. Stage your changes with `git add`.")
            raise typer.Exit(1)

        prompt = f"Generate{alt} conventional/professional commit message(s) for this git diff:\n{diff}"

        typer.echo("Thinking ...")
        result = ask_ai(prompt)

        typer.echo("\nAI Suggestion(s):")
        typer.echo(result)

        choice = typer.prompt("\nDo you want to (c)ommit, (e)dit, or (q)uit?", default="c")

        if choice.lower().startswith("c"):
            commit_lines = result.split("\n")
            subprocess.run(["git", "commit", "-m", commit_lines[0], "-m", "\n".join(commit_lines[1:])])
            typer.echo(f"Commited with {commit_lines}")

        elif choice.lower().startswith("e"):
            commit_msg = typer.prompt("Edit your commit message",default=result.split("\n")[0].strip())
            subprocess.run(["git", "commit", "-m", commit_msg])
            typer.echo(f"Commited with {commit_msg}")

        else:
            typer.echo("Commit cancelled")