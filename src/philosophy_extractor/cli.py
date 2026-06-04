from pathlib import Path

import typer
from rich import print

from philosophy_extractor.people import extract_people

app = typer.Typer()

@app.callback()
def main():
    """Philosophy extractor commands."""

@app.command()
def analyze(file: str):
    """
    Analyze a journal text file.
    """

    path = Path(file)

    if not path.exists():
        print(f"[red]File not found:[/red] {file}")
        raise typer.Exit()

    text = path.read_text()

    people = extract_people(text)

    print("\n[bold cyan]People Mentioned[/bold cyan]")

    if not people:
        print("No people found.")
    else:
        for name, count in sorted(
            people.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            print(f"- {name}: {count}")


if __name__ == "__main__":
    app()

    