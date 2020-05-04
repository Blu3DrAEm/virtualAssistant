# Python Virtual Assistant
# Josh Anderson
# 05/01/2020
# pip install speechrecognition,  pip install pyaudio, pip install gtts, pip install playsound, pip install PyObjC

# User guide:
# Say "Search" to search the web
# Say "Set a timer" to set timer using DuckDuckGo
# Say "Exit" or "Thank you" to quit

import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Virtual Assistant")
wn.tracer(0)

# Register the shapes - need to get an image
wn.register_shape("virtualassistant.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

# Create the Virtual Assistant turtle
player = turtle.Turtle()
player.color("blue")
player.shape("virtualassistant.gif")
player.penup()
player.speed(0)
player.setposition(0, 0)
player.setheading(90)
player.speed = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.setposition(0, -260)
score_pen.write('Press "Spacebar" to begin', False, align="center", font=("Arial", 25, "normal"))
score_pen.hideturtle()

while True:
    wn.update()

    def virtual_assistant():
        r = sr.Recognizer()

        def record_audio(ask=False):
            with sr.Microphone() as source:
                if ask:
                    computer_speak(ask)
                audio = r.listen(source)
                voice_data = ''
                try:
                    voice_data = r.recognize_google(audio)
                except sr.UnknownValueError:
                    computer_speak("I'm sorry, I didn't get that")
                except sr.RequestError:
                    computer_speak('Sorry, my speech service is down')
                return voice_data


        def computer_speak(audio_string):
            tts = gTTS(text=audio_string, lang='en')
            r = random.randint(1, 10000000)
            audio_file = 'audio-' + str(r) + '.mp3'
            tts.save(audio_file)
            playsound.playsound(audio_file)
            print(audio_string)
            os.remove(audio_file)


        # Questions you can ask the computer
        def respond(voice_data):
            if 'what is your name' in voice_data:
                computer_speak('I am your Computer')
            if 'what do you do' in voice_data:
                computer_speak("I can search the web and set a timer for you using DuckDuckGo.\n Say 'Search' or 'Set a timer'")
            if 'what can you do' in voice_data:
                print("I can search the web and set a timer for you using DuckDuckGo.\n Say 'Search' or 'Set a timer'")
            if 'search' in voice_data:
                search = record_audio('what would you like me to search for?')
                url = 'https://duckduckgo.com/?q=' + search
                webbrowser.get().open(url)
                computer_speak('Let me get right on it! ' + search)
                voice_data = record_audio('Anything else?')
            if 'thank you' in voice_data:
                computer_speak("You're welcome! Good bye")
                exit()
            if 'no thank you' in voice_data:
                computer_speak('Ok, have a great day!')
                exit()
            if 'how are you' in voice_data:
                computer_speak("I am very well! Thank you. How can I help you?")
            if 'set an timer' in voice_data:
                search = record_audio('for how long?')
                url = 'https://duckduckgo.com/?q=' + "set a timer for" + " " + search
                webbrowser.get().open(url)
                computer_speak('Ok, set a timer for ' + search)
                voice_data = record_audio('Anything else?')
            if 'set a timer' in voice_data:
                search = record_audio('for how long?')
                url = 'https://duckduckgo.com/?q=' + "set a timer for" + " " + search
                webbrowser.get().open(url)
                computer_speak('Ok, set a timer for ' + search)
                voice_data = record_audio('Anything else?')
            if 'exit' in voice_data:
                computer_speak('Goodbye')
                exit()
            if 'goodbye' in voice_data:
                computer_speak('Goodbye')
                exit()

        time.sleep(1)
        computer_speak('How can I help you?')
        while 1:
            voice_data = record_audio()
            respond(voice_data)


    # To activate VirtualAssistant
    # Keyboard Bindings
    wn.listen()
    wn.onkeypress(virtual_assistant, "space")
    wn.onkeypress(virtual_assistant, "q")
