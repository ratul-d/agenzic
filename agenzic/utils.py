import os
import typer
from dotenv import load_dotenv

load_dotenv()

def get_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        typer.echo("Please set OPENAI_API_KEY environment variable")
        raise typer.Exit()
    return key