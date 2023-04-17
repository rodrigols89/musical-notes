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
