#0. Import Libraries
from colorama import Fore
import random
from textblob import TextBlob
import speech_recognition as sr
import pyttsx3

s = sr.Recognizer()



engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



#Loading Required Files For FUrther Analysis
# f = open("StopWords_GenericLong.txt", "r")
# content = f.read()
# stopwords_given = content.split("\n")
# f.close()
# master_dict = pd.read_csv("Loughran-McDonald_MasterDictionary_1993-2021.csv")





# Sentimental Analysis
# class Sentiment_Analysis:
#     def __init__(self, ans):
#         self.ans = ans.upper().split()
#
#         pos_words = [word for word, score in zip(master_dict['Word'], master_dict['Positive']) if
#                      score > 0 and not word in stopwords_given]
#         neg_words = [word for word, score in zip(master_dict['Word'], master_dict['Negative']) if
#                      score > 0 and not word in stopwords_given]
#
#         positive = 0
#         negative = 0
#         no_of_words = (len(ans))
#
#         for word in ans:
#             if word in pos_words:
#                 positive += 1
#             elif word in neg_words:
#                 negative += 1
#
#         self.polarity_score = (positive - negative) / ((positive + negative) + 0.000001)
#         self.subjectivity_score = (positive + negative) / (no_of_words + 0.000001)




try:
    #1. Name and nickname conversation

    # print(Fore.RED + "EVE :>   Hello human, I am Eve, you can have me as your personal companion, may I know your name?\n")
    # speak("Hello human, I am Eve, you can have me as your personal companion, may I know your name?")
    #
    # # name = input()
    # with sr.Microphone() as source:
    #     print(Fore.YELLOW + "Say somethnig: \n")
    #     s.pause_threshold = 1496.57047566
    #     audio = s.listen(source, timeout=7, phrase_time_limit=7)
    #     print(Fore.YELLOW + "recognizing...\n")
    #     query = s.recognize_google(audio, language = 'en-in')
    #     name = query
    #     print(Fore.GREEN + 'You :>  ', query, '\n')
    #
    #
    #
    # print(Fore.RED + "EVE :>   Do you have nickname?\n")
    # speak("Do you have nickname?")
    #
    #
    # with sr.Microphone() as source:
    #     print(Fore.YELLOW + "Say somethnig: \n")
    #     s.pause_threshold = 1496.57047566
    #     audio = s.listen(source, timeout=7, phrase_time_limit=7)
    #     print(Fore.YELLOW + "recognizing...\n")
    #     query = s.recognize_google(audio, language = 'en-in')
    #     print(Fore.GREEN + 'You :>  ', query, '\n')
    #     ans = query
    #
    #
    # if 'y' in ans.lower():
    #     print(Fore.RED + "EVE :>   Coool!!!, I love nicknames. What's your nickname?\n")
    #     speak("Coool!!!, I love nicknames. What's your nickname?")
    #
    #     with sr.Microphone() as source:
    #         print(Fore.YELLOW + "Say somethnig: \n")
    #         s.pause_threshold = 1496.57047566
    #         audio = s.listen(source, timeout=7, phrase_time_limit=7)
    #         print(Fore.YELLOW + "recognizing...\n")
    #         query = s.recognize_google(audio, language='en-in')
    #         print(Fore.GREEN + 'You :>  ', query, '\n')
    #         nickname = query
    #
    #     print(Fore.RED + "EVE :>   Good to meet you " + nickname + '\n')
    #     speak("Good to meet you " + nickname)
    # else:
    #     nickname = name
    #     print(Fore.RED + 'EVE :>   I will call you then ' + nickname + '\n')
    #     speak('I will call you then ' + nickname)
    #
    #
    #
    #
    #
    # #Greeting selection
    # greetings = [
    #     f"How are you today {nickname}?",
    #     f"Howdy {nickname}, how are you feeling?",
    #     f"What's up {nickname}?",
    #     f"Greetings {nickname}, are you well?",
    #     f"How are things going {nickname}?"
    # ]
    #
    # greeting = random.choice(greetings)
    #
    # print(Fore.RED + "EVE :>   ", greeting, '\n')
    # speak(greeting)
    #
    # with sr.Microphone() as source:
    #     print(Fore.YELLOW + "Say somethnig: \n")
    #     s.pause_threshold = 1496.57047566
    #     audio = s.listen(source, timeout=7, phrase_time_limit=7)
    #     print(Fore.YELLOW + "recognizing...\n")
    #     query = s.recognize_google(audio, language='en-in')
    #     print(Fore.GREEN + 'You :>  ', query, '\n')
    #     ans = TextBlob(query)
    #
    # if ans.polarity > 0:
    #     # print(ans.polarity)
    #     print(Fore.RED + "EVE :>   Glad you are doing well\n")
    #     speak("Glad you are doing well")
    # else:
    #     # print(ans.polarity)
    #     print(Fore.RED + "EVE :>   Sorry to hear that\n")
    #     speak("Sorry to hear that")
    #
    #
    #
    #
    #
    # # 3. Several random opinions on topic
    # topics = [
    #     'football',
    #     'Melbourne',
    #     'AFL',
    #     'Endgame',
    #     'Python',
    #     'Computers',
    #     'Computer games'
    # ]
    #
    # questions = [
    #     'What is your take on ',
    #     'What do you think about ',
    #     'How do you feel about ',
    #     'What do you reckon about ',
    #     'I would like your opinion on '
    # ]
    #
    # for i in range(0, random.randint(3, 4)):
    #     question = random.choice(questions)
    #     questions.remove(question)
    #     topic = random.choice(topics)
    #     topics.remove(topic)
    #
    #     print(Fore.RED + "EVE :>   ", question + topic + '?\n')
    #     speak(question + topic + '?')
    #
    #     with sr.Microphone() as source:
    #         print(Fore.YELLOW + "Say somethnig: \n")
    #         s.pause_threshold = 1496.57047566
    #         audio = s.listen(source, timeout=7, phrase_time_limit=7)
    #         print(Fore.YELLOW + "recognizing...\n")
    #         query = s.recognize_google(audio, language='en-in')
    #         print(Fore.GREEN + 'You :>  ', query, '\n')
    #         ans = TextBlob(query)
    #
    #
    #     if ans.polarity > 0.5:
    #         # print(ans.polarity)
    #         print(Fore.RED + 'EVE :>   OMG you really love ' + topic + '\n')
    #         speak('OMG you really love ' + topic)
    #     elif ans.polarity > 0:
    #         # print(ans.polarity)
    #         print(Fore.RED + 'EVE :>   Well, you clearly like ' + topic + '\n')
    #         speak('Well, you clearly like ' + topic)
    #     elif ans.polarity < -0.5:
    #         # print(ans.polarity)
    #         print(Fore.RED + 'EVE :>   Woof, you totally hate ' + topic + '\n')
    #         speak('Woof, you totally hate ' + topic)
    #     elif ans.polarity < 0:
    #         # print(ans.polarity)
    #         print(Fore.RED + "EVE :>   So you don't like " + topic + '\n')
    #         speak("So you don't like " + topic)
    #     else:
    #         # print(ans.polarity)
    #         print(Fore.RED + 'EVE :>   That is a very neutral view on ' + topic + '\n')
    #         speak('That is a very neutral view on ' + topic)
    #
    #     if ans.subjectivity > 0.6:
    #         # print(ans.subjectivity)
    #         print(Fore.RED + 'EVE :>   and you are so biased\n')
    #         speak('and you are so biased')
    #     elif ans.subjectivity > 0.3:
    #         # print(ans.subjectivity)
    #         print(Fore.RED + 'EVE :>   and you are a bit biased\n')
    #         speak('and you are a bit biased')
    #     else:
    #         # print(ans.subjectivity)
    #         print(Fore.RED + 'EVE :>   and you are quite objective\n')
    #         speak('and you are quite objective')
    #
    #
    #
    #
    #
    # # 4. Random goodbye
    #
    # goodbyes = [
    #     'Good talking to you ' + nickname + 'I gotta go now....bye and take care',
    #     'OK I am bored, I will go watch Netflix.....bye and take care',
    #     'Yaaawn . . . I gotta go now......bye and take care',
    #     'Catch ya later ' + nickname + ', bye and take care'
    # ]
    #
    #
    # goodbye = random.choice(goodbyes)
    # print(Fore.RED + "EVE :>   ", goodbye, '\n')
    # speak(goodbye)
    with sr.Microphone() as source:
        print(Fore.YELLOW + "Say somethnig: \n")
        s.pause_threshold = 1496.57047566
        audio = s.listen(source, timeout=7, phrase_time_limit=7)
        print(Fore.YELLOW + "recognizing...\n")
        query = s.recognize_google(audio, language='en-in')
        print(Fore.GREEN + 'You :>  ', query, '\n')

    speak(query)

except:
    speak("EVE :>   Sorry! couldn't process your input")
    print(Fore.RED + "Sorry! couldn't process your input\n")