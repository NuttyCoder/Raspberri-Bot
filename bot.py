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