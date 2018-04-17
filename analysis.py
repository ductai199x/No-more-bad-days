import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


#---------- FUNCTIONS TO OPEN TEXT FILE TO PARSE AT A GIVEN DIRECTORY ------


#
# with open('C:\\Users\\lem1\\Desktop\\aws\\nlp\\lyrics.txt') as file:
#     content = file.readlines()
# lyrics = [x.strip() for x in content]
#
# sid = SentimentIntensityAnalyzer()
# neg = 0
# pos = 0
# neu = 0
#
# for sentence in lyrics:
#      ss = sid.polarity_scores(sentence)
#      neg += ss['neg']*100
#      pos += ss['pos']*100
#      neu += ss['neu']*100
#
# pos = format(pos / len(lyrics), '.2f')
# neg = format(neg / len(lyrics), '.2f')
# neu = format(neu / len(lyrics), '.2f')
# print ('This song is', pos, '% positive', neg, '% negative and', neu, '% neutral')
