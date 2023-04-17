from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from musical_notes.chords import chord as _chord
from musical_notes.harmonic_field import harmonic_field as _harmonic_field
from musical_notes.scales import scale as _scale

console = Console()
app = Typer()


@app.command()
def scale(
    tonic=Argument('c', help='Tonic of scale'),
    key=Argument('major', help='Key (PT-BR=tonalidade) of scale'),
):
    table = Table()

    notes, degrees = _scale(tonic, key).values()

    for degree in degrees:
        table.add_column(degree)  # Add header (degrees)
    table.add_row(*notes)  # Add row/+Unpacking approach (*)
    console.print(table)  # print table.


@app.command()
def chord(
    chord_notation=Argument('c', help='Chord notation of a chord'),
):
    table = Table()

    notes, degrees = _chord(chord_notation).values()

    for degree in degrees:
        table.add_column(degree)  # Add header (degrees)
    table.add_row(*notes)  # Add row/+Unpacking approach (*)
    console.print(table)  # print table.


@app.command()
def harmonic_field(
    tonic: str = Argument('c', help='Harmonic field tonic note'),
    key: str = Argument('major', help='Harmonic field key (PT-BR=tonalidade)'),
):
    table = Table()

    chords, degrees = _harmonic_field(tonic, key).values()

    for degree in degrees:
        table.add_column(degree)

    table.add_row(*chords)

    console.print(table)
