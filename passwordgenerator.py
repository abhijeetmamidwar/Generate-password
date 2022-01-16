import random as rd
import pyperclip as cp
from tkinter import *

letterC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  ## 26 possibilites
letterS = "abcdefghijklmnopqrstuvwxyz"  ## 26 possibilites
numbers = "1234567890"  ## 10 possibilites
alpha = "\`~!@#$%^&*(_)-+=[{]}|;:'.>,<?/*" + '"'  ## 33 possibilites

password = []
final = ""

team = {"letterC": 26, "letterS": 26, "numbers": 10, "alpha": 33}


def selector(r):
    try:
        r != int()
    except:
        r = int(rd.random() * 4) + 1
    if r == 1:
        v = int(rd.random() * (26))
        password.append(letterC[v:v + 1])
    elif r == 2:
        v = int(rd.random() * (26))
        password.append(letterS[v:v + 1])
    elif r == 3:
        v = int(rd.random() * (10))
        password.append(numbers[v:v + 1])
    else:
        v = int(rd.random() * (33))
        password.append(alpha[v:v + 1])


def generator(l):
    for i in range(l):
        selector(i)
    Display()


def compulsory():
    for i in range(4, 0, -1):
        selector(int(i))


def IsNumber():
    text = textin.get()
    try:
        length = int(text)
        password.clear()
        compulsory()  # includes compulsororily each type of character
        generator(length - 4)
    except:
        print("Enter a No.")


def Display():
    global final
    final = ''.join(password)  # str(e) for e in password
    t.delete("1.0", "end")
    t.insert(END, final)


def copyToClipboard():
    cp.copy(final)


win = Tk()

win.geometry('300x300')
win.title("Password Generator")

textin = StringVar()
e1 = Entry(win, width=20, textvariable=textin)
e1.place(x=85, y=80)

goButton = Button(win, text=" Go ", height=1, command=IsNumber)
goButton.place(x=210, y=77)

t = Text(bg='light gray', height=1, width=25)
t.place(x=40, y=150)

copyButton = Button(win, text=" Copy ", height=1, command=copyToClipboard)
copyButton.place(x=245, y=147)

win.mainloop()
