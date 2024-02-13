hi
import pyttsx3
import speech_recognition as sr
import pywhatkit
import requests
from bs4 import BeautifulSoup
import random
import datetime
import pyautogui
import webbrowser
import time
from openai import OpenAI
from wiz import start_wiz

client = OpenAI()

import os


username = ""
def start_guide():
    global username
    while True:
        user_input = input("HELLO, DO YOU WANT TO USE VOICE OR CHAT BASED CHATBOT?\n")

        if "voice" in user_input.casefold():
            run_jarvis()
            break  # Exit the loop if the user selects voice
        elif "chat" in user_input.casefold():
            start_wiz()
            break  # Exit the loop if the user selects chat
        else:
            print("Please write 'voice' or 'chat' to start.")

def generate_chat_response(prompt):
    response = client.completions.create(
        model="gpt-3.5-turbo-1106",
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        stop=["space"]
    )
    return response.choices[0].text.strip()


list1 = ["fine", "great", "good", "amazing", "awesome", "good.", "Good", "Fine", "Amazing"]
exitgreet = ["bye", "bie", "goodbye", "see you", "see yaa", "byee"]
greet = ["hey", "hello", "hii", "heyaa"]

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

listening_status = False
stop_listening = False


def greeting():
    current_hour = int(time.strftime('%H'))
    if 5 <= current_hour < 12:
        talk("Good morning! How can I assist you?")
    elif 12 <= current_hour < 18:
        talk("Good afternoon! How can I assist you?")
    else:
        talk("Good evening! How can I assist you?")


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=10)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except:
        return ""


def get_news_headlines():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')

    unwanted = ['BBC World News TV', 'BBC World Service Radio',
                'News daily newsletter', 'Mobile app', 'Get in touch', 'BBC News Channel',
                'BBC Radio 5 Live']

    news_list = [x.text.strip() for x in headlines if x.text.strip() not in unwanted]

    return news_list[:5]


def get_weather_info(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": city, "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com",
        "X-RapidAPI-Key": "9fd654d284msh3607ec1ec8113fap1aa355jsnd430c9cd2f34"
    }

    response = requests.get(url, headers=headers, params=querystring)
    weather_data = response.json()

    if "location" in weather_data:
        current_condition = weather_data["current_observation"]["condition"]["text"]
        temperature = weather_data["current_observation"]["condition"]["temperature"]
        talk(f"The weather in {city} is {current_condition} with a temperature of {temperature} degrees Fahrenheit.")
    else:
        talk(f"Sorry, I couldn't retrieve the weather information for {city} at the moment.")


def run_jarvis():
    global username
    greeting()

    while True:
        command = listen_command().lower()  # Convert the command to lowercase for case-insensitivity
        if "how are you" in command:
            response = random.choice(list1)
            talk(f"I'm doing {response}, thank you for asking!")
        elif any(word in command for word in greet):
            talk("Hello, How are you?")
        elif any(word in command for word in exitgreet):
            talk("Bye, have a good day")
            exit()
        elif "play" in command:
            search_query = command.replace("play", "").strip()
            talk("Playing " + search_query)
            pywhatkit.playonyt(search_query)
        elif "news" in command:
            news_headlines = get_news_headlines()
            for i, headline in enumerate(news_headlines, 1):
                talk(f"Headline {i}: {headline}")
                stop_command = listen_command().lower()
                if "stop" in stop_command or "enough" in stop_command:
                    talk("Stopping current action. How can I assist you now?")
                    return
            print("TYPE (BACK) TO GO BACK TO MAIN PAGE")
        elif "weather of" in command:
            city_start = command.find("weather of") + len("weather of")
            input_of = command[city_start:].strip()
            get_weather_info(input_of)
            print("(TYPE BACK) TO GO BACK TO MAIN PAGE")
        elif "current time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            talk(f"The current time is {current_time}")
        elif "current date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            talk(f"Today's date is {current_date}")
        elif "current day" in command:
            current_day = datetime.datetime.now().strftime("%A")
            talk(f"Today is {current_day}")
        elif "open" in command:
            # Extract the application name after "open"
            app_name = command.split("open", 1)[1].strip()
            pyautogui.hotkey('win', 'r')  # Open Run dialog
            pyautogui.write(f"{app_name}.exe")
            pyautogui.press('enter')
            talk(f"Opening {app_name.capitalize()}")
        elif "search" in command:
            # Extract the search query after "search"
            search_query = command.replace("search", "").strip()
            talk(f"Searching for {search_query} on the web.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        elif "close" in command:
            # Extract the application name after "close"
            app_name = command.replace("close", "").strip()
            pyautogui.hotkey('alt', 'f4')  # Simulate Alt + F4 to close the active window
            talk(f"Closing {app_name.capitalize()}")
        elif "who is" in command:
            # Extract the name after "who is"
            person_name = command.replace("who is", "").strip()
            talk(f"Searching Wikipedia for {person_name}.")
            webbrowser.open(f"https://en.wikipedia.org/wiki/{person_name.replace(' ', '_')}")
        elif "remember that" in command:
            remembermessage = command.replace('remember that', '')
            talk("Done I have remembered that " + remembermessage)
            remember = open('remember.txt', "a")
            remember.write(remembermessage)
            remember.close()
        elif "what do you remember" in command:
            remember = open('remember.txt', "r")
            remembered_data = remember.read()
            if remembered_data:
                talk("You told me to remember the following:\n" + remembered_data)
            else:
                talk("I don't have any specific information remembered.")
            remember.close()
        elif "forget my list" in command:
            open('remember.txt', 'w').close()
            talk("I have forgotten everything.")
        elif "your name" in command:
            talk("MY name is Jarvis and i am at your service")
        elif "my name is" in command:
            username = command.replace('my name is', '')
            talk("Thanks for telling me your name")
        elif "what is my name" in command:
            if username:
                talk("As of my knowledge , your name is " + username)
            else:
                talk("you havent told me your name")
        elif "ok" in command:
            talk("Anything else ?")
            useri = listen_command().lower()
            if "no" in  useri:
                talk("BYE , HAVE A NICE DAY ")
                exit()
        else:
            talk("i dont understand")


if __name__ == '__main__':
    start_guide()