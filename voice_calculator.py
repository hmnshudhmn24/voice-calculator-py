import speech_recognition as sr
import pyttsx3
import re

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError:
            print("Could not request results, check your internet")
            return None

def evaluate_expression(expression):
    try:
        expression = re.sub(r'[^0-9+\-*/().]', '', expression)
        result = eval(expression)
        return result
    except Exception as e:
        print("Error in calculation:", e)
        return None

def main():
    speak("Welcome to Voice Calculator. Speak your calculation.")
    while True:
        print("Say a mathematical expression or 'exit' to quit.")
        command = recognize_speech()
        if command:
            command = command.lower()
            if "exit" in command:
                speak("Goodbye!")
                break
            result = evaluate_expression(command)
            if result is not None:
                print(f"Result: {result}")
                speak(f"The result is {result}")

if __name__ == "__main__":
    main()
