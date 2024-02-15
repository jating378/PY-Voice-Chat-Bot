import sys
import os
import time
import random
import requests
from bs4 import BeautifulSoup
import datetime
import string
from random import *
import re
import nltk
from nltk.corpus import wordnet
import webbrowser
import randfacts
from matplotlib import pyplot as plt, animation

list1 = [ "fine","great","good","amazing","i'm good","i am good","i am great","i am fine","i'm fine","and","awesome","good.","Good","Fine","Amazing"]
list2 = ["bye","bie","goodbye","see you","see yaa","byee"]
list3 = ["hey","hello","hi","heyaa"]

def start_wiz():

    #THEN I STARTED TO TAKE USERINPUT BY ASKING GENERAL QUESTIONS

    name = input("WIZ - Hello , what is your name? ")
    time.sleep(1)
    print("WIZ - HELLO " + name + ", MY NAME IS WIZ AND I AM HERE TO HELP YOU !!")
    use = input("WIZ - HOW ARE YOU?? ")



    if use.casefold() in list1:
        print("WIZ - NICE!! , HOW CAN I HELP YOU? ")
    else:
        print("WIZ - SORRY TO HEAR THAT , HOW CAN I HELP YOU?")

    print("IF YOU WANT TO KNOW WHAT I CAN DO JUST (TYPE HELP)")

    #I USED WHILE LOOP WITH OS LIBRARY SO THAT AFTER EVERY RESPONSE THERE IS CLEAR SCREEN
    #THEN I USED BASIC IF ELSE STATEMENTS TO CODE MY CHATBOT FUNCTIONS

    while True:
        userinput = input(name + "- ")
        os.system("cls")
        if "help" in userinput.lower().split():
            print("WIZ - I CAN TELL YOU WEATHER OF ANY CITY IN WORLD(TYPE WEATHER) \n I CAN TELL YOU LATEST NEWS (TYPE NEWS) \n I CAN SPLIT WORDS FOR SENTENCES TO TRY THIS (TYPE SPLIT) \n I CAN COUNTDOWN FOR YOU (TYPE COUNTDOWN) \n I CAN TELL YOU FAMOUS TOURIST ATTRACTIONS TO VISIT IN SOME POPULAR CITIES OF UNITED KINDOM (TYPE PLAN) \n I CAN CONVERT ANY TEXT INTO ANIMATED TEXT (TYPE ANIMATE) \n I CAN GENERATE RANDOM PASSWORDS (TYPE PASS) \n I CAN TELL YOU A RANDOM FACT (TYPE FACT)")
        elif "plan" in userinput.lower().split():
            print("WIZ - TYPE A NAME OF ANY MAIN CITY IN UNITED KINGDOM TO GET BEST TOURIST ATTRACTIONS THAT CITY")
            print("YOU CAN TYPE ANY OF THE CITIES NAMES \n COVENTRY,BIRMINGHAM,LONDON,EDINBURGH,GLASGOW,DUBLIN,BRISTOL,NEWCASTLE UPON TYNE,LEEDS,MANCHESTER,LIVERPOOL")
            print("TYPE (BACK) TO GO BACK TO MAIN PAGE")

            user_input = input("Enter a city name: ")

            city_headlines = get_city_headlines(user_input)
            if city_headlines:
                for idx, headline in enumerate(city_headlines):
                    print(f" {headline}")
            else:
                print("City not found.")


        #I USED CASEFOLD FUNCTION SO THAT EVEN IF USER WRITES THE INPUT IN ANY CASE ,BOT RECOGNIZES THE WORD
        #I USED REQUESTS AND BBEAUTIFULSOUP WHICH WAS VERY HELPFUL TO ME TO SCRAPE TOP TOURIST ATTRACTIONS OF MAIN CITIES OF UK
        #ALL OF THE DATA IS TAKEN FROM (https://www.planetware.com/)



    #IN THE CASE OF NEWS ALMOST SAME CODE IS USED AND SPILT FUNCTION IS USED
    #ALL THE DATA IS TAKEN FROM BBC.COM/NEWS

        elif "news" in userinput.lower().split() :
            news_headlines = news()
            for idx, headline in enumerate(news_headlines, start=1):
                print(f"{idx}. {headline}")
            print("TYPE (BACK) TO GO BACK TO MAIN PAGE")

    #FOR WEATHER I TRIED TO USED API . IT IS A FREE API PROVIDED BY YAHOO AND I GOT TO KNOW ABOUT THIS FROM (RAPIDAPI.COM)

        elif "weather" in userinput.lower().split():
            inputof = input("WIZ - TYPE THE NAME OF CITY TO SHOW ITS WEATHER")
            show_weather_info(inputof)

            print( "(TYPE BACK ) TO GO BACK TO MAIN PAGE")
    #BASIC SPILIT COMMAND USED TO HELP SOMEONE SPLIT THEIR WORDS FROM PARAGRAPH OR LINE.
        elif "split" in userinput.lower().split():
            input4 = input("WIZ - WRITE YOUR SENTENCE OR PARAGRAPH AND I WILL SPLIT WORDS FROM IT")
            words = input4.split()
            print(words)
            print(" (TYPE BACK ) TO GO BACK TO MAIN PAGE")
    #I USED FOR LOOP FOR COUNTDOWN SO USER CAN GET COUNTDOWN FOR ANY SECONDS
        elif "countdown" in userinput.lower().split():
            input5 = int(input("how many seconds timer you want?"))
            for i in range(input5):
                print(str(input5 - i) + "seconds remaining")
                time.sleep(1)
            print("WIZ - TIME IS UP")
            print(" (TYPE BACK ) TO GO BACK TO MAIN PAGE")

    # USED CONTINUE HERE SO THAT IF USER WANTS TO GO TO BACK PAGE
        elif "back" in userinput.lower().casefold():
            print("WIZ - IF YOU WANT TO KNOW WHAT I CAN DO JUST (TYPE HELP)")
            continue
    #IF NAME IS IN USER INPUT IT WILL GIVE RESPONSE BY TELLING ITS NAME

    #I REALLY WANTED TO ADD ONN MANY THINGS TO THE GREETING PART AND I ALSO SAW MANY TUTORIALS BUT DUE TO POOR CODING KNOWLEDGE IT WAS DIFFICULT
        elif "name" in userinput.lower().split(" "):
            print("WIZ - MY NAME IS WIZ AND I AM HERE TO HELP.")


    #USED MATPLOTLIB AND PYPLOT WHICH I LEARNED FROM 4005CEM DATA VISUALISATION IN PYTHON WHICH HELPED ME TO PERFORM THIS CODE
    #I GOT TO KNOW ABOUT THIS CODE FROM https://www.tutorialspoint.com/plot-animated-text-on-the-plot-in-matplotlib
        elif "animate" in userinput.lower().split():

            user_input = input("Enter the text that you want to convert to animated text: ")
            animate_text(user_input)
            print("Type (BACK) to go back to the main page.")

    # I USED DATETIME PACKAGE SO THAT IF USER WANTS TO KNOW DATE AND TIME
        elif "date" in userinput.lower().split():
            now = datetime.datetime.now()
            print ("Current date and time:")
            print("WIZ - " +now.strftime("%y-%m-%d %H:%M:%S"))
    #USED BOOLEAN SO THAT IF HOW AND YOU IS IN USER INPUT AT SAME TIME IT SHOULD REPLY
        elif "how" and "you" in userinput.lower().split():
            print("WIZ - I AM GOOD AND THANKS FOR ASKING")
    #USED STRING AND RANDOM PACKAGE TO DO A CODE THAT CAN GIVE YOU RANDOM PASS WORD
        elif "pass" in userinput.lower().split():

            characters = string.ascii_letters + string.punctuation + string.digits
            password = "".join(choice(characters) for x in range(randint(8,16)))
            print("WIZ - " + password)

    #BASIC RESPONSES TO USER INPUT DONE WITH THE HELP OF IF ELSE STATEMENT AND USED BREAK SO WHEN USER TYPES BREAK THE PROCESS ENDS
        elif userinput.casefold() in list2 :
            print("WIZ - BYEE!, TAKE CARE \n ")
            break
        elif userinput.lower() in list3:
            print("WIZ - HELLO!")
        elif "fact" in userinput.lower().split():
            print("WIZ - "+randfacts.get_fact())


    #IF USER INPUTS SOMEETHING THAT BOT DOESNT UNDERSTAND IT WILL REPLY BY SORRY I CANT UNDERSTAND
        else:
            print("WIZ - I AM SORRY , I CAN'T UNDERSTAND WHAT YOU ARE TRYING TO SAY \n PLEASE SEE THE INSTRUCTIONS ABOVE \n  (TYPE BACK ) TO GO BACK TO MAIN PAGE ")



def news():
    url = 'https://www.bbc.com/news'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h3')
    unwanted = ['BBC World News TV', 'BBC World Service Radio',
                'News daily newsletter', 'Mobile app', 'Get in touch', 'BBC News Channel',
                'BBC Radio 5 Live']

    newsheadlines = [x.text.strip() for x in headlines if x.text.strip() not in unwanted]

    return newsheadlines

def get_city_headlines(city_name):
    city_name_lower = city_name.casefold()

    city_urls = {
        "coventry": 'https://www.planetware.com/england/top-rated-things-to-do-in-coventry-eng-1-47.htm',
        "birmingham": 'https://www.planetware.com/tourist-attractions-/birmingham-eng-wm-brum.htm',
        "london": 'https://www.planetware.com/tourist-attractions-/london-eng-l-lon.htm',
        "manchester": 'https://www.planetware.com/tourist-attractions-/manchester-eng-m-man.htm',
        "leeds": 'https://www.planetware.com/tourist-attractions-/leeds-eng-wy-lee.htm',
        "liverpool": 'https://www.planetware.com/tourist-attractions-/liverpool-eng-mrs-liv.htm',
        "glasgow": 'https://www.planetware.com/tourist-attractions-/glasgow-sco-stra-glas.htm',
        "edinburgh": 'https://www.planetware.com/tourist-attractions-/edinburgh-things-to-do-sco-loth-edin.htm',
        "dublin": 'https://www.planetware.com/tourist-attractions-/dublin-irl-db-dub.htm',
        "bristol": 'https://www.planetware.com/tourist-attractions-/bristol-eng-av-bristol.htm',
        "newcastle upon tyne": 'https://www.planetware.com/tourist-attractions-/newcastle-upon-tyne-eng-tw-nut.htm'
    }

    if city_name_lower not in city_urls:
        return []  # Return an empty list for unknown city names

    url = city_urls[city_name_lower]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2')

    unwanted = ['More on England']

    travel_headlines = [x.text.strip() for x in list(dict.fromkeys(headlines)) if x.text.strip() not in unwanted]

    return travel_headlines



def get_weather(city_name):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"
    headers = {
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com",
        "X-RapidAPI-Key": "9fd654d284msh3607ec1ec8113fap1aa355jsnd430c9cd2f34"
    }

    querystring = {"location": city_name, "format": "json", "u": "f"}

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def show_weather_info(city_name):
    weather_data = get_weather(city_name)

    if weather_data:
        # Parse and display relevant weather information
        temperature = weather_data.get('current_observation', {}).get('condition', {}).get('temperature')
        condition = weather_data.get('current_observation', {}).get('condition', {}).get('text')
        print(f"Weather in {city_name}: {temperature}°F, {condition}")
    else:
        print("Failed to fetch weather information.")

def animate_text(user_input):
    plt.rcParams["figure.figsize"] = [8, 4]
    plt.rcParams["figure.autolayout"] = True
    fig, ax = plt.subplots()
    ax.set(xlim=(-1, 1), ylim=(-1, 1))
    label = ax.text(0, 0, user_input[0], ha='center', va='center', fontsize=20, color="Red")

    def animate(i):
        label.set_text(user_input[:i + 1])

    anim = animation.FuncAnimation(
        fig, animate, interval=200, frames=len(user_input))
    ax.axis('off')
    plt.show()