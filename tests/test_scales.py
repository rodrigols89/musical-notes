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
    'tonic, key, expected',
    [
        ('C', 'major', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'major', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'major', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'minor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'minor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'minor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)  # Arrange
def test_scale_must_return_correct_note(tonic, key, expected):
    # Act
    result = scale(tonic, key)

    # Assert
    assert result['notes'] == expected


@mark.parametrize(
    'tonic, key, expected',
    [
        ('c', 'major', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']),
    ],
)  # Arrange
def test_scale_must_return_seven_degrees(tonic, key, expected):
    resultado = scale(tonic, key)  # Act
    assert resultado['degrees'] == expected  # Assert
