import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good Eveening")
    
    speak("Hi Shubh,How May I Help You")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening !!")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognising !!")
        query = r.recognize_google(audio, language='en-in')
        print("User Said:",query)
    except Exception as e:
        print("Say that again")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching!!")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
