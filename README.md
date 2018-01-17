# No-more-bad-days

A device that helps with depression by playing the auto-generated songs, trained by the data set of all the songs you love

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
	- Probably using tensorflow/deep learning and recurrent networks ?!?
3. **Song Mashup Generation:** *(algorithm is open for discussion)*
	- Sample user's favorite songs into an array of data
	- Detect note pattern inside songs (most frequently used note pattern)
	- Dectect sentences' block in songs by looking at rests
	- Mashup songs that has similar note patterns but cut and paste their sentences' block together
	
**DISCUSSION & RESEARCH:**
- A happy song usually has the following characteristics:
	- Mostly major cords (C, D)
	- Tempo > 120 bpm
	- Happy song has a much larger quantity of do, mi, sol
- A sad song usually has the following characteristics:
	- Most sad classical songs have a lot of black/white notes at the beginning, and/or 16th, 32nd, 64th note at the end
	- Sad song have a lot more flat notes, or more legato for gentleness and smoothness.
	- The mi-la-ti combination kinda signifies anguish/sadness many of the times

**WORK LOGS:** *(please conform to the format: mm/dd/yy:contributor: what_did_you_do)*

**RESEARCH LINKS:** *(please conform to the format: #. summary: hyperlink)*
1. What a happy song usually looks like: https://www.quora.com/What-makes-a-song-happy-or-sad
2. The ultimate guide to musical keys vs emotion relationship: https://ledgernote.com/blog/lessons/musical-key-characteristics-emotions/
