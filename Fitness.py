from tkinter import*
import time
import pyttsx3
def count(x):
    t=0
    while t<x:
        time.sleep(1)
        engine=pyttsx3.init()
        engine.say(t)
        engine.runAndWait()
        t+=1
    if t==x:
        engine=pyttsx3.init()
        engine.say("done")
        engine.runAndWait()

def march_on_the_spot(y==30):
    print("Start off marching on the spot and then march forwards and backwards. Pump your arms up and down in rhythm with your steps, keeping the elbows bent and the fists soft.")
    count(x)
march_on_the_spot()