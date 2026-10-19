from utils.connect_gemini import ask
from utils.model_loader import loader
from utils.predictor import output_generator
from utils.spelling_correction import speller
from utils.stabilizer import SentenceBuilder
from utils.voice import speak
import cv2


model=loader()
builder=SentenceBuilder()

def vedio_process(frame):
    frame=cv2.flip(frame,1)
    roi = frame[100:400, 300:600]
    cv2.rectangle(frame,(300,100), (600,400), (0,255,0), 2)

    letter,confidence=output_generator(model,roi)
    Sentence=builder.update(letter,confidence)

    user_text=None
    bot_responce=None

    if builder.should_send():
        correction=speller(Sentence)
        responce=ask(correction)
        user_text=correction
        bot_responce=responce

        speak(responce)

        builder.clear()
    
    return frame,letter,confidence,Sentence,user_text,bot_responce