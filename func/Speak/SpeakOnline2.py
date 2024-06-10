from gtts import gTTS
from io import BytesIO
import pygame
import eel


def Speak(*text):
    txt=""
    for i in text:
        txt+=str(i)
    eel.displayBotResponse(txt)
    tts = gTTS(text=txt, lang='en', slow=False)

    # Save the speech as an in-memory file
    speech_file = BytesIO()
    tts.write_to_fp(speech_file)
    speech_file.seek(0)

    # Play the speech using pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(speech_file)
    pygame.mixer.music.play()

    # Wait for the speech to finish playing
    while pygame.mixer.music.get_busy():
        continue

