def convert_degrees(chord_notation: str, degree: str):
    """
    Converts relative degree to Chord notation (Chord symbols or Portuguese "Cifra").

    Args:
        chord_notation: A Chord notation (Chord symbols or Portuguese "Cifra") in form of chord.
        degree: Degree in major form.

    Examples:
        >>> convert_degrees('C', 'I')
        'I'
        >>> convert_degrees('Cm', 'I')
        'i'
        >>> convert_degrees('C°', 'I')
        'i°'
    """
    if 'm' in chord_notation:
        return degree.lower()

    if '°' in chord_notation:
        return f'{degree.lower()}°'

    return degree
