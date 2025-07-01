import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import musicLibrary
import requests
# c544ddd8a50246c882c9ad1e66c48b0b
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def process_command(c):
    
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open linkdin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    


if __name__=="__main__":
    speak("Initializing Dora")
    #Listen for the wake word for Dora
    while True:
        r = sr.Recognizer()
        # recognize speech using Sphinx
        try:
            print("Recognizing....")
            with sr.Microphone() as source:
                print("Listening,,,")
                audio = r.listen(source,timeout=3,phrase_time_limit=2)
            word=r.recognize_google(audio)
            print(word)

            if(word.lower()=="dora"):
                speak("Yes Altaf")
                with sr.Microphone() as source:
                    print("Dora Active...")
                    audio = r.listen(source,timeout=3,phrase_time_limit=2)
                command=r.recognize_google(audio)

                if any(word in command.lower() for word in ["goodbye", "bye", "see you", "exit", "quit", "stop"]):
                    speak("Okay Altaf, talk to you later. Bye!")
                    break

                process_command(command)
     
        except Exception as e:
            print("Try again",e)
