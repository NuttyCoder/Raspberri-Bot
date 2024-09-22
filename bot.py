#python bot used for Raspberry Pi
#1. create a wake word
#2. create a response to the wake word
#3. pass query to OpenAi 
#4. return response from OpenAi
#5. pass response to text to speech
#6. return audio response

import keys
import waitForWakeWord
import SpeechRec
import callOpenai
import openai
from gtts import gTTS
import playsound

def speak(text, filename):
    tts = gTTS(text, lang='en')
    tts.save(filename)

def play(filename):
    playsound.playsound(filename)

openai.api_key = keys.key['OPENAI_API_KEY']
filename = 'query.mp3

def Gspeak():
    speak('Hello, how can I help you?', filename)
    play(filename)
    query = SpeechRec.record()
    response = callOpenai(query)
    speak(response, filename)
    play(filename)

    if query != "quit"
        Gspeak("I think you said" + str(query) + "but I am not sure")
        response = callOpenai.openai_create(query)
        Gspeak(response)
        Gspeak("Do you have any other questions?")

    else:
        sucess = False
        Gspeak("Goodbye, have a nice day")
