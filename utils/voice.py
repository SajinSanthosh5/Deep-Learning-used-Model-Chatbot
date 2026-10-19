from gtts import gTTS
import os

def speak(text):
    tts=gTTS(text=text,lang="en")
    tts.save("responce.mp3")
    os.system("start responce.mp3")

# if __name__=="__main__":
#     print("module loaded")
#     speak("malayalam ariyumo")
