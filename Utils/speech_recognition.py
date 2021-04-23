import speech_recognition as sr
from langdetect import detect
import langid

def AudioToLang(audio_input):
    r = sr.Recognizer()
    context = sr.AudioFile(audio_input)
    with context as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    translated = r.recognize_google(audio)
    # print(somevar)
    langid.set_languages(['es', 'en'])  # ISO 639-1 codes
    lang, score = langid.classify(translated)
    # print(lang)
    return lang


if __name__ == '__main__':
    # print_hi('PyCharm')
    AudioToLang()


