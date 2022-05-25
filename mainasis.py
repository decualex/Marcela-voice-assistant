import speech_recognition as sr  # pentru speech to text
import pyttsx3  # pentru text to speech
import datetime  # pentru welcomer
from tkinter import *  # tk requierements

name_assistant = 'Marcela'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
global screen


def speak(text):
    engine.say(text)
    print(name_assistant + " : " + text)
    engine.runAndWait()


def welcomer():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:

        speak(f"Top of the morning to you! My name is {name_assistant}")

    elif 12 <= hour < 18:

        speak(f"Happy dupa-amiaza amigo. My name is {name_assistant}")

    else:
        speak(f"Buna seara, colega! My name is {name_assistant}")


def get_audio():
    r = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:

        print("Listening")
        audio = r.listen(source, phrase_time_limit=3)
        print("Stop.")

    try:
        text = r.recognize_google(audio, language='en-US')
        print('You: ' + ': ' + text)
        return text

    except:

        return "cgfhcfgh"


def audioprocess():
    run = 1
    if __name__ == '__main__':
        while run == 1:

            statement = get_audio().lower()
            results = ''
            run += 1

            if "hello" in statement or "hi" in statement:
                welcomer()

            if "exit" in statement or "stop" in statement:
                speak('I am shutting down')
                screen.destroy()
                break

            speak(results)


def stopapp():
    screen.destroy()


def main_screen():
    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("300x110")
    screen.iconbitmap('icon.ico')

    name_label = Label(text=name_assistant, width=300, bg="black", fg="white", font=("Calibri", 13))
    name_label.pack()

    microphone_button = Button(text='SPEAK', command=audioprocess)
    microphone_button.pack(pady=10)
    exit_button = Button(text='EXIT', command=stopapp)
    exit_button.pack()

    screen.mainloop()


main_screen()
