import pyttsx

engine = pyttsx.init()

def speak(text):
    engine.say(text)

    engine.runAndWait()

def setVoice(value):
    voices = engine.getProperty('voices')
    if value == 1:
        engine.setProperty('voice', voices[1].id)
    elif value == 2:
        engine.setProperty('voice', voices[0].id)

value = int(input('Welcome, Press 1 for male voice\n Press 2 for female voice.\n'))

setVoice(value)

text = input('Hello there, enter a command!\n')

speak(text)

