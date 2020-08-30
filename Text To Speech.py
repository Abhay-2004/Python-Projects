import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[40].id)
engine.say(input("Enter the text here: "))
engine.runAndWait()