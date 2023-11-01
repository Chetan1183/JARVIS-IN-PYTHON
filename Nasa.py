from os import name, path
import requests
import os
from PIL import Image
import pyttsx3



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate',180)


def Speak(Audio):
    print("   ")
    engine.say(Audio)
    print(f": {Audio}")
    print("   ")
    engine.runAndWait()


Api_key = "11qFLOrvtE2BBeKIbxPOW8ueaVLpc5pebkq8VuHR"

def NasaNews(Date):
    Speak("Extracting Data From Nasa")

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)

    Params = {'date':str(Date)}

    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'
    
    with open(FileName,'wb') as f:

        f.write(Image_r.content)
    Path_1 ="E:\\PYTHON PROJECTS\\JARVIS 2.0\\" + str(FileName) 


    Path_2 ="E:\\PYTHON PROJECTS\\JARVIS 2.0\\NasaDataBase\\" + str(FileName)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)
    img.show()

    Speak(f"Title : {Title}")
    Speak(f"According To Nasa : {Info}")



