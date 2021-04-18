import speech_recognition as sr

def print_hi(name):
    r = sr.Recognizer()
    harvard = sr.AudioFile('audio_files_harvard.wav')
    with harvard as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    somevar = r.recognize_google(audio)
    print(somevar)

if __name__ == '__main__':
    print_hi('PyCharm')


