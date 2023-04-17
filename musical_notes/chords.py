from musical_notes.half_step import half_step
from musical_notes.minors import _minor
from musical_notes.triad import triad


def chord(chord_notation: str) -> dict[str, list[str]]:
    """
    Generates the chord notes from Chord notation (Chord symbols or Portuguese "Cifra").

    Args:
        chord_notation: A chord in form of Chord notation (Chord symbols or Portuguese "Cifra")

    Returns:
        A dictionary with notes and degrees corresponds to the major scale.

    Examples:
        >>> chord('C')
        {'notes': ['C', 'E', 'G'], 'degrees': ['I', 'III', 'V']}
        >>> chord('Cm')
        {'notes': ['C', 'D#', 'G'], 'degrees': ['I', 'III-', 'V']}
        >>> chord('C°')
        {'notes': ['C', 'D#', 'F#'], 'degrees': ['I', 'III-', 'V-']}
        >>> chord('C+')
        {'notes': ['C', 'E', 'G#'], 'degrees': ['I', 'III', 'V+']}
        >>> chord('Cm+')
        {'notes': ['C', 'D#', 'G#'], 'degrees': ['I', 'III-', 'V+']}
    """
    if 'm' in chord_notation:
        notes, degrees = _minor(chord_notation)
    elif '°' in chord_notation:
        # Split '°' of 'C°', that's, note = C.
        note, _ = chord_notation.split('°')
        tonic, third, fifth = triad(note, 'minor')
        notes = [tonic, third, half_step(fifth, interval=-1)]
        degrees = ['I', 'III-', 'V-']
    elif '+' in chord_notation:
        # Split '+' of 'C+', that's, note = C.
        note, _ = chord_notation.split('+')
        tonic, third, fifth = triad(note, 'major')
        notes = [tonic, third, half_step(fifth, interval=+1)]
        degrees = ['I', 'III', 'V+']
    else:
        notes = triad(chord_notation, 'major')
        degrees = ['I', 'III', 'V']

    return {'notes': notes, 'degrees': degrees}
