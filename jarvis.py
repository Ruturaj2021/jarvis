
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print ("Initializing Jarvis")
MASTER="Ruturaj"
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(text):
   engine.say(text)
   engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour <12 :
        speak("Good Morning"+ MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ MASTER)


    else:
        speak("Good Evening"+MASTER)
    
    speak("I am Jarvis. how may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone (device_index=0) as source:
        print("Listening...")
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language = 'en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
       print("Say that again please")
       

speak("Initializing Jarvis...")
wishMe()






