from musical_notes.scales import scale


def triad(note: str, key: str) -> list[str]:
    """
    Generate a triad from a tonic note and key.

    Args:
        note: A note that wishes to get the chord.
        key: Key (PT-BR=tonalidade) that the chord will be formed.

    Returns:
        The triad of the chord referent to the note and key (PT-BR=tonalidade).

    Examples:
        >>> triad('C', 'major')
        ['C', 'E', 'G']
        >>> triad('C', 'minor')
        ['C', 'D#', 'G']
    """
    degrees = (0, 2, 4)
    scale_notes, _ = scale(note, key).values()

    return [scale_notes[degree] for degree in degrees]


def triad_in_the_scale(note: str, note_in_the_scale: str):
    """
    Saber se as notas de um acorde estão na escala.

    Examples:
        >>> triad_in_the_scale('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'
        >>> triad_in_the_scale('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'
        >>> triad_in_the_scale('B', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'B°'
    """
    tonic, third, fifth = triad(note, 'major')

    match third in note_in_the_scale, fifth in note_in_the_scale:
        case True, True:
            return tonic
        case False, True:
            return f'{tonic}m'
        case False, False:
            return f'{tonic}°'
