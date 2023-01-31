import pywhatkit
import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import os 
import wolframalpha 
from time import sleep
from bs4 import BeautifulSoup
from playsound import playsound
import json
import requests
import Translator
from gtts import gTTS
import googletrans
import webbrowser
from decouple import config
import pyautogui
import subprocess as sp

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[-6].id)
engine.setProperty('voice', voices[6].id)
engine.setProperty('rate', 140)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("I can not hear you......")
        return "None"
    return query



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if 'next song' in query:
            speak("playing next song")
            sleep(0.3)
            pyautogui.press('spacebar')
            #pyautogui.click(x=847, y=797)  

        
        elif 'spotify' in query:
            speak("ok sir")
            speak("opening your playlist")
            url = ('https://open.spotify.com/')
            webbrowser.open(url)
            sleep(7)
            pyautogui.click(x=74, y=414)
            sleep(5)
            pyautogui.click(x=847, y=797)  
    