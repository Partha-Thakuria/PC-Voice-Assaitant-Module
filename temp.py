from Genration_Of_Images import Generate_Images , Show_Image
from func.Speak.SpeakOffline import Speak
from toolkit.Mistral import Mistral7B

summary = Mistral7B("summarize the current conversation", temperature=0.9)
Speak(summary)