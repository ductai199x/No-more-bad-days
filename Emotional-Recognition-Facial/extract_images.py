import glob
from shutil import copyfile

emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"] #Define emotion order
participants = glob.glob("source_emotion//*") #Returns a list of all folders with participant numbers

for x in participants:
    part = "%s" %x[-4:] #store current participant number
    for sessions in glob.glob("%s//*" %x): #Store list of sessions for current participant
        for files in glob.glob("%s//*" %sessions):
            current_session = files[20:-30]
            print current_session
            file = open(files, 'r')

            emotion = int(float(file.readline())) #emotions are encoded as a float, readline as float, then convert to integer.

            sorcefile_list = sorted(glob.glob("source_images//%s//%s//*" %(part, current_session)))

            sourcefile_emotion = sorcefile_list[-1] #get path for last image in sequence, which contains the emotion
            print "Emotion " + sourcefile_emotion
            sourcefile_neutral = sorcefile_list[0] #do same for neutral image
            print "Neutral " + sourcefile_neutral
            dest_neut = "sorted_set//neutral//%s" %sourcefile_neutral[25:] #Generate path to put neutral image
            dest_emot = "sorted_set//%s//%s" %(emotions[emotion], sourcefile_emotion[25:]) #Do same for emotion containing image

            copyfile(sourcefile_neutral, dest_neut) #Copy file
            copyfile(sourcefile_emotion, dest_emot) #Copy file
