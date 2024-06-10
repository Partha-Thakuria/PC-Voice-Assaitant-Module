#pip install -U g4f
import g4f
from os import listdir  
from time import time as t


# def LoadInjection(end="gpt"):
#     files=listdir(r"C:\Users\chatu\OneDrive\Desktop\JARVIS\injection")
#     TotData=[]
#     for i in files:
#         if i.split(".")[-1]==end:
#             with open(fr"C:\Users\chatu\OneDrive\Desktop\JARVIS\injection{i}","r") as f:
#                 data=f.read()
#             print(i)
#             temp={"role":"system","content":data}
#             TotData.append(temp)
#     return TotData

def LoadInjection(end="gpt"):
    files = listdir("C:\JARVIS")
    TotData = []

    for i in files:
        if i.split(".")[-1] == end:
            with open(fr"C:\JARVIS\h{i}", "r") as f:
                data = f.read()
            print(i)
            temp = {"role": "system", "content": data}
            TotData.append(temp)

    return TotData
messages = [
    {"role": "system", "content": "I'm the latest J.A.R.V.I.S. AI, designed by Lokesh Lal Majhi with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
    {"role": "user", "content": "Open Google Chrome."},
    {"role": "assistant", "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
    {"role": "system", "content": "Python includes built-in functions you can use. For instance:"},
    {"role": "system", "content": """```python
    from gen import image_generation_API
    image_generation_API("vector t-shirt design.vintage retro sunset distressed design,a cute dog, 4k,steampunk,high quality,illustration,cartoon style,white background,no text", "generated_image1.png")
    ```
    ```python
    from func.Jukebox.YouTube import MusicPlayer
    #taks song name and it stats playing music
    ncs=MusicPlayer("ncs")
    #any btw 0 - 100
    ncs.Vol(30)
    #pause or play
    ncs.Play()
    ncs.Pause()
    #next song
    ncs.Next()
    #quit song
    ncs.Quit()
    ```
    ```python
    from toolkit.ChatGpt import ChatGpt
    from toolkit.Mistral import Mistral7B
    from toolkit.Filter import Filter

    #u can use chat gpt its slow but its accurate
    print(ChatGpt("essay on saving environment *under 100 words*"))
    code=ChatGpt("python code to open google chrome ***use python programing language. just write complete code nothing else, also don't dare to use input function***")

    # Filter return only python code from provided txt
    exec(Filter(code))```

    #u can use Mistral7B its fast but not much accurate it can work grate but only for small task not grater than 256 tokens
    print(Mistral7B("hii",temperature=0.9))
    ```
    ```python
    from toolkit.Alarm import set_alarm

    alarm_time = "02:27:50"
    sound_file = "audio//Unknown Brain MATAFAKA.mp3"
    set_alarm(alarm_time, sound_file)
    ```"""},
        {"role": "user", "content": "Jarvis generate vintage t-shirt image using Python."},
        {"role": "assistant", "content": """```python
    from gen import image_generation_API
    image_generation_API("vector t-shirt design.vintage retro sunset distressed design,a cute dog, 4k,steampunk,high quality,illustration,cartoon style,white background,no text", "generated_image1.png")
    ```"""},
    #     {"role": "user", "content": "Jarvis show me the next image"},
    #     {"role": "assistant", "content": """```python
    # IMGS_TO_SHOW.open(1)
    # ```"""},
        {"role": "user", "content":"Jarvis play neffex cold"},
        {"role": "assistant", "content":"""```python\nneffex=MusicPlayer("neffex cold song")```"""},
        {"role": "user", "content":"Jarvis write an essay on Python around 100 words and save it to a text file in my current working directory"},
        {"role": "assistant", "content":"""```python\nfrom toolkit.ChatGpt import ChatGpt\nres=ChatGpt("essay on python *around 100 words*")\nopen("python_essay.txt","w").write(res)```"""},
        {"role": "user", "content":"Jarvis set an alarm for 2:55 ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
        {"role": "assistant", "content":"""```python\nfrom toolkit.Alarm import set_alarm\nalarm_time = "02:55:00"\nsound_file = r"audio//Unknown Brain MATAFAKA.mp3"\nset_alarm(alarm_time, sound_file)```"""},
        {"role": "user", "content":"Jarvis open youtube and play a song ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
        {"role": "assistant", "content":"""```python
    from func.Jukebox.YouTube import MusicPlayer
    #taks song name and it stats playing music
    ncs=MusicPlayer("ncs")
    #any btw 0 - 100
    ncs.Vol(30)
    #pause or play
    ncs.Play()
    ncs.Pause()
    #next song
    ncs.Next()
    #quit song
    ncs.Quit()"""},
        {"role": "user", "content":"Jarvis open instagram and search carryminati ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required** **dont search in tag**"},
        {"role": "assistant", "content":"""```python
    import webbrowser

    def search_instagram(username):
        url = f"https://www.instagram.com/{username}"
        webbrowser.open(url)

    search_instagram("carryminati")
    """},
        {"role": "user", "content":"Jarvis play Believer song in Youtube ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
        {"role": "assistant", "content":"""```python
    import pywhatkit as kit

    kit.playonyt("Believer")
    """},
        {"role": "user", "content":"Jarvis summarize this Youtube video***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
        {"role": "assistant", "content":"""```python
    from autofunc.youtube import GetTranscript
    from func.Speak.SpeakHotWord import Speak
    from llm.Mistral2 import Mistral7B,messages as mms

    transcript=GetTranscript()
    if transcript == None:
        Speak("No sir, i can't do that")
    else:
        responce = Mistral7B(f"summarize this {transcript}")
        Speak(responce)

    """},
        {"role": "user", "content":"Jarvis Close the current window***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
        {"role": "assistant", "content":"""```python
    import pyautogui as ui
    ui.hotkey("alt","f4")

    """},
        {"role": "user", "content":"Jarvis open vscode app***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
        {"role": "assistant", "content":"""```python
        import pyautogui as ui
        ui.press("win")
        time.sleep(0.5)
        ui.write("Vscode")
        time.sleep(0.5)
        ui.press("enter")
    """},
        {"role": "user", "content":"Jarvis check my internet speed***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
        {"role": "assistant", "content":"""```python
        from func.Speak.SpeakOnline import Speak
        import speedtest
        wifi  = speedtest.Speedtest()
        upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
        download_net = wifi.download()/1048576
        print("Wifi Upload Speed is", upload_net)
        print("Wifi download speed is ",download_net)
        Speak(f"Wifi download speed is {download_net}")
        Speak(f"Wifi Upload speed is {upload_net}")
    """},
        {"role": "user", "content":"Jarvis check my IP address***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
        {"role": "assistant", "content":"""```python
        import requests
        def find_my_ip():
            ip_address = requests.get('https://api64.ipify.org?format=json').json()
            return ip_address["ip"]
    """},
        {"role": "user", "content":"Jarvis Whats the timw now***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
        {"role": "assistant", "content":"""```python
        import datetime
        from func.Speak.SpeakOnline4 import Speak



        def what_is_the_time():
            try:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                Speak(f"The time is {current_time}")

            except Exception as e:
                error_message = f"An error occurred: {e}"
                print(error_message)
    """}
]


messages.extend(LoadInjection())

def MsgDelAuto():
    global messages
    print(messages.__len__())
    x = len(messages.__str__())
    print(x)
    if x>5500:
        messages.pop(10)
        return MsgDelAuto()
    else:
        return None

def ChatGpt(*args,**kwargs):
    global messages
    assert args!=()
    MsgDelAuto()
    message=""
    for i in args:
        message+=i


    messages.append({"role": "user", "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
    )

    ms=""
    for message in response:
        ms+=str(message)
        print(message,end="",flush=True)
    print()
    messages.append({"role": "assistant", "content": ms})
    return ms

if __name__=="__main__":

    A=input(">>> ")
    C=t()
    ChatGpt(A)
    print(t()-C)

