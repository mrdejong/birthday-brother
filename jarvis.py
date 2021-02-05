import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print(voice.gender)
    print(voice.languages)

engine.setProperty('voice', voices[7].id) # voice 7 is a brithish male voice.

engine.say('Good morning Alexander')

engine.runAndWait()
