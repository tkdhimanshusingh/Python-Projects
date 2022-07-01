import pyttsx3
import speech_recognition as sr
import os
import pyfirmata
import time
board=pyfirmata.Arduino("COM8")
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
        query=set(query)
        if 'on' in query:
            if 'lamp' in query:
                board.digital[12].write(1)
            if 'fan' in query:
                board.digital[11].write(1)
            if 'bulb' in query:
                board.digital[10].write(1)
            if 'night' in query:
                board.digital[9].write(1)
            board.digital[2].write(1)
        elif 'off' in query:
            if 'lamp' in query:
                board.digital[12].write(0)
            if 'fan' in query:
                board.digital[11].write(0)
            if 'bulb' in query:
                board.digital[10].write(0)
            if 'night' in query:
                board.digital[9].write(0)
            board.digital[2].write(0)
        elif 'exit' in query:
            board.digital[9].write(0)
            board.digital[10].write(0)
            board.digital[11].write(0)
            board.digital[12].write(0)
            board.digital[2].write(2)
            exit()
