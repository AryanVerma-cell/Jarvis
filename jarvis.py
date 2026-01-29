import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musiclib
import requests
from brain import ask_ai
from bs4 import BeautifulSoup

recognizer = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
     c = c.lower()
     if "google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")
     elif "youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
     elif "facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
     elif "linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
     elif c.startswith("play"):
         song = " ".join(c.lower().split(" ")[1:]).strip()

         link=musiclib.music[song]
         webbrowser.open(link)
     elif "news" in c:
        try:
           
           speak("Fetching today's top headlines")

           url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
           r = requests.get(url)
           soup = BeautifulSoup(r.content, "xml")
           items = soup.find_all("item")[:5]

        

           for item in items:
            title = item.title.text
            print("News:", title)
            speak(title)
            time.sleep(2)

        except Exception as e:
            print("News Error:", e)
            speak("Unable to fetch news right now")
     
     else :
         answer = ask_ai(c)
         speak(answer)
         print(answer)      

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    activated=False
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, phrase_time_limit=6)
            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "jarvis" in word.lower():
                speak("yes boss")
                if not activated:
                    print("Jarvis Active...")
                    activated = True
                while True:
                    try:
                        with sr.Microphone() as source:
                            audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print("You said:", command)

                        if "stop" in command.lower():
                            speak("Going to sleep")
                            break   # exit command mode, wait for "jarvis" again
                        processCommand(command)
                    except:
                        pass
        except Exception as e:
            print("Error",e)


