from pytest import mark, raises

from musical_notes.scales import NOTES, SCALES, scale


def test_scale_must_work_with_lowercase_tonic():
    # Arrange
    tonic = 'c'
    key = 'major'

    # Act
    result = scale(tonic, key)

    # Assert
    assert result


def test_scale_must_return_an_error_saying_that_the_tonic_not_exists():
    # Arrange
    tonic = 'X'
    key = 'major'
    error_message = f'That tonic does not exist, try {NOTES}'

    # Act
    with raises(ValueError) as error:
        scale(tonic, key)

    # Assert
    assert error_message == error.value.args[0]


def test_scale_key_not_exists():
    # Arrange
    tonic = 'X'
    key = 'banana'
    error_message = f'That key (PT-BR=tonalidade) does not exist or not does implemented, try {list(SCALES.keys())}'

    # Act
    with raises(KeyError) as error:
        scale(tonic, key)

    # Assert
    assert error_message == error.value.args[0]


@mark.parametrize(
    # Arrange
    'tonic, expected',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_scale_must_return_correct_note(tonic, expected):
    # Act
    result = scale(tonic, 'major')

    # Assert
    assert result['notes'] == expected
