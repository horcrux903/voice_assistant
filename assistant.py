import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import random
import pyaudio
import time
import smtplib
import os
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):                            #speak function string to audio 
    engine.say(audio)
    engine.runAndWait()

def wishme():                                  #greeting function
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning sir")
    elif hour<18 and hour >=12:
        speak("good afternoon sir")
    else:
        speak("good evening")     
    speak("I am Jarvis sir how can i help you sir")
    
def take_command():                         #converting audio in string
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    
    except Exception as e:
        print("Repeat your command")
        return "none"
    
    return query


if __name__ == "__main__":

    wishme()

    while True:

        query = take_command().lower()

        if 'youtube' in query:
            speak('opening youtube')
            webbrowser.open_new("http://www.youtube.com")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            try:
                p = wikipedia.page(query)
            except wikipedia.DisambiguationError as e:
                s = random.choice(e.options)
                p = wikipedia.page(s)

            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'google' in query:
            speak('opening google')
            webbrowser.open_new("http://www.google.com")

        elif 'play music' in query:
            music_dir = '/Users/rajatsharma/Desktop/music'
            song = os.listdir(music_dir)
            print(song[0])
            os.startfile(os.path.join(music_dir))

        elif 'time' in query:
            str = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str}")

        elif 'thank you' in query:
            speak('welcome sir')

        elif 'quit' in query:
            speak('ok sir')
            exit()

            
    
 



