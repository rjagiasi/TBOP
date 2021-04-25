import speech_recognition as sr
from langdetect import detect, detect_langs
import langid

def AudioToLang(audio_input):
    r = sr.Recognizer()
    context = sr.AudioFile(audio_input)
    #context =  audio_input
    with context as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    translated = r.recognize_google(audio)
    #print(translated)
    # print(somevar)
    #langid.set_languages(['es', 'en'])  # ISO 639-1 codes
    #lang, score = langid.classify(translated)
    lang = detect(translated)
    #print(lang)
    if lang =='en':
        lang = 2
    elif lang =='es':
        lang = 1
    else:
        lang = 5
    #print(lang)
    return lang


if __name__ == '__main__':
    # print_hi('PyCharm')
    AudioToLang()


