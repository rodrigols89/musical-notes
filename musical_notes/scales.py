NOTES = 'C C# D D# E F F# G G# A A# B'.split()
ESCALES = {'major': (0, 2, 4, 5, 7, 9, 11)}


def scales(note: str, key: str) -> dict[str, list[str]]:
    """
    Generate a scale from a note and a tone (key).

    Parameters:
        note: The note that will be the tonic of the scale.
        key: Scale tone (key).

    Returns:
        A dictionary with the scale notes and degree. Inside of the dictionary, the key is a string (str) and a value is a list of strings.

    Examples:
        >>> scales('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scales('A', 'major')
        {'notes': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    intervals = ESCALES[key]
    key_post = NOTES.index(note)
    temp = []

    for interval in intervals:
        note = (key_post + interval) % 12
        temp.append(NOTES[note])

    return {'notes': temp, 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
