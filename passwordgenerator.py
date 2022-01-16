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
        l1.config(text="Enter a Number !!")


def Display():
    global final
    final = ''.join(password)  # str(e) for e in password
    t.delete("1.0", "end")
    t.insert(END, final)


def copyToClipboard():
    win.config(bg="Orange")
    l1.config(bg="Orange")
    l2.config(text="Copied to Clipboard",bg="Orange")
    cp.copy(final)


win = Tk()

win.geometry('500x500')
win.title("Password Generator")

img = PhotoImage(file='locks.png')
Label(win, image=img).place(x=170, y=5)

l1 = Label(win, text="Length of password ")
l1.place(x=180, y=220)
textin = StringVar()
e1 = Entry(win, width=20, textvariable=textin)
e1.place(x=180, y=240)

goButton = Button(win, text=" Go ", height=1, command=IsNumber)
goButton.place(x=305, y=237)

t = Text(bg='light gray', height=1, width=25)
t.place(x=150, y=350)

l2 = Label(win, text="Click Copy to copy password")
l2.place(x=150, y=320)
copyButton = Button(win, text=" Copy ", height=1, command=copyToClipboard)
copyButton.place(x=333, y=348)

win.mainloop()
