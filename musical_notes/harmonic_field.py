from musical_notes.convert_degrees import convert_degrees
from musical_notes.scales import scale
from musical_notes.triads import triad_in_the_scale


def harmonic_field(tonic: str, key: str) -> dict[str, list[str]]:
    """
    Generate a Harmonic Field based on the tonic note and key.

    args:
        tonic: First degree of the Harmonic Field.
        key: Key to the field. E.g major, minor, etc...

    Returns:
        A Harmonic Field.

    Examples:
        >>> harmonic_field('c', 'major')
        {'chords': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'], 'degrees': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']}

        >>> harmonic_field('c', 'minor')
        {'chords': ['Cm', 'D°', 'D#', 'Fm', 'Gm', 'G#', 'A#'], 'degrees': ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']}
    """
    notes, _degrees = scale(tonic, key).values()
    chords = [triad_in_the_scale(note, notes) for note in notes]
    degrees = [
        convert_degrees(chord, degree)
        for chord, degree in zip(chords, _degrees)
    ]

    return {'chords': chords, 'degrees': degrees}
