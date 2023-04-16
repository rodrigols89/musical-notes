from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from musical_notes.scales import scale

console = Console()
app = Typer()


@app.command()
def scales(tonic=Argument('c'), key=Argument('major')):
    table = Table()

    notes, degrees = scale(tonic, key).values()

    for degree in degrees:
        table.add_column(degree)  # Add header (degrees)
    table.add_row(*notes)  # Add row/+Unpacking approach (*)
    console.print(table)  # print table.
