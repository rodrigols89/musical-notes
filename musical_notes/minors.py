from musical_notes.half_step import half_step
from musical_notes.triad import triad


def _minor(chord_notation):
    note, _ = chord_notation.split('m')

    if '+' in chord_notation:
        tonic, third, fifth = triad(note, 'minor')
        notes = [tonic, third, half_step(fifth, interval=1)]
        degrees = ['I', 'III-', 'V+']
    else:
        notes = triad(note, 'minor')
        degrees = ['I', 'III-', 'V']
    return notes, degrees
