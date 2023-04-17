from musical_notes.scales import NOTES


def half_step(note: str, *, interval: int) -> str:
    """
    Half-Step (Portuguese "Semitom").
    Calculate the distance between Half-Step using intervals.

    Args:
        note: An any note.
        interval: A interval in Half-Step (Portuguese "Semitom").

    Returns:
        A correspondent note to the interval.

    Examples:
        >>> half_step('C', interval=+1)
        'C#'
        >>> half_step('c', interval=-1)
        'B'
    """
    note_postion = NOTES.index(note.upper()) + interval

    return NOTES[note_postion % 12]
