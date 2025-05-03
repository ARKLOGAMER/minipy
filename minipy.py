import openai
import speech_recognition as sr
from gtts import gTTS
import os
import io
import pygame

Set your OpenAI API key

openai.api_key = 'your-api-key-here'

Initialize the Pygame mixer

pygame.mixer.init()

def listen():
# Initialize recognizer
recognizer = sr.Recognizer()
with sr.Microphone() as source:
print("Listening...")
audio = recognizer.listen(source)
try:
print("Recognizing...")
query = recognizer.recognize_google(audio, language='en-US')
print(f"You said: {query}\n")
except Exception as e:
print("Sorry, I did not get that. Could you please repeat?")
return None
return query

def speak(text):
# Use gTTS to convert text to speech
tts = gTTS(text=text, lang='en', slow=False)

# Save the speech to a memory stream  
fp = io.BytesIO()  
tts.write_to_fp(fp)  
fp.seek(0)  
  
# Play the speech directly from memory using Pygame  
pygame.mixer.music.load(fp, "mp3")  
pygame.mixer.music.play()  
  
# Wait until the speech is done  
while pygame.mixer.music.get_busy():  
    continue

def ask_openai(prompt):
response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": prompt},
]
)
return response.choices[0].message['content'].strip()

def main():
# Setting the initial prompt for the chatbot
initial_prompt = (
"ADD YOUR PRESET PROMPT"
)
while True:
query = listen()
if query:
complete_prompt = f"{initial_prompt}\nUser: {query}\n Bot:"
response = ask_openai(complete_prompt)
print(response)
speak(response)

if name == "main":
main()
