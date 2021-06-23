import speech_recognition as sr
import pyttsx3
from datetime import date,datetime
import time ,os
import numpy as np
from VolumeHandControl import volumehandcontrol
import cv2
from detect import Face_detect

robot_ear = sr.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""


robot_mouth.say("Hello, i'm TenTen and what can i do for you!!")
robot_mouth.runAndWait()

while True:
    with sr.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    print("Robot: ... ")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: "+you)
    if you == "":
        robot_brain = "I can hear you, please try again!!!"
    elif "hello" in you:
        robot_brain = "Hello A Nam"
    elif "bye" in you:
        robot_brain = "Bye Nam"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "open" in you:
        robot_brain = "okay"
        volumehandcontrol()
    elif "camera" in you:
        robot_brain = "Let me check"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        Face_detect()
        robot_brain = "Ok, and now what can i do for you"
    else:
        robot_brain = "wait me a minute"
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()