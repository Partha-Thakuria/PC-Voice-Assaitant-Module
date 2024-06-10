#pip install pyttsx3
import pyttsx3
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import eel


id=r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\IVONA 2 Voice Brian22"


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 175)
engine.setProperty('voice', id)


def Speak(*args, **kwargs):
    audio = ""
    for i in args:
        audio += str(i)
    print(Fore.CYAN+audio)
    eel.displayBotResponse(audio)
    engine.say(audio)
    engine.runAndWait()
#if __name__=="__main__":
    #Speak("hi i am a virtual assistant")