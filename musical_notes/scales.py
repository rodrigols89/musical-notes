NOTES = 'C C# D D# E F F# G G# A A# B'.split()
SCALES = {'major': (0, 2, 4, 5, 7, 9, 11)}


def scale(tonic: str, key: str) -> dict[str, list[str]]:
    """
    Generate a scale from a tonic note (PT-BR=Nota tônica) and a key (PT-BR=tonalidade).

    Args:
        tonic: The note that will be the tonic of the scale.
        key: Scale key (PT-BR=tonalidade).

    Returns:
        A dictionary with the scale "notes" and "degrees" (PT-BR=graus). Inside of the dictionary, the key (PT-BR=tonalidade) is a string (str) and a value is a list of strings.

    Raises:
        ValueError: When passing a non-existent note.
        KeyError: When key (PT-BR=tonalidade) does not exist or not does implemented.

    Examples:
        >>> scale('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scale('a', 'major')
        {'notes': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonic = tonic.upper()
    try:
        intervals = SCALES[key]
        key_post = NOTES.index(tonic)
    except ValueError:
        raise ValueError(f'That tonic does not exist, try {NOTES}')
    except KeyError:
        raise KeyError(
            'That key (PT-BR=tonalidade) does not exist or not does implemented, '
            f'try {list(SCALES.keys())}'
        )

    temp = []

    for interval in intervals:
        note = (key_post + interval) % 12
        temp.append(NOTES[note])

    return {
        'notes': temp,
        'degrees': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'],
    }
