from pytest import raises

from musical_notes.scales import NOTES, scale


def test_scale_must_work_with_lowercase_notes():
    # Arrange
    note = 'c'
    key = 'major'

    # Act
    result = scale(note, key)

    # Assert
    assert result


def test_scale_must_return_an_error_saying_that_the_note_not_exists():
    # Arrange
    note = 'X'
    key = 'major'
    error_message = f'That note does not exist, try {NOTES}'

    # Act
    with raises(ValueError) as error:
        scale(note, key)

    # Assert
    assert error_message == error.value.args[0]
