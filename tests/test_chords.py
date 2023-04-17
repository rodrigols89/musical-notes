from pytest import mark

from musical_notes.chords import chord


@mark.parametrize(
    'chord_notation, expected',
    [
        ('C', ['C', 'E', 'G']),
        ('Cm', ['C', 'D#', 'G']),
        ('C°', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('Cm+', ['C', 'D#', 'G#']),
        ('F#', ['F#', 'A#', 'C#']),
    ],
)  # Arrange
def test_chord_must_return_the_correspondent_notes(chord_notation, expected):
    # Act
    notes, _ = chord(chord_notation).values()

    # Assert
    assert expected == notes


@mark.parametrize(
    'chord_notation, expected',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('C°', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
        ('Cm+', ['I', 'III-', 'V+']),
    ],
)  # Arrange
def test_chord_must_return_the_correspondent_degree(chord_notation, expected):
    # Act
    _, degrees = chord(chord_notation).values()

    # Assert
    assert expected == degrees
