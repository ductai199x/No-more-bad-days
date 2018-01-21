# No-more-bad-days

A device that helps with depression by playing the auto-generated songs, trained by the data set of all the songs you love  

***OPTIMISTIC GOAL THIS WEEK: Finish the code structure for the algorithm that generates a mashup of songs***  


**IDEA:**

You and I, we all struggle in one thing: Sometimes, it's incredibly hard to find a new song, which can help you in your hardest time, with all the tunes you love. This project does just that, it composes new music that is unique to you and for you, when you needed it the most.

**EXECUTION STEPS:**

This project is devided in 3 separate parts:
1. **Emotional Dectection:** *(algorithm is open for discussion)*
	- Through facial recognition
	- Through heart pulse's patterns recognition
	- Integration of the above methods for accurate emotional reading
2. **Music Generation:** *(algorithm is open for discussion)*
	- Collect data from user's most favorite song (from metrics such as rating or frequency)
	- Recognize musical cords that user most likely love
	- Compose a 2-minute-song that includes those cords
	- Probably using tensorflow/deep learning and (neural) recurrent networks ?!?
3. **Song Mashup Generation:** *(algorithm is open for discussion)*
	- Sample user's favorite songs into an array of data
	- Detect note pattern inside songs (most frequently used note pattern)
	- Dectect sentences' block in songs by looking at rests
	- Mashup songs that has similar note patterns but cut and paste their sentences' block together
4. **Theoretical Approach to Mashup:**
	- Find the simple back ground project loop of pitch variating combination of notes
	- Find the lead note and generate the relationship between the vocal/main notes and the background notes.
	- Generate mashup based on the songs with exact same background combinations by separating a portion of this song main vocal and the next one's main vocal by the background music
	- Find algorithm based on first 3 note and their repeat in a notably fixed distance block of notes to define that own block.
	
**DISCUSSION & RESEARCH:**
- A happy song usually has the following characteristics:
	- Mostly major cords (C, D)
	- Tempo > 120 bpm
	- Happy song has a much larger quantity of do, mi, sol
- A sad song usually has the following characteristics:
	- Most sad classical songs have a lot of black/white notes at the beginning, and/or 16th, 32nd, 64th note at the end
	- Sad song have a lot more flat notes, or more legato for gentleness and smootfahness.
	- The mi-la-ti combination kinda signifies anguish/sadness many of the times
- Next step on the facial emotional detector is to use TENSORFLOWWWWWW with convolutional networks instead of just a few layers of trained classifiers
- Heart rate -> Emotion, well, we need HRV (Heart Rate Variability - the variability of time between one heart beat and the next over extended amount of time) and, train this data with a neural network :D MORE TENSORFLOW?

**WORK LOGS:** *(please conform to the format: mm/dd/yy:contributor: what_did_you_do)*  

01/17/18:Tai Nguyen: upload the list and installing methods for the dependencies used in this project  
01/18/18:Tai Nguyen: completed algorithm for facial emotional dectector, uploaded to repo with dataset 
and empty testset, update list of dependencies for MIDI and some music processing library  
01/19/18:Hoang Nguyen: came up with an algorithm to generate a mashup of songs  
01/20/18:Tai Nguyen: uploaded the code for simple music generation in tensorflow and figured out how to loop through the notes in a .midi music file.
01/21/18:Tai Nguyen: finished writing the code for the algorithm to find the "left-hand-patterns" of notes in songs. Going to use this to generate snip of music by correlating the left-hand-patterns with the right-hand notes at 4:31 am LMAO

**RESEARCH LINKS:** *(please conform to the format: #. summary: hyperlink)*
1. What a happy song usually looks like: https://www.quora.com/What-makes-a-song-happy-or-sad
2. The ultimate guide to musical keys vs emotion relationship: https://ledgernote.com/blog/lessons/musical-key-characteristics-emotions/
3. Stuff for saving trained classifier: https://stackoverflow.com/questions/10592605/save-classifier-to-disk-in-scikit-learn
4. Heart Rate Variability? https://www.psychologytoday.com/blog/sweet-emotion/201406/what-is-heart-rate-variability-and-why-does-it-matter
5. MIT's Music21 library? http://web.mit.edu/music21/doc/
