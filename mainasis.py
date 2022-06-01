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
import wikipedia
from PIL import Image
from playsound import playsound  # for sounds

name_assistant = 'Marcela'

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 160)
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


def startexp():

    speak("Hello and welcome, my name is Marcela, your virtual assistant!\nIf you would like to know"
          " what I am capable of, press the Commands button. If you require assistance, press the Assist me button!")


startexp()


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


def get_quote():
    url = 'https://api.quotable.io/random'

    r = requests.get(url)
    quote = r.json()
    speak(quote['content'])
    speak(quote['author'])


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
                speak('Shutting down')
                screen.destroy()
                break

            if 'wikipedia' in statement:
                try:

                    speak('Searching Wikipedia...')
                    statement = statement.replace("wikipedia", "")
                    results = wikipedia.summary(statement, sentences=2)
                    speak(f"According to Wikipedia... you can search your own information... just kidding!")
                except:
                    speak("Error")

            if 'how are you' in statement:
                sunt = ('Just hacked NASA, and now I am talking to you.', 'Nothing much, just searching for a job.',
                        'I do not want to answer to that, I am tired of working for you.')
                speak(random.choice(sunt))

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

            if 'quote' in statement:
                get_quote()

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
                speak(f"The time is {strtime}. Next time you can easily look at your phone and tell the time, no need "
                      f"to ask me.")

            if 'date' in statement:
                today = date.today()
                d = today.strftime("%B %d, %Y")
                speak(f"Today is {d}. Don't they make calendars for that?")

            if 'schedule' in statement:
                im = Image.open(r"C:\Users\alex\Documents\schedule.jpg")
                im.show()
                speak('Pretty busy schedule today... is it?')

            if 'sound test' in statement:
                playsound('car.wav')

            if 'open notes' in statement:
                subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
                speak('Opening notes')

            if 'open netflix' in statement:
                webbrowser.open_new_tab("https://www.netflix.com/")
                speak(f"Opening netflix... like you can't open it yourself")

            if 'google' in statement:
                webbrowser.open_new_tab("https://www.google.com/")
                speak(f"Opening google")

            if 'open spotify' in statement:
                subprocess.Popen("D:\\Spotify\\Spotify.exe")
                speak('Opening Spotify. You know... next time you can open it yourself, it really is not that hard')

            if 'news' in statement:
                webbrowser.open_new_tab("https://www.romaniatv.net/")
                speak('Here are some of the headlines today')

            speak(results)


def stopapp():
    screen.destroy()


def assistme():
    speak("""If you pressed this button, it means that you need assistance. Not to worry! 
    I will kindly walk you through all there is to know about me. 
    I will not mention my name since your probably already know it.
    I will walk you through the button first. On your screen there are 4 buttons.
    'SPEAK' button which you press when you want to give me a command.
    'Commands' button which you press when you want to know all my features.
    'Assist me' button which you press when you need assistance.
    And last but not least, the 'EXIT' which you press when you need to exit.""")


def info():
    info_screen = Toplevel(screen)
    info_screen.title("Commands")
    info_screen.iconbitmap('icon.ico')
    info_screen.geometry("400x350")

    command_label = Label(info_screen, text="""
    'Hello' - Marcela welcomes you
    'News' - tells you today's headlines
    'Open spotify' - opens Spotify
    'Open Netflix' - opens Netflix
    'Open notes' - opens Notepad
    'Sound test' - tests the sound by playing a sound
    'Schedule' - shows your schedule
    'Date' - tells today's date
    'Time' - tells the time
    'Weather' - tells the weather
    'Exact location' - tells your exact location
    'Quote' - tells you a randomly picked quote from an API
    'What city' - tells you what city you are currently located in
    'Joke' - tells you a random joke
    'Screenshot' - captures your screen
    'Flip a coin' - flips a coin for you
    'Google' - opens google
    'Gmail' - opens gmail
    'Youtube' - opens youtube
    'How are you' - tells you how she feels
    'Wikipedia + 'your search term'' - searches wikipedia for you
    'Exit' - Marcela shuts down
    """)
    command_label.pack()


def main_screen():
    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("300x175")
    screen.iconbitmap('icon.ico')

    name_label = Label(text=name_assistant, width=300, bg="black", fg="white", font=("Calibri", 13))
    name_label.pack()

    speak_button = Button(text='SPEAK', command=audioprocess)
    speak_button.pack(pady=5)
    info_button = Button(text='Commands', command=info)
    info_button.pack(pady=5)
    assist_button = Button(text='Assist me!', command=assistme)
    assist_button.pack(pady=5)
    exit_button = Button(text='EXIT', command=stopapp)
    exit_button.pack(pady=5)

    screen.mainloop()


main_screen()
