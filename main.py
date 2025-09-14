import speech_recognition as sr
import webbrowser
import pyttsx3

recognition=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        speak("I'm listening")
        audio = recognition.listen(source)
        try:
            query = recognition.recognize_google(audio)
            print(f"You said: {query}")
            speak(f"You said {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            speak("Sorry, there was a problem with the speech recognition service.")
            return ""
    
if __name__ == '__main__':
    speak("Initializing jarivis.....")
    command = listen()
   
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif command:
        speak("Command not recognized.")
   

    
