from music21 import *
import random
from jiami import *

# from jiemi import *


def main():
    # print("main")
    string = str(input("Enter a string: "))
    music_scale, duration = func(string)
    # print(music_scale)
    melody = stream.Part()
    instru = instrument.Flute()
    melody.append(instru)
    chord_part = stream.Part()
    chord_part.append(instrument.Piano())
    cmaj = [48, 52, 55]
    fmaj = [53, 57, 60]
    gmaj = [55, 59, 62]

    for i in range(len(music_scale)):
        midi_pitch = music_scale[i]
        if midi_pitch == -1:
            r = note.Rest()
            r.quarterLength = duration[i]
            melody.append(r)
            chord_part.append(r)
        else:
            if midi_pitch % 12 == 0 or midi_pitch % 12 == 4:
                c = chord.Chord(cmaj)
            elif midi_pitch % 12 == 5 or midi_pitch % 12 == 9:
                c = chord.Chord(fmaj)
            else:
                c = chord.Chord(gmaj)

            quarter_length = duration[i]
            c.quarterLength = quarter_length
            chord_part.append(c)

            n = note.Note(midi_pitch)
            n.quarterLength = quarter_length
            melody.append(n)

    # melody.show("text")
    # melody.show("midi")

    nScore = stream.Score()
    nScore.insert(0, melody)
    nScore.insert(0, chord_part)
    # nScore.show("text")
    # nScore.show('midi')

    file_name = "output.mid"
    nScore.write("midi", fp=file_name)
    print(f"The output file is saved as: {file_name}")


if __name__ == "__main__":
    main()
