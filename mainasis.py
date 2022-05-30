import pyjokes  # pentru niste glume mai putin amuzante
import speech_recognition as sr  # pentru speech to text
import pyttsx3  # pentru text to speech
import datetime  # pentru welcomer
from datetime import date
from tkinter import *  # tk requierements
import random  # pt random choices
import pyautogui  # pt screenshot si ce mai foloseste pyautogui
import time  # pt timesleep
import webbrowser  # youtube, google, etc.
import requests  # pt locatii
import subprocess  # pt a deschide file-uri
from PIL import Image

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

        return "None"


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

            if 'youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("Opening youtube")
                time.sleep(1)

            if 'gmail' in statement:
                webbrowser.open_new_tab("https://mail.google.com/mail/u/1/#inbox")
                speak("Opening gmail")
                time.sleep(1)

            if 'flip a coin' in statement:
                moves = ["Head", "Tails", "Flip your own, I don't feel like helping you today."]
                cmove = random.choice(moves)
                speak(cmove)

            if 'screenshot' in statement:
                my_screenshot = pyautogui.screenshot()
                my_screenshot.save('D:/screenshot/screenshot.png')
                speak("Screen captured")

            if 'joke' in statement:
                speak(pyjokes.get_joke())

            if 'what city' in statement:
                ip_info = requests.get('https://api.ipdata.co?api-key=d1a649ed39dd19a27105e14ba9ab5'
                                       '3d177d8ca6f639db6d94741eda7').json()
                loc = ip_info['region']
                speak(f"You must be somewhere in {loc}")

            if 'exact location' in statement:
                url = "https://www.google.com/maps/search/Where+am+I+?/"
                webbrowser.get().open(url)
                speak("You must be somewhere near here, as per Google maps")

            if 'weather' in statement:
                url = "https://bit.ly/3LTeooM"
                webbrowser.get().open(url)
                speak("This is the weather at your current location")

            if 'time' in statement:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strtime}")

            if 'date' in statement:
                today = date.today()
                d = today.strftime("%B %d, %Y")
                speak(f"Today is {d}")

            if 'schedule' in statement:
                im = Image.open(r"C:\Users\alex\Documents\schedule.jpg")
                im.show()
                speak('Pretty busy schedule today... is it?')

            if 'open notes' in statement:
                subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
                speak('Opening notes')

            if 'news' in statement:
                webbrowser.open_new_tab("https://www.romaniatv.net/")
                speak('Here are some of the headlines today')
                time.sleep(1)

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

    speak_button = Button(text='SPEAK', command=audioprocess)
    speak_button.pack(pady=10)
    exit_button = Button(text='EXIT', command=stopapp)
    exit_button.pack()

    screen.mainloop()


main_screen()
