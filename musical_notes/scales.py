NOTES = 'C C# D D# E F F# G G# A A# B'.split()
SCALES = {'major': (0, 2, 4, 5, 7, 9, 11)}


def scale(note: str, key: str) -> dict[str, list[str]]:
    """
    Generate a scale from a note and a tone (key).

    Parameters:
        note: The note that will be the tonic of the scale.
        key: Scale tone (key).

    Returns:
        A dictionary with the scale notes and degree. Inside of the dictionary, the key is a string (str) and a value is a list of strings.

    Raises:
        ValueError: When passing a non-existent note.
        KeyError: When key (tone) does not exist or not does implemented.

    Examples:
        >>> scale('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scale('a', 'major')
        {'notes': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    note = note.upper()
    try:
        intervals = SCALES[key]
        key_post = NOTES.index(note)
    except ValueError:
        raise ValueError(f'That note does not exist, try {NOTES}')
    except KeyError:
        raise KeyError(
            'That key (tone) does not exist or not does implemented, '
            f'try {list(SCALES.keys())}'
        )

    temp = []

    for interval in intervals:
        note = (key_post + interval) % 12
        temp.append(NOTES[note])

    return {'notes': temp, 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
