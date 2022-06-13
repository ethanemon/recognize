import speech_recognition as sr
import pyttsx3
from difflib import SequenceMatcher
from parser import parse_file

negative_lines = parse_file("negative.txt")
neutral_lines = parse_file("neutral.txt")
positive_lines = parse_file("positive.txt")


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


def similar(task, lines):
    for line in lines:
        score = SequenceMatcher(None, task, line).ratio()
        if score > 0.8:
            return True
    return False


def recognize(task):
    is_negative = similar(task, negative_lines)
    is_neutral = similar(task, neutral_lines)
    is_positive = similar(task, positive_lines)
    if is_negative:
        talk("Это негативный ответ")
    elif is_neutral:
        talk("Это нейтральный ответ")
    elif is_positive:
        talk("Это положительный ответ")
    else:
        talk("Это другой ответ")


while True:
    recognize(command())
