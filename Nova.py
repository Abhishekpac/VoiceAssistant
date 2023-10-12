import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, Sir!")
    else:
        speak("Good Evening, Sir!")
    
    speak("I am Nova. Tell me how may I help you")

def takeComamnd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Sorry I did't recognize, Say that again please...")
        return "None"
    return query

    
if __name__=="__main__":
    wishMe()
    while True:
        if 1:
            query = takeComamnd().lower()
        
            if 'wikipedia' in query:   #Executig task based on query 
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:   
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open notepad' in query:
                subprocess.Popen(['notepad.exe'])

            elif 'Thank you' in query:
                speak("Pleasure to help")

            elif 'quit' in query:      #Quit the program
                speak("Goodbye, Sir!")
                exit()