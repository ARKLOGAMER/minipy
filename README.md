# MiniPy: Voice Assistant with OpenAI

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenAI API](https://img.shields.io/badge/OpenAI-GPT--3.5-blueviolet)](https://platform.openai.com/)
[![Build: Manual](https://img.shields.io/badge/Build-Manual-green)]()

**MiniPy** is a lightweight voice assistant built in Python using OpenAI's GPT-3.5, Google Text-to-Speech (gTTS), and speech recognition. It listens to your voice, processes it using ChatGPT, and responds with spoken output.

---

## Demo

![MiniPy Demo](demo.gif)  
*This is a placeholder — replace with a real GIF showing the assistant in action.*

---

## Features

- Voice input using microphone
- GPT-3.5 conversation engine
- Speech response with gTTS
- Audio playback using Pygame
- Continuous loop for natural interaction

---

## Installation

### Requirements

- Python 3.7+
- OpenAI API Key

### Install Dependencies

bash
pip install openai speechrecognition gtts pygame

For pyaudio:

Windows:

pip install pipwin
pipwin install pyaudio

Linux:

sudo apt install portaudio19-dev python3-pyaudio
pip install pyaudio



---

Setup

1. Clone this repository or download minipy.py.


2. Replace the line in minipy.py:

openai.api_key = 'your-api-key-here'

with your actual OpenAI API key.


3. Run:

python minipy.py




---

Usage

Speak when prompted.

Listen to the assistant’s voice response.

Exit anytime with Ctrl + C.



---

To-Do

[ ] Whisper ASR for better transcription

[ ] Save session chat logs

[ ] GUI interface (Tkinter/PyQt)

[ ] Add voice command control (e.g., “stop”, “repeat”)



---

License

This project is licensed under the MIT License.

