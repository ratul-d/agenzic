import os
import typer
import ast
from radon.complexity import cc_visit
from radon.metrics import h_visit,mi_visit

# -------------------------------------------------------------------------
# EXPERIMENTAL COMMAND: Python Function Extractor & Code Metrics
# Purpose: Extract all functions from a Python file and optionally analyze them
#          for metrics, readability, and maintainability.
# Status: Hidden / Experimental
# Notes:
#   - Reads a Python (.py) file.
#   - Splits the file into individual functions.
#   - Computes metrics like LOC, cyclomatic complexity, and maintainability index.
#   - Outputs metrics per function or for the whole file.
# -------------------------------------------------------------------------

# This command is intentionally left here for experimentation with external APIs.
# It is NOT part of the official Agenzic feature set.


def register(app: typer.Typer):
    @app.command(hidden=True)
    def codemetrics(file: str = typer.Option(..., "--file", help="Output file path")):
        """
        Generate code metrics for a Python file.
        Example:
            codemetrics --file abc.py
        """

        if not os.path.exists(file):
            typer.echo(f"File not found: {file}")
            raise typer.Exit()
        with open(file, "r", encoding="utf-8") as f:
            code = f.read()

        tree = ast.parse(code)
        num_functions = sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))
        num_classes = sum(isinstance(node, ast.ClassDef) for node in ast.walk(tree))
        loc = len(code.splitlines())

        # --- Cyclomatic complexity ---
        cc_scores = [block.complexity for block in cc_visit(code)]
        avg_cc = sum(cc_scores) / len(cc_scores) if cc_scores else 0

        # --- Maintainability index ---
        try:
            mi = mi_visit(code, False)
        except Exception:
            mi = None

        metrics = {
            "loc": loc,
            "functions": num_functions,
            "classes": num_classes,
            "cyclomatic_complexity": {
                "average": avg_cc,
                "all": cc_scores
            },
            "maintainability_index": mi
        }
        typer.echo(f"Lines of Code: {metrics['loc']}")
        typer.echo(f"Number of Functions: {metrics['functions']}")
        typer.echo(f"Number of Classes: {metrics['classes']}")
        typer.echo(f"Cyclomatic Complexity (average): {metrics['cyclomatic_complexity']['average']}")
        typer.echo(f"Cyclomatic Complexity (all): {metrics['cyclomatic_complexity']['all']}")
        typer.echo(f"Maintainability Index: {metrics['maintainability_index']}")