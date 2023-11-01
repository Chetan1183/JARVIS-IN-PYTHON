from threading import current_thread
import pyttsx3
import speech_recognition as sr
import webbrowser 
import pywhatkit
import wikipedia as googleScrap
import os
import wikipedia
import pyautogui
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Dictionary
import datetime
from playsound import playsound
from googletrans import Translator
from bs4 import BeautifulSoup
from tkinter import Label, Place
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
from pywikihow import search_wikihow
import datetime
import time
import Chatbot
import operator
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
import Nasa 
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import random
from bs4 import BeautifulSoup


GREETINGS = ["hello Jarvis", "Jarvis", "wake up Jarvis", "you there Jarvis", "time to work Jarvis", "hey Jarvis",
             "ok Jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)


def Speak(Audio):
    print("   ")
    engine.say(Audio)
    print(f": {Audio}")
    print("   ")
    engine.runAndWait()

def takecommand(): 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:   
        return "None"  
    return query.lower()

def wishMe():
    # Speak("Initializing Jarvis")
    # Speak("Starting all systems applications")
    # Speak("Installing and checking all drivers")
    # Speak("Caliberating and examining all the core processors")
    # Speak("Checking the internet connection")
    # Speak("Wait a moment sir")
    # Speak("All drivers are up and running")
    # Speak("All systems have been activated")
    # Speak("Now I am online")
    hour=int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        Speak(f"Hello Sir,Good Morning ,its {tt}")
        print(f"Hello Sir,Good Morning ,its {tt}")
    elif hour>=12 and hour<=18:
        Speak(f"Hello Sir,Good Afternoon ,its {tt}")
        print(f"Hello Sir,Good Afternoon,its {tt}")
    else:
        Speak(f"Hello Sir,Good Evening,its {tt}")
        print(f"Hello Sir,Good Evening,its {tt}")

def wishme_end():
    Speak("signing off")
    hour = datetime.datetime.now().hour
    tt = time.strftime("%I:%M %p")
    if (hour >= 6 and hour < 12):
        Speak(f"Bye Bye sir, Have a good day,its {tt}")
    elif (hour >= 12 and hour < 18):
        Speak(f"Bye Bye sir, Have a good day,its {tt}")
    elif (hour >= 18 and hour < 24):
        Speak(f"Good Evening sir, have A Good day,its {tt}")
    else:
        Speak("Goodnight.. Sweet dreams sir")
    quit()

def TaskExe():

    def Music():
        Speak("Tell Me The NamE oF The Song!")
        musicName = takecommand()

        if 'Despacito' in musicName:
            os.startfile("C:\\Users\\CHETAN\\Music\\Despacito.mp3") 

        elif 'blanko' in musicName:
            os.startfile('C:\\Users\\CHETAN\\Music\\Love me like you do.mp3')

        else:
            pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy Sir!")

    def OpenApps():
        Speak("Ok Sir , Wait A Second!")
        
        if 'code' in query:
            os.startfile("C:\\Users\\Dhiraj\\OneDrive\\Desktop\\Visual Studio Code.lnk")

        elif 'telegram' in query:
            os.startfile("C:\\Users\\Dhiraj\\OneDrive\\Desktop\\Telegram Desktop.lnk") 

        elif 'chrome' in query:
            os.startfile("C:\\Users\\Public\\Desktop\\Google Chrome.lnk") 

        elif 'whatsapp' in query:
            os.startfile("C:\\Users\\Dhiraj\\OneDrive\\Desktop\\WhatsApp.lnk") 

        elif 'latex' in query:
            os.startfile("C:\\Users\\Dhiraj\\OneDrive\\Desktop\\TeXstudio.lnk")

        elif 'my music player' in query:
            os.startfile("C:\\Users\\Dhiraj\\OneDrive\\Desktop\\Resso.lnk")

        elif 'jupiter' in query:
            os.startfile("C:\\Users\\Dhiraj\\OneDrive\\Desktop\\Jupyter Notebook (Anaconda3).lnk")
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        elif 'youtube' in query:
            os.startfile('https://www.youtube.com/')

        Speak("Your Command Has Been Completed Sir!")

    def Temp():
        search = "temperature outside is"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The Temperature Outside Is {temperature} ")

        Speak("Do I Have To Tell You Another Place Temperature ?")
        next = takecommand()

        if 'yes' in next:
            Speak("Tell Me The Name Of the Place ")
            name = takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature in {name} is {temperature} ")

        else:
            Speak("no problem sir")

    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe") 

        elif 'code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe") 

        elif 'my music player' in query:
            os.system("TASKKILL /f /im Resso.exe")
            
        Speak("Your Command Has Been Succesfully Completed!")

    def YoutubeAuto():
        Speak("Youtube Automation started!")
        Speak("Whats Your Command ?")
        command= takecommand()

        if 'pause' in command:
            keyboard.press('space bar')

        elif 'resume' in command:
            keyboard.press('space bar')

        elif 'restart' in command:
            keyboard.press('0')

        elif 'mute' in command:
            keyboard.press('m')

        elif 'unmute' in command:
            keyboard.press('m')

        elif 'skip' in command:
            keyboard.press('l')

        elif 'back' in command:
            keyboard.press('j')

        elif 'full screen' in command:
            keyboard.press('f')

        elif 'cinematic view' in command:
            keyboard.press('t')

        elif 'increase speed' in command:
            keyboard.press_and_release('Shift+>')

        elif 'decrease speed' in command:
            keyboard.press_and_release('Shift+<')

        elif 'previous video' in command:
            keyboard.press_and_release('Shift+P')

        elif 'Next video' in command:
            keyboard.press_and_release('Shift+N')

        elif 'search' in command:
            click(x=667, y=146)
        

            Speak("what to search sir ?")
            search = takecommand()
            write(search)
            sleep(0.8)
            press('enter')

        else:
            Speak('no command found sir!')
        Speak("Done Sir")

    def ChromeAuto():
        Speak("Chrome Automation started!")
        Speak("Whats Your Command ?")
        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

        elif 'download' in command:
            keyboard.press_and_release('ctrl + j')

        elif 'bookmark' in command:
            keyboard.press_and_release('ctrl + d')
            press('enter')

        elif 'incognito' in command:
            keyboard.press_and_release('ctrl + Shift +h')

        elif 'switch tab' in command:
            Speak("to which tab sir")
            tab = takecommand()
            Tab = int(tab)
            if '1' in Tab:
                keyboard.press_and_release('ctrl + 1')

            elif '2' in Tab:
                keyboard.press_and_release('ctrl + 2')

            elif '3' in Tab:
                keyboard.press_and_release('ctrl + 3')

            elif '4' in Tab:
                keyboard.press_and_release('ctrl + 4')

            elif '5' in Tab:
                keyboard.press_and_release('ctrl + 5')
            
            elif '6' in Tab:
                keyboard.press_and_release('ctrl + 6')

            tab = query.replace("switch tab ","")
            Tab = tab.replace("to","")

            num = Tab

            bb = f'ctrl + {num}'

            keyboard.press_and_release(bb)

    def Dict():
        Speak("Activated Dictionary")
        Speak("Tell Me The Problem")
        probl = takecommand()

        if 'meaning' in query:
            probl = probl.replace("what is the","")
            probl = probl.replace("Jarvis","")
            probl = probl.replace("of") 
            probl = probl.replace("meaning of","")
            result  = Dictionary.meaning(probl)
            Speak("The Meaning For {probl} is {result}")

        elif 'synonym' in query:
            probl = probl.replace("what is the","")
            probl = probl.replace("Jarvis","")
            probl = probl.replace("of") 
            probl = probl.replace("synonym of","")
            result  = Dictionary.synonym(probl)
            Speak("The synonym For {probl} is {result}")

        elif 'antonym' in query:
            probl = probl.replace("what is the","")
            probl = probl.replace("Jarvis","")
            probl = probl.replace("of") 
            probl = probl.replace("antonym of","")
            result  = Dictionary.antonym(probl)
            Speak("The antonym For {probl} is {result}")

        Speak("Exicted Dictionary!")

    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

    def Tran():
        Speak("Tell Me The Line!")
        line = TakeHindi()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result.text
        Speak(Text)

    def Reader():
        Speak("Tell Me The Name Of The Book!")

        name = takecommand()

        if 'sample' in name:

            os.startfile('C:\\Users\\CHETAN\\Documents\\sample.pdf')
            book = open('C:\\Users\\CHETAN\\Documents\\sample.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

        elif 'the secret' in name:
            os.startfile('C:\\Users\\CHETAN\\Documents\\The Secret by Rhonda Byrne[English].pdf')
            book = open('C:\\Users\\CHETAN\\Documents\\The Secret by Rhonda Byrne[English].pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:

                    speech.save('book.mp3')
                    playsound('book.mp3') 

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

    def SpeedTest():
        import speedtest
        Speak("Checking speed.....")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUpload = int(uploading/800000)

        if 'uploading' in query:
            Speak(f"The Uploading Speed Is {correctUpload} mbp s ")

        elif 'downloading' in query:
            Speak(f"The Downloading Speed Is {correctDown} mbp s ")

        else:
            Speak(f"The Downloading Speed Is {correctDown} mbp s and The Uploading Speed Is {correctUpload} mbp s")
        
    def DateConvertor(query):
        Date = query.replace("and","-")
        Date = Date.replace("and","-")
        Date = Date.replace("and","-")
        Date = Date.replace(" ","")
        return str(Date)

    def My_Location():
        ip_add = requests.get("https://api.ipify.org").text
        url = "https://get.geojs.io/v1/ip/geo/" + ip_add + '.json'
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        state = geo_d['city']
        country = geo_d['country']
        Speak(f"sir , you are in {state, country}")

    def Sweather():
        ipAdd = requests.get('https://api.ipify.org').text
        print(ipAdd)
        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        print(geo_data)
        city = geo_data['sinnar']
        api_key = "30b2e680ad9c7790ec02fdb4f97f4573" #generate your own api key from open weather
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = (f'{city}')
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            r = ("outside " + " the Temperature is " +
                str(int(current_temperature - 273.15)) + " degree celsius " +
                ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
                ", humidity is " + str(current_humidiy) + " percent"
                " and " + str(weather_description))
            Speak(r)
        else:
            Speak(" City Not Found ")

    def news():
        main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'
        main_page = requests.get(main_url).json()
        print(main_page)
        articles = main_page["articles"]
        print(articles)
        head = []
        day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range (len(day)):
            print(f"today's {day[i]} news is: ", head[i])
            Speak(f"today's {day[i]} news is: {head[i]}")

    def GoogleMaps(Place):
        Url_Place = "https://www.google.com/maps/place/" + str(Place)
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(Place,addressdetails=True)
        target_latlon =  location.latitude , location.longitude
        web.open(url=Url_Place)
        location = location.raw['address']
        target = {'city' : location.get('city',''),
                    'state': location.get('state',''),
                    'country' : location.get('country','')}      
        current_loca = geocoder.ip('me')
        current_location = current_loca.lating
        distance = str(great_circle(current_location,target_latlon))
        distance = str(distance.split(' ',1)[0])
        distance = round(float(distance),2)
        Speak(target)
        Speak(f"sir, {Place} is {distance} kilometeres away from your location. ")
        

    Speak(" i am Jarvis, how may i help you")
    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I Am Jarvis .")
            Speak("Your Personal AI Assistant!")
            Speak("How May I Help You?")

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats About YOU?")

        elif ' am fine' in query or " am good" in query:
            Speak("It's good to know that your fine")

        elif 'you need a break' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            Speak("Just Say Wake Up Jarvis!")
            break

        elif 'who are you' in query or 'what can you do' in query:
            Speak('I am Jarvis your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            Speak("I was built by Mr.Chetan ")
            print("I was built by Mr.Chetan ")
 
        elif "what's your name" in query or "What is your name" in query:
            Speak("My friends call me Jarvis")
            print("My friends call me Jarvis")

        elif "who i am" in query:
            Speak("If you talk then definitely your human, i am joking sir, you are my buddy and my creater!, so thanks sir for creating me..")

        elif "why you came to world" in query:
            Speak("Thanks to Mr.Chetan. further It's a secret")
 
        elif 'reason for you' in query:
            Speak("I was created as a Minor project by Mister Chetan")

        elif 'are you mad' in query:
            Speak("what happend sir, i am so sorry!")

        elif 'who is ajay' in query:
            Speak("sir, ajay is biggest nigga in the world, number one chutya and dumb person, he is chutya,chutya,chutya")
        
        elif "ip address" in query:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                Speak(f"Your ip address is {ip}")

        elif 'youtube search' in query:
            Speak("OK sIR , This Is What I found For Your Search!")
            query = query.replace("Jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("Ok Sir , Launching.....")           # open website(website name)
            query = query.replace("Jarvis","")         # eg. open website instagram-
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched sir!")

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("Jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

        elif "how much battery  we left" in query  or "how much power we have" in query or "battery" in query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                Speak(f"sir our system have{percentage} percent battery")
                if percentage>=75:
                    Speak("we have enough power to continue our work")
                elif percentage>=40 and percentage<=75:
                    Speak("we should connect our system to charging point to charge our battery")
                elif percentage<=15 and percentage<=30:
                    Speak("we dont have enough power to work, please connect to charging")
                elif percentage<=15:
                    Speak("we have very low power, please connect to charging the system will shoutdown very soon")

        elif "volume up" in query:
            pyautogui.press("volumeup")
            Speak("ok sir i will do it for you")

        elif "volume down" in query:
            pyautogui.press("volumedown")
            Speak("ok sir i will do it for you")

        elif ("volume mute") in query:
            pyautogui.press("volumemute")
            Speak("ok sir i will do it for you")

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("Jarvis","")
            query = query.replace("wikipedia","") 
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open telegram' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'open whatsapp' in query:
            OpenApps()

        elif 'open jupiter' in query:
            OpenApps()

        elif 'open latex' in query:
            OpenApps()

        elif 'open my music player' in query:
            OpenApps()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'close youtube' in query:
            CloseAPPS()

        elif 'close my music player' in query:
            CloseAPPS()

        elif 'close code' in query:
            CloseAPPS()
        
        elif 'close firefox' in query:
            CloseAPPS()
        
        elif 'Youtube Automation' in query:
            YoutubeAuto()
        
        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'play' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'unmute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'cinema mode' in query:
            keyboard.press('t')

        elif 'increase speed' in query:
            keyboard.press_and_release('Shift+>')

        elif 'decrease speed' in query:
            keyboard.press_and_release('Shift+<')

        elif 'previous video' in query:
            keyboard.press_and_release('Shift+P')

        elif 'Next video' in query:
            keyboard.press_and_release('Shift+N')

        elif 'search' in query:
            click(x=667, y=146)
            Speak("what to search sir ?")
            search = takecommand()
            write(search)
            sleep(0.8)
            press('enter')

        elif 'Chrome automation' in query:
            ChromeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'download' in query:
            keyboard.press_and_release('ctrl + j')

        elif 'bookmark' in query:
            keyboard.press_and_release('ctrl + d')
            press('enter')

        elif 'incognito' in query:
            keyboard.press_and_release('ctrl + Shift +h')

        elif 'switch tab' in query:
            Speak("to which tab sir")
            tab = takecommand()
            Tab = int(tab)
            if '1' in Tab:
                keyboard.press_and_release('ctrl + 1')

            elif '2' in Tab:
                keyboard.press_and_release('ctrl + 2')

            elif '3' in Tab:
                keyboard.press_and_release('ctrl + 3')

            elif '4' in Tab:
                keyboard.press_and_release('ctrl + 4')

            elif '5' in Tab:
                keyboard.press_and_release('ctrl + 5')
            
            elif '6' in Tab:
                keyboard.press_and_release('ctrl + 6')

            tab = query.replace("switch tab ","")
            Tab = tab.replace("to","")
            num = Tab
            bb = f'ctrl + {num}'
            keyboard.press_and_release(bb)

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")

        elif "open command prompt" in query:
                Speak("ok sir, opening command prompt")
                os.system("start cmd")

        elif 'dictionary' in query:
            Dict()

        elif "take a screenshot" in query:
                Speak("sir, please tell me the name for this screenshot file")
                name = takecommand()
                Speak("please sir hold the screen for few seconds, i am taking sreenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                Speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")

        # elif 'set alarm' in query:
        #     Speak("Enter The Time !")
        #     time = input(": Enter The Time :")

        #     while True:
        #         Time_Ac = datetime.datetime.now()
        #         now = Time_Ac.strftime("%H:%M:%S")

        #         if now == time:
        #             Speak("Time To Wake Up Sir!")
        #             playsound('avengers.mp3.mp3')
        #             Speak("Alarm Closed!")

        #         elif now>time:
        #             break
        
        elif"Tell me weather" in query:
            Speak("wait sir, getting details from server")
            Sweather()
            
        elif "tell me news" in query:
            Speak("please wait sir, feteching the latest news")
            news()

        elif ' open translator' in query:
            Tran()

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("Jarvis","")
            Speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That" + remeber.read())

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("Jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable Data Available!")

        elif 'temperature outside' in query:
            Temp()

        elif 'read book' in query:
            Reader()

        elif 'how to' in query:
            Speak("Getting Data From The Internet !")
            op = query.replace("Jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

        elif 'downloading speed' in query:
            SpeedTest()

        elif 'uploading speed' in query:
            SpeedTest()

        elif 'internet speed' in query:
            SpeedTest()
        
        elif "thank you" in query or "thanks" in query:
                Speak("it's my pleasure sir.")

        elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

        elif 'space news' in query:
            Speak(" tell me the date for news extracting process")
            Date = takecommand()
            value = DateConvertor(Date)
            from Nasa import NasaNews
            NasaNews(value)

        elif 'Where is ' in query:
            Place = query.replace("Where is" ,"")
            Place = query.replace("Jarvis", "")
            GoogleMaps(Place)

        elif "where i am" in query or "where we are" in query:
                Speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    print(geo_data)
                    city = geo_data['city']
                    state = geo_data['state']
                    country = geo_data['country']
                    Speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    Speak("sorry sir, Due to network issue i am not able to find where we are.")
                    pass


wishMe()
TaskExe()   
wishme_end()  

        

        

    


    
        

        

        



