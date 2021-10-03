import pyttsx3
jarvis= pyttsx3.init()


rate=jarvis.getProperty('rate')
print(rate)
jarvis.setProperty('rate', 100)
voices=jarvis.getProperty('voices')
jarvis.setProperty('voice', voices[0].id)

jarvis.say("badal",str(rate))

jarvis.runAndWait()