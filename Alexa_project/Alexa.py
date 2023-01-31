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
print(voices[6].id)
engine.setProperty('voice', voices[6].id)
engine.setProperty('rate', 140)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=18c4881ad66a4a13aa7b4d61246b3035",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=18c4881ad66a4a13aa7b4d61246b3035",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=18c4881ad66a4a13aa7b4d61246b3035",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=18c4881ad66a4a13aa7b4d61246b3035",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=18c4881ad66a4a13aa7b4d61246b3035",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=18c4881ad66a4a13aa7b4d61246b3035",
            "political" :"https://newsapi.org/v2/top-headlines?country=in&apiKey=18c4881ad66a4a13aa7b4d61246b3035",
            "historical" :"https://newsdata.io/api/1/archive?apikey=18c4881ad66a4a13aa7b4d61246b3035&q=metaverse"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    print("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")    

def WolfRamAlpha(query):
    apikey = 'R42XGQ-2XVHV57XH4'
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("into","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)

def searchfirefox(query):
    if "firefox" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("firefox search","")
        query = query.replace("firefox","")
        speak("This is what I found on firefox")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")        

def translategl(query):
    speak("SURE SIR")
    print(googletrans.LANGUAGES)
    translator = translator()
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")   
    text_to_translate = translator.translate(query,src = "auto",dest= b,)
    text = text_to_translate.text
    try : 
        speakgl = gTTS(text=text, lang=b, slow= False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        
        time.sleep(5)
        os.remove("voice.mp3")
    except:
        print("Unable to translate")

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']        

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hii, I am alexa talk something to wake up me")    
    query = takeCommand()
    speak("hello sir , how can i help you")
    if "i am fine" in query:
        speak("that's great, sir")
    elif "how are you" in query:
        speak("Perfect, sir")
    elif "thank you" in query:
        speak("you are welcome, sir")  

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
    wishMe()
    while True:
        query = takeCommand().lower()

        if ' wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("according to wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)    

        elif 'open youtube' in query:
            speak("ok sir")
            speak("opening the youtube")
            sp.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'https://www.youtube.com'])

        elif 'open google' in query:
            speak("ok sir")
            speak("opening the google ")
            sp.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'what the current time' in query:
            speak("ok sir")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open my photo' in query:
            speak("ok sir")
            speak("opening the photoes")
            codePath = "C:\\Users\JYP\Desktop\photoes"
            os.startfile(codePath)

        elif 'volume up' in query:
            speak("ok sir")
            speak("Increase the volume")
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            speak("ok sir")
            speak("Decrease  the volume")
            pyautogui.press("volumedown")

        elif 'volume mute' in query:
            speak("ok sir")
            speak("Mute the volume")
            pyautogui.press("volumemute")

        elif ' open microsoft edge' in query:
            speak("ok sir")
            speak("opening the microsoft edge")
            sp.Popen(['C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'])

        elif 'thank you alexa now you can sleep' in query:
            speak("It's my pleasure sir")
            speak("I hope you are enjoying !")
            speak("Have a good day")
            exit()

        elif 'today temperature' in query:
            speak("ok sir")
            search = "temperature in bhusawal"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temperature = data.find("div", class_="BNeawe").text
            speak(f"The temperature of bhusawal is {temperature}")
        
        elif 'open microsoft excel' in query:
            speak("Ok sir")
            speak("Opening the microsoft excel")
            sp.Popen("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE")

        elif 'open microsoft powerpoint' in query:
            speak("Ok sir")
            speak("Opening the microsoft powerpoint")
            sp.Popen("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

        elif 'open microsoft word' in query:
            speak("Ok sir")
            speak("Opening the microsoft word")    
            sp.Popen("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

        elif 'open whatsapp' in query:
            speak("Ok sir")
            speak("Opening the whatsapp") 
            sp.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 'https://web.whatsapp.com/'])   

        elif "weather" in query:
            search = "temperature in bhusawal"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")    

        elif "google" in query:
            searchGoogle(query)

        elif "youtube" in query:
            searchYoutube(query)

        elif "play music" in query:
            speak("This is what I found for your search!") 
            query = query.replace("youtube search","")
            query = query.replace("youtube","")
            url  = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(url)
            pywhatkit.playonyt(query)
            speak("Done sir")   

        elif "open my email" in query:
            speak("Ok sir")
            speak("opening your email")
            sp.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe','https://mail.google.com/mail/u/0/?ogbl#inbox'])
        
        elif 'open firefox' in query:
            speak("ok sir")
            speak("Opening firefox")
            sp.Popen('C:\\Program Files\\Mozilla Firefox\\firefox.exe')        

        elif "translate" in query:
            from Translator import translategl 
            query = query.replace("Alexa","")
            query = query.replace("translate","")
            translategl(query)  

        elif "calculate" in query:
            WolfRamAlpha(query)
            Calc(query)
            query = query.replace("calculate","")
            query = query.replace("alexa","")             

        elif 'spotify' in query:
            speak("ok sir")
            speak("opening your playlist")
            url = ('https://open.spotify.com/')
            webbrowser.open(url)
            sleep(7)
            pyautogui.click(x=74, y=414)
            sleep(5)
            pyautogui.click(x=847, y=797)  

        elif 'next song' in query:
            speak("playing next song")
            sleep(0.3)
            pyautogui.press(49)
            #pyautogui.click(x=847, y=797)    

        elif'close the window' in query:
            speak("ok sir")
            speak("Closing the window")
            sleep(0.3)
            pyautogui.click(x=1574, y=11)  

        elif'minimise the window' in query:
            speak("ok sir")
            speak("minimize the window")
            sleep(0.3)   
            pyautogui.click(x=1485, y=9)   

        elif'maximize the window' in query:
            speak("ok sir")
            speak("maximize the window")
            sleep(0.3) 
            pyautogui.click(x=1527, y=14)   

        elif'open the playlist' in query:
            speak("ok sir")
            speak("playing lata mangeshkwar songs")
            url = ('https://open.spotify.com/')
            webbrowser.open(url)
            sleep(7)
            pyautogui.click(x=126, y=257)
            sleep(4)
            pyautogui.click(x=618, y=101)
            sleep(3)
            pyautogui.click(x=1026, y=291)
            sleep(3)
            pyautogui.click(x=518, y=461)
            sleep(4)
            pyautogui.click(x=599, y=545)
            sleep(4)
            pyautogui.click(x=301, y=459)

        elif'pause the song' in query:
            speak("ok sir")
            speak("pause the music")
            sleep(0.3)
            pyautogui.click(x=802, y=801)  

        elif'play the song' in query:
            speak("ok sir")
            speak("play the music")
            sleep(0.3)
            pyautogui.click(x=802, y=801)        

        elif'previous song' in query:
            speak("ok sir")
            speak("play previous song")
            sleep(0.3)
            pyautogui.click(x=754, y=797)  
            pyautogui.click(x=754, y=797) 
            pyautogui.click(x=754, y=797)   

        elif'activate home automation mode' in query:
            speak("ok sir")
            speak("opening the home automation mode")
            pyautogui.click(x=424, y=133)
            pyautogui.click(x=424, y=133)
            sleep(10) 

        elif 'set alarm' in query:
            speak("ok sir") 
            speak("Please Enter the time below")
            time = input("Enter the number : ")
            speak("Alarm has been set")

            while True:
                Time_now = datetime.datetime.now()
                now = Time_now.strftime("%H:%M:%S")

                if now == time:
                    speak("Wake up sir !!")
                    speak("Alram has ringing")
                    speak("Its time to wakeup")
                    playsound("C:\\Users\\JYP\\OneDrive\\Pictures\\alram.mp3")
                    speak("Alarm Closed !!")

                elif now > time:
                    break

        elif 'whatsapp' in query:
            speak("You want to sure that to send a whatsapp message then write yes or no")
            yes = input("You want to sure that to send a whatsapp message write { yes / no } : ")
            no = 1
            while 'yes' in yes:
                name = takeCommand()
                if'Jayashree' in name:
                    speak("Enter the message")
                    msg =input("Enter the Message : ")
                    speak("tell me the time sir")
                    speak("Enter only in hour")
                    hour = int(input("Enter the hour :"))
                    speak("Enter only minutes")
                    min = int(input("Enter the minutes :")) 
                    pywhatkit.sendwhatmsg("+918668519095",msg,hour,min,15)
                    speak("ok sir, Sending the whatsapp message !")
                    sleep(4)
                    pyautogui.click(x=1542, y=804)
                    speak("Message will be delivered")

                elif 'yogesh' in name:
                    speak("Tell me the message")
                    msg = input("Enter the Message : ")
                    speak("tell me the time sir")
                    speak("Enter only hour")
                    hour = int(input("Enter the hour :"))
                    speak("Enter only minutes")
                    min = int(input("Enter the minutes :")) 
                    pywhatkit.sendwhatmsg("+919420110923",msg,hour,min,20)
                    speak("ok sir, Sending the whatsapp message !")
                    sleep(4)
                    pyautogui.click(x=1542, y=804)
                    speak("Message will be delivered")    

                elif 'not send message' in name:
                    speak("ok sir")
                    speak("Not sending the whatsapp message")        
                    break


        elif'advice' in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)  

        elif "news" in query:
            latestnews()   

        elif "ipl score" in query:
                    from plyer import notification  
                    import requests 
                    from bs4 import BeautifulSoup 
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )     

        elif "play a game" in query:
                    from game import game_play
                    game_play()            
