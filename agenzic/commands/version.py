import typer
import agenzic

def register(app: typer.Typer):
    @app.command()
    def version():
        """Show Agenzic version"""
        typer.echo(f"Agenzic v{agenzic.__version__}")