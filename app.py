import speech_recognition as sr
import os
import sys
import pyttsx3


def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
        print("вы сказали: " + task)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        task = command()

    return task


def recognize(task):
    if 'да' in task:
        talk("Вы сказали да")

    elif 'нет' in task:
        talk("Вы сказали нет")
        sys.exit()
    elif 'наверное' in task:
        talk("Вы сказали наверное")

    elif 'наверное' in task:
        talk("Может быть")


while True:
    recognize(command())
