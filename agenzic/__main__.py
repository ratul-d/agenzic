import subprocess
import typer
from .ai_client import ask_ai
import os
import agenzic

app = typer.Typer(help="Agenzic CLI - AI assistant for developers")

@app.command()
def hello():
    """TEST Hello Command"""
    typer.echo("Hello from Agenzic CLI!")

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
        commit_msg = result.split("\n")[0].strip()
        subprocess.run(["git","commit","-m",commit_msg])
        typer.echo(f"Commited with {commit_msg}")

    elif choice.lower().startswith("e"):
        commit_msg = result.split("\n")[0].strip()
        commit_msg = typer.prompt("Edit your commit message",default=result.split("\n")[0].strip())
        subprocess.run(["git", "commit", "-m", commit_msg])
        typer.echo(f"Commited with {commit_msg}")

    else:
        typer.echo("Commit cancelled")

@app.command()
def summarize(file: str):
    """Summarize a file with AI"""
    if not os.path.exists(file):
        typer.echo(f"File not found: {file}")
        raise typer.Exit(1)
    with open(file,"r",encoding="utf-8") as f:
        content = f.read()

    prompt = f"Summarize the following code/file in a concise, human readable way:\n{content}"
    typer.echo("Summarizing...")
    summary=ask_ai(prompt)
    typer.echo("\n Summary:")
    typer.echo(summary)

@app.command()
def version():
    """Show Agenzic version"""
    typer.echo(f"Agenzic v{agenzic.__version__}")

def main():
    """Entry point for console_scripts"""
    app()

if __name__ == "__main__":
    main()