from music21 import *
import glob


# Set the environment, path to midi player and path to xml music sheet viewer
# Also, go to file subConverter.py in the music21 library (probably in python-dir/Lib/site(dist)-packages/music21),
# line 183, delete "None" in "app=None"
environment.set('midiPath', '/usr/bin/timidity')
environment.set('musicxmlPath', '/usr/bin/musescore')

# Note creation:
f = note.Note("F5")
f.duration.quarterLength
# print(f)
# Stream creation (stream = array of notes)
stream2 = stream.Stream()
stream2.repeatAppend(f, 4)
# print(type(stream2))

# show('midi') will play the stream/note/song
# show() will show the music sheet. Need to install museScore or Finale to view sheet
#stream2.show('midi')

# Parse a bunch of notes and play them
#converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f#").show('midi')

# How to play a midi song in the current directory
path = glob.glob('*.mid*')
# print(path)

mf = converter.parse(path[0]) #.show('midi') to play song

# This will play the "left hand" of the piano song
for stream in mf:
    for notes in stream.pitches:
        print(notes.midi, notes)

# Chord creation
cMinor = chord.Chord(["C4","G4","E-5"])
# cMinor.show('midi')