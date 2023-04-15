from pytest import mark
from typer.testing import CliRunner

from musical_notes.cli import app

runner = CliRunner()  # Arrange


def test_scale_cli_must_return_zero_stdout():
    result = runner.invoke(app)  # Act

    # Assert
    assert result.exit_code == 0  # exit_code is 0 when not having an error.


@mark.parametrize('note', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])  # Arrange
def test_scale_cli_must_contain_notes_in_the_answer(note):
    result = runner.invoke(app)  # Act

    # Assert
    assert note in result.stdout


@mark.parametrize('note', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])  # Arrange
def test_scale_cli_f_node(note):
    result = runner.invoke(app, ['F'])  # Act

    # Assert
    assert note in result.stdout
