from music21 import *
# import tk

def differ(list1: list, list2: list):
    difference_arr = []
    try:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                difference = list2[i] - list1[i]
                difference_arr.append(difference)
    except:
        pass
    return difference_arr

def read_music_parts(file_name) -> list:
    myFile = converter.parse(file_name)
    # print(myFile.parts[0].getInstrument())
    parts_list = []
    for i in myFile.parts:
        # print(i.getInstrument().instrumentName)
        parts_list.append(i)
    return parts_list


def encrypt_a_part(note_list: list, text_list: list) -> list:
    new_list = []
    note_index = 0

    for i in range(len(text_list)):
        while note_index < len(note_list) and note_list[note_index] == -1:
            new_list.append(note_list[note_index])
            note_index += 1
        if note_index >= len(note_list):
            break

        new_list.append(note_list[note_index] + text_list[i])
        note_index += 1

    while note_index < len(note_list):
        new_list.append(note_list[note_index])
        note_index += 1
    return new_list


def main():
    file_name = str(input("Please enter the key filename: "))
    text = str(input("Please enter the text to encrypt: "))
    text_list = []  # 輸入的ASCII
    for i in text:
        if i == " ":
            text_list.append(-1)
        elif i.isalpha():
            text_list.append(ord(i.upper()) - 64)
    
    # append end signal
    text_list.append(-2)

    parts_list = read_music_parts(file_name)
    # print(parts_list)

    notes_array_array = []
    duration_list = []

    for part in parts_list:
        # # trun the note into numbers in the 0-127 range, rest is -1
        notes_array = []
        durations = []
        for element in part.recurse():
            if isinstance(element, note.Note):
                notes_array.append((element.pitch.midi))
                durations.append(element.quarterLength)
            elif isinstance(element, note.Rest):
                notes_array.append((-1))
                durations.append(element.quarterLength)

        # print the notes and rests
        # print(notes_array)
        # print(durations)
        notes_array_array.append(notes_array)
        duration_list.append(durations)

    # print(len(notes_array_array))
    longest_note_array = max(notes_array_array, key=len)
    # print(longest_note_array)
    longest_duration = max(duration_list, key=len)
    # find index of longest note array
    longest_note_array_index = notes_array_array.index(longest_note_array)
    longest_duration_array_index = duration_list.index(longest_duration)

    # print(f"{longest_note_array, longest_duration, longest_note_array_index, longest_duration_array_index}")

    new_list = encrypt_a_part(longest_note_array, text_list)
    # print(new_list, len(new_list), len(longest_note_array))
    # print(differ(longest_note_array, new_list))

    # write song

    melody = stream.Part()
    melody.append(instrument.Piano())

    for i in range(len(new_list)):
        if new_list[i] == -1:
            melody.append(note.Rest())
        else:
            melody.append(note.Note(new_list[i]))
        melody[-1].duration.quarterLength = longest_duration[i]
    
    # print(melody, len(melody))

    file_name = "output.mid"
    melody.write("midi", fp=file_name)
    print(f"The output file is saved as: {file_name}")


if __name__ == "__main__":
    main()
