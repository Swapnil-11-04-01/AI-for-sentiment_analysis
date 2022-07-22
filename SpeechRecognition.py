# import speech_recognition as sr
#
# s = sr.Recognizer()
#
# with sr.Microphone() as source:
#     print("Say somethnig: ")
#     s.pause_threshold = 1496.57047566
#     audio = s.listen(source, timeout=5, phrase_time_limit=5)
#     print("recognizins...")
#     query = s.recognize_google(audio, language = 'en-in')
#     print(query)

import random
import pandas as pd

f = open("StopWords_GenericLong.txt", "r")
content = f.read()
stopwords_given = content.split("\n")
f.close()
master_dict = pd.read_csv("Loughran-McDonald_MasterDictionary_1993-2021.csv")

pos_words = [word for word, score in zip(master_dict['Word'], master_dict['Positive']) if score > 0 and not word in stopwords_given]
neg_words = [word for word, score in zip(master_dict['Word'], master_dict['Negative']) if score > 0 and not word in stopwords_given]
print(pos_words, '\n')
print(neg_words)

# Sentimental Analysis
class Sentiment_Analysis:
    def __init__(self, ans):
        self.ans = ans.upper().split()

        positive = 0
        negative = 0
        no_of_words = (len(ans))

        for word in self.ans:
            print(word)
            if word in pos_words:
                positive += 1
            elif word in neg_words:
                negative += 1

        self.polarity_score = (positive - negative) / ((positive + negative) + 0.000001)
        self.subjectivity_score = (positive + negative) / (no_of_words + 0.000001)

review = Sentiment_Analysis(input())

print(review.ans)
print(review.polarity_score)
print(review.subjectivity_score)