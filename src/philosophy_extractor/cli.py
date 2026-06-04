import typer
from rich import print

app = typer.Typer()


@app.callback()
def main():
    """Philosophy extractor commands."""


@app.command()
def analyze(file: str):
    print(f"[green]Analyzing:[/green] {file}")


if __name__ == "__main__":
    app()

    