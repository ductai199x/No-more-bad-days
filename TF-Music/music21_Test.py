from music21 import *
import glob

# Set the environment, path to midi player and path to xml music sheet viewer
# Also, go to file subConverter.py in the music21 library (probably in python-dir/Lib/site(dist)-packages/music21),
# line 183, delete "None" in "app=None"
# environment.set('midiPath', '/usr/bin/timidity')
# environment.set('musicxmlPath', '/usr/bin/musescore')

def read_in_song(song_name):
    global song_array
    # How to play a midi song in the current directory
    path = glob.glob(song_name)
    mf = converter.parse(path[0])  # .show('midi') to play song

    # This will examine the "left hand" of the piano song
    song_array = []
    for song_stream in mf:
        # stream.notes.show('midi')
        for notes in song_stream.notes:
            try:
                print(notes.midi, notes.pitch)
                song_array.append(notes.pitch.name)  # .name+notes.pitch.octave)
            except:
                pass


def song_simplification():
    global song_array
    global simplified_song
    first_note = 0
    last_note = 0
    simplified_song = []
    is_main_note = False
    is_continue = False
    i = 0

    while (i < len(song_array) - 1 - 4):
        for j in range(i + 1, len(song_array) - 2):
            if song_array[i] == song_array[j]:
                is_continue = True
                i = j
                break
            else:
                if j - i > 2:
                    is_main_note = True
                    last_note = j - 2
                    break
                else:
                    is_main_note = False
                    continue
        if is_main_note == True:
            simplified_song.append(song_array[last_note - 1])
            is_main_note = False
            i = last_note + 1

    print(simplified_song)
    song_str = " ".join(str(e) for e in simplified_song).lower()
    # print (song_str)
    converter.parse('tinyNotation: ' + song_str, makeNotation=False).show('midi')


def find_patterns_of_notes():
    # patterns of notes = combo
    global song_array
    global simplified_song
    global most_freq_combo
    most_freq_combo = {}
    combo_index = 1
    num_notes_in_combo_list = [3, 4, 5, 7, 11, 13]

    for num_notes_in_combo in num_notes_in_combo_list:
        isCombo = False
        first_note_in_combo = 0
        for x in range(0, len(simplified_song) - 1 - num_notes_in_combo - 1):
            y = x + num_notes_in_combo
            n = num_notes_in_combo * 3
            while (y < len(simplified_song) - 1 and y - x < n):
                if x > first_note_in_combo and simplified_song[x] == simplified_song[first_note_in_combo]:
                    n = num_notes_in_combo * 2
                note1 = simplified_song[x]
                note2 = simplified_song[y]
                if note1 != note2:
                    isCombo = False
                    break
                else:
                    isCombo = True
                    y += num_notes_in_combo
                    continue

            if isCombo == False:
                first_note_in_combo += 1
            else:
                if x - num_notes_in_combo == first_note_in_combo:
                    combo = simplified_song[x - num_notes_in_combo: x]
                    most_freq_combo[combo[0] + "_" + str(combo_index)] = combo
                    first_note_in_combo = x + 1
                    combo_index += 1
                    print(num_notes_in_combo)
                else:
                    continue

    print(most_freq_combo)

if __name__ == "__main__":
    read_in_song('In The End.mid*')
    # read_in_song('Numb.mid*')
    # read_in_song('Barbie Girl.mid*')
    song_simplification()
    find_patterns_of_notes()