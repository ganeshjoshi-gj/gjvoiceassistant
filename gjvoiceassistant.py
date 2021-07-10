"""
---------------GJ's Desktop Voice Assistant---------------

"""
#Used Python 3 and Google's Speech Recognition API
# Importing Required Modules

"""
---------------GJ's Desktop Voice Assistant---------------

"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import requests
import json
import random

#Initializing
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

"""
Writing Functions
"""


def speak(audio):
    """
    speak() function will speak the string we give as an argument - Text To Speech
    """
    print(f"GJ's Assistant: {audio}")
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """
    wishMe() Function Will Wish User According To Current Time
    """

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {name} sir")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {name} sir")
    else:
        speak(f"Good Evening {name} sir")


def takeCommand():
    """
    This Function Will Take Microphone Input From The User And Return String Output
    """
    while(True):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            speak("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            speak("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            speak(f"You Said: {query}\n")
        except Exception:
            speak("Say That Again Please!!")
        else:
            return query


def setName(startupcall=True):  # if startupcall is False it means user want to change name
    if(startupcall == True):
        speak("Hello Sir, What's Your Name?")
    else:
        speak("Tell Me Your New Name Sir")
    namecorrect = False
    while(True):
        tname = takeCommand()
        while(True):
            speak(f"Your Name Is {tname},Right Sir?\nPlease Say Yes Or No.")
            confirm = takeCommand().lower()
            if("yes" in confirm):
                global name
                if(startupcall == True):
                    speak("Ok Sir")
                    name = tname
                    done = True
                    break
                else:
                    speak("Your Name Has Been Changed Sir")
                    speak(f"Your Old Name Was {name}")
                    speak(f"Your New Name is {tname}")

                name = tname
                break
            elif("no" in confirm):
                speak("Sorry Sir,Asking Again!!")
                speak("Please Tell Again,What's Your Name Sir?")
                tname = takeCommand()

            else:
                speak("Please Say Yes or No Only...")
        if done:
            break


name = "Sir"  # Setting Default Name as Sir
"""
    Taking User's Name and Greeting Welcome
"""

setName()

speak(f"Welcome {name} Sir")
wishMe()

while(True):

    query = takeCommand().lower()
    if "wikipedia" in query:
        if query == "wikipedia":
            speak("Please Say Wikipedia <query>")
            speak("For Example, You Can Say Wikipedia Sachin Tendulkar")
        else:
            query = query.replace("wikipedia", "")
            try:
                speak("Searching In Wikipedia")
                results = wikipedia.summary(query, sentences=2)

                speak("According To Wikipedia.....")
                speak(results)
            except Exception as e:
                speak("Unable to understand,Please Say That Again")
                
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
        speak("Please Wait....")
        speak("Opening YouTube Sir....")
        
    elif "open google" in query:
        webbrowser.open("google.com")
        speak("Please Wait....")
        speak("Opening Google Sir....")
        
    elif "open stackoverflow" in query or "open stack overflow" in query:
        webbrowser.open("stackoverflow.com")
        speak("Please Wait....")
        speak("Opening Stackoverflow Sir....")
        
    elif "play music" in query:
        musicdir = "C:\\Users\\BHERULALJOSHI\\Music\\DemoMusicPython"
        songs = os.listdir(musicdir)
        speak(f"Playing {songs[0]}....")
        
        os.startfile(os.path.join(musicdir, songs[0]))
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir The Time Is {strTime}")
        
    elif "open code" in query or "open visual studio code" in query:
        codepath = "D:\\Users\\BHERULALJOSHI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Opening Visual Studio Code....")
        os.startfile(codepath)
        
    elif "what's my name" in query or "what is my name" in query or "do you know my name" in query:
        speak("I remember your name sir")
        speak(f"Your name is {name}")
        
    elif "change my name" in query or "change name" in query:
        speak("Ok Sir")
        setName(startupcall=False) #startupcall=False Because User Wants to Change The Username
        
    elif "who made you" in query or "owner of you" in query or "who created you" in query or "founder of you" in query:
        speak("Ganesh Joshi aka GJ is the developer of GJ's Voice Assistant")
        speak("Ganesh Joshi Created Me To Help Users")
        speak("I am very glad to help users like you")
        speak("Keep Using Me:)")

    elif "quit" in query or "stop" in query or "exit" in query or "bye" in query:
        speak("Ok Sir...")
        speak("Thank You For Using Me....")
        speak(f"Program Exiting {name} Sir")
        if "bye" in query:
            speak("Good Bye Sir")
        speak("Have a Nice Day!!")
        exit()

    elif "search" in query or "search on google" in query:
        if "search" in query and "on google" in query:
            temp = query.replace("search", "")
            temp = temp.replace("on google", "")
            speak("Please Wait....")
            speak(f"Searching {temp} on Google Sir....")
            webbrowser.open(f"https://www.google.com/search?q={temp}")
        if "search" in query:
            temp = query.replace("search", "")
            speak("Please Wait....")
            speak(f"Searching {temp} on Google Sir....")
            webbrowser.open(f"https://www.google.com/search?q={temp}")

    elif "inspirational quote" in query or "quote" in query:

        speak("\n\nShowing You a Random Inspirational Quote, Please Wait.....")
        response = requests.get("https://type.fit/api/quotes")

        randomnumber = random.randint(0, len(response.json()))
        quote = json.dumps(
            response.json()[randomnumber]["text"], sort_keys=True, indent=4)
        author = json.dumps(
            response.json()[randomnumber]["author"], sort_keys=True, indent=4)
        if author is None or author == "null":
            author = "Unknown"
        speak(f"\n\n\n{quote}\n\t\t\t\t\t\t\t\t\tBy {author}\n\n\n")

    else:
        speak("Sorry I Can't Do This....Please Try Something Else!!")
    time.sleep(3)
