from pytest import mark
from typer.testing import CliRunner

from musical_notes.cli import app

runner = CliRunner()  # Arrange


def test_scale_cli_must_return_zero_stdout():
    result = runner.invoke(app, ['scale'])  # Act

    # Assert
    assert result.exit_code == 0  # exit_code is 0 when not having an error.


@mark.parametrize('tonic', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])  # Arrange
def test_scale_cli_must_contain_tonics_in_the_answer(tonic):
    result = runner.invoke(app, ['scale'])  # Act

    # Assert
    assert tonic in result.stdout


@mark.parametrize('f_note', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])  # Arrange
def test_scale_cli_f_note(f_note):
    result = runner.invoke(app, ['scale', 'F'])  # Act

    # Assert
    assert f_note in result.stdout


@mark.parametrize(
    'degrees',
    ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
)  # Arrange
def test_scale_cli_must_contain_all_degrees_in_the_cli_return(degrees):
    result = runner.invoke(app, ['scale', 'F'])  # Act

    # Assert
    assert degrees in result.stdout


@mark.parametrize('note', ['C', 'E', 'G'])  # Arrange
def test_chord_cli_must_contain_notes_in_the_answer(note):
    result = runner.invoke(app, ['chord'])  # Act

    # Assert
    assert note in result.stdout


@mark.parametrize(
    'degrees',
    ['I', 'III', 'V'],
)  # Arrange
def test_chord_cli_must_contain_all_degrees_in_the_cli_return(degrees):
    result = runner.invoke(app, ['chord', 'F'])  # Act

    # Assert
    assert degrees in result.stdout


@mark.parametrize(
    'degree', ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']
)  # Arrange
def test_harmonic_field_cli_must_contain_all_degrees_in_the_cli_return(
    degree,
):
    result = runner.invoke(app, ['harmonic-field', 'C'])  # Act
    assert degree in result.stdout  # Assert


@mark.parametrize(
    'chord_notation', ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°']
)  # Arrange
def test_harmonic_field_cli_must_contain_all_chord_notation(chord_notation):
    result = runner.invoke(app, ['harmonic-field', 'C'])  # Act
    assert chord_notation in result.stdout  # Assert
