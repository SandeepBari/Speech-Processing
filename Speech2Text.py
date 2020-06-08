import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

recog = spr.Recognizer()
translator = Translator()

with spr.Microphone() as source:
    print('You Can Speak Now')
    audio = recog.listen(source)
    get_sentence = recog.recognize_google(audio)
        
    try:
        text = recog.recognize_google(audio)
        print("You said : {}".format(text))
        file = open('SpokenOriginal.txt', 'w')
        file.write(text)
        file.close()
        os.system("start SpokenOriginal.txt")

    except:
        print("Something Failed !")