from pytest import mark
from typer.testing import CliRunner

from musical_notes.cli import app

runner = CliRunner()  # Arrange


def test_scale_cli_must_return_zero_stdout():
    result = runner.invoke(app)  # Act

    # Assert
    assert result.exit_code == 0  # exit_code is 0 when not having an error.


@mark.parametrize('tonic', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])  # Arrange
def test_scale_cli_must_contain_tonics_in_the_answer(tonic):
    result = runner.invoke(app)  # Act

    # Assert
    assert tonic in result.stdout


@mark.parametrize('f_note', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])  # Arrange
def test_scale_cli_f_note(f_note):
    result = runner.invoke(app, ['F'])  # Act

    # Assert
    assert f_note in result.stdout


@mark.parametrize(
    'degrees',
    ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
)  # Arrange
def test_scale_cli_must_contain_all_degrees_in_the_cli_return(degrees):
    result = runner.invoke(app, ['F'])  # Act

    # Assert
    assert degrees in result.stdout
