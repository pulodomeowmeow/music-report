from music21 import *


def differ(list1: list, list2: list):
    difference_arr = []
    try:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                difference = list2[i] - list1[i]
                if difference == -2:
                    break
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


def main():
    # 解密
    file_name = str(input("Please enter the key filename: "))
    encryption_file_name = str(input("Please enter the encrypted filename: "))
    # file_name = "never.mid"
    # encryption_file_name = "output.mid"

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
            # elif isinstance(element, note.Rest):
            #     notes_array.append((-1))
            #     durations.append(element.quarterLength)

        # print the notes and rests
        # print(notes_array)
        # print(durations)
        notes_array_array.append(notes_array)
        duration_list.append(durations)
        
    longest_note_array = max(notes_array_array, key=len)
    # index = notes_array_array.index(longest_note_array)
    # print(notes_array_array.index(longest_note_array))

    encryption = converter.parse(encryption_file_name)
    # print(parts_list)
    encryption_list = []
    d_encryption = []
    # print(len(encryption.recurse()))
    for element in encryption.recurse():
        if isinstance(element, note.Note):
            encryption_list.append((element.pitch.midi))
            d_encryption.append(element.quarterLength)
        # elif isinstance(element, note.Rest):
        #     encryption_list.append((-1))
        #     d_encryption.append(element.quarterLength)
        
    # for i in range(len(encryption_list)):
    #     print(f"({longest_note_array[i]}, {encryption_list[i]})")
    
    # print()
    # print(len(longest_note_array), len(encryption_list))
    # print(longest_note_array)
    # print(encryption_list)
    # for i in range(len(longest_note_array)):
    #     print(f"({longest_note_array[i]}, {durations[i]}, {encryption_list[i]}, {d_encryption[i]})", end=" ")
    text_ascii = differ(longest_note_array, encryption_list)
    # print(text_ascii)
    text = ""
    
    for i in text_ascii:
        if i == -1:
            text += " "
        else:
            text += chr(i + 64)
            
    print(text)
    
    
    # print(f"{len(longest_note_array)}, {len(encryption_list)}")
    # print(f"The text is: {differ(longest_note_array, encryption_list)}")


if __name__ == "__main__":
    main()
