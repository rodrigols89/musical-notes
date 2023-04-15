from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from musical_notes.scales import scale

console = Console()
app = Typer()


@app.command()
def scales(note=Argument('c'), key=Argument('major')):
    table = Table()

    notes, grades = scale(note, key).values()

    for grade in grades:
        table.add_column(grade)
    table.add_row(*notes)  # Add row/+Unpacking approach (*)
    console.print(table)  # print table.
