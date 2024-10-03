import tkinter as tk
from playsound import playsound
import threading

window = tk.Tk()
window.config(width=500, height=500)
window.title("Shrimp Detector")
title = tk.Label(text="Shrimp Detector", font=("Arial", 25))
shrimp = tk.PhotoImage(file="pngegg.png")
shrimpLabel = tk.Label(image=shrimp)
pepe = tk.PhotoImage(file="pepe.png")
whale = tk.PhotoImage(file="Whale.png")

def play1():
    playsound("WAHAHAHAHAHA (Tiktok laughing meme sound).mp3")

def play2():
    playsound("Gentlemen, The King! Sound effect.mp3")

threadsound1 = threading.Thread(target=play1)
threadsound2 = threading.Thread(target=play2)

def yes():
    yesWindow = tk.Toplevel()
    yesWindow.title("Shrimp Detector")
    yesWindow.config(width=2000, height=2000)
    whaleLabel = tk.Label(yesWindow, image=whale).pack()
    threadsound1.start()
    

def no():
    noWindow = tk.Toplevel()
    noWindow.title("Shrimp Detector")
    noWindow.config(width=2000, height=2000)
    pepeLabel = tk.Label(noWindow, image=pepe).pack()
    threadsound2.start()

def start():
    queryWindow = tk.Toplevel()
    queryWindow.title("Shrimp Detector")
    queryWindow.config(width=400, height=400)

    question = tk.Label(queryWindow,text="Are you a shrimp?")
    yesButton = tk.Button(queryWindow, text="Yes", command=yes)
    noButton = tk.Button(queryWindow,text="No", command=no)
    question.pack()
    yesButton.pack()
    noButton.pack()

startButton = tk.Button(text="Start Detection",
                   command=start)



title.pack()
shrimpLabel.pack()
startButton.pack()

window.mainloop()