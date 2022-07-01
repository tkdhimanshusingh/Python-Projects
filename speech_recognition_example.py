import speech_recognition as sr
import os
import time
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    input("PRESS ENTER KEY TO START")
    while True:
        query = takeCommand().lower()
        if "exit" in query:
            print("\n"*4+"Good Bye !!".center(85))
            time.sleep(1.5)
            exit()
