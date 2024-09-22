import openai
import speech_recognition as sr
import pyttsx3
# Intialize OpenAI API
openai.api_key = "your-api-key"
# Initialize speech recognition and text-to-speech
r = sr.Recognizer()
engine = pyttsx3.init()
# Listen to
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except:
            print("Sorry, I did not get that.")
            return None
# Speak to
def respond(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=200
    )
    message = response.choices[0].text.strip()
    print(f"Bot: {message}")
    engine.say(message)
    engine.runAndWait()

    while True:
        text = listen()
        if text:
            respond(text)