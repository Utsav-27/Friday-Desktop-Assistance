import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random


address = {
    "utsav":"11th floor, high rise buildings, California",
    "hiral":"21 Louis street, Canada",
    "shubh": "Duckland street, Australia"
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    engine.setProperty('rate', 200)
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good Evening")

    speak("I am Friday! Your New Assistant, How can i help you?")


def takeCommand():
    # takes microphone input from the users and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
       # r.pause_threshold = 1  # user can take 1s break so it does not quit listening
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mail@gmail.com', '')
    server.sendmail('', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
   # while(True):
    if 1:
        query = takeCommand().lower()

        # executing tasks based on query
        if 'wikipedia' in query:
            speak("Looking")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'github' in query:
            webbrowser.open('github.com/Utsav-27')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\panch\\OneDrive\\Desktop\\Utsav\\Music'
            songs = os.listdir(music_dir)
            ran = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[ran]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")

        elif 'sublime' in query:
            path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(path)

        elif 'email to utsav' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "crazybanda793@gmail.com"
                speak("Sending Email")
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, couldn't complete request")

        elif 'address' in query:
            speak("Who's address do you want sir")
            add = takeCommand().lower()
            if add in address.keys():
                print(address[add])
                speak(address[add])
            else:
                speak("There is no such person in record, Do you want to add this person?")
                add_addr = takeCommand().lower()
                if add_addr == 'yes' or add_addr == 'ok':
                    speak("Tell the name of the person")
                    name = takeCommand().lower()
                    speak(f"Tell the address of {name}")
                    name_addr = takeCommand().lower()
                    address[name] = name_addr
                    speak(f"{name} added in record")
                else:
                    speak("ok")
                    exit()

        elif 'exit' in query:
            exit()


        
