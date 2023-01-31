from password2 import password as ps
import os
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[6].id)
engine.setProperty('voice', voices[6].id)
engine.setProperty('rate', 140)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("The file is protected ")
speak("You get only one chance to open a file")

while True:
    a = int(input("Enter the password : ")) 
    if a == ps:
        speak("The password is correct ")
        speak("Opening the file")
        os.startfile("C:\\Users\\JYP\\PycharmProjects\\Python Program\\Python project (Alexa)\\Alexa.py")
        break
        
        
    elif a != ps:
        speak("Sorry the password is incorrect")
        break
            
        
    
