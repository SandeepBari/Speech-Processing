import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

recog = spr.Recognizer()
translator = Translator()
from_lang = 'en'
to_lang = 'hi'

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

        """
        text_to_translate = translator.translate(text, src = from_lang, dest = to_lang)
        text = text_to_translate.text
        speak = gTTS(text=text, lang = to_lang, slow = False)
        speak.save("TranslatedAudio.mp3")
        """

    except:
        print("Something Failed !")