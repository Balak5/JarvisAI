from calendar import month
import pyttsx
import datetime

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

def time():
    time = datetime.datetime.now().strftime("%I:%M:%S") # hour minute second
    speak('the time is -')
    speak(time)

def date():
    # make the 
    year = datetime.datetime.now().year
    month  = datetime.datetime.now().month
    day = datetime.datetime.now().day

    speak('the current date is ')
    speak(getMonth(month))
    speak(day)
    speak(year)

def getMonth(monthNum):
    if monthNum == 1:
        return 'January'
    elif monthNum == 2:
        return 'February'
    elif monthNum == 3:
        return 'March'
    elif monthNum == 4:
        return 'April'
    elif monthNum == 5:
        return 'May'
    elif monthNum == 6:
        return 'June'
    elif monthNum == 7:
        return 'July'
    elif monthNum == 8:
        return 'August'
    elif monthNum == 9:
        return 'Spetember'
    elif monthNum == 10:
        return 'October'
    elif monthNum == 11:
        return 'November'
    elif monthNum == 12:
        return 'December'

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('Good Morning sir')
    elif hour >= 12 and hour < 17:
        speak('Good Afternoon sir')
    elif hour > 17 and hour < 19:
        speak('Good Evening sir')
    else:
        speak('How is your night sir')

def wishme():
    setVoice(1)
    speak('Welcome back sir')
    time()
    date()
    greeting()
    speak('Jarvis at your service, your command is my wish')

# while True:

#     value = int(input('Welcome, Press 1 for male voice\n Press 2 for female voice.\n'))

#     setVoice(value)

#     text = input('Hello there, enter a command!\n')

#     speak(text)

wishme()
