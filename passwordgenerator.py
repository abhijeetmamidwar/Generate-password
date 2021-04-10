from tkinter import *
import random as rd

letterC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"              ## 26 possibilites
letterS = "abcdefghijklmnopqrstuvwxyz"              ## 26 possibilites
numbers = "1234567890"                              ## 10 possibilites
alpha = "\`~!@#$%^&*(_)-+=[{]}|;:'.>,<?/*" + '"'    ## 33 possibilites

password = []

team = {"letterC":26,"letterS":26,"numbers":10,"alpha":33}

def selector(r):
    try:
        r != int()
    except:
        r = int(rd.random()*4)+1
    if r == 1:
        v = int(rd.random()*(26))
        password.append(letterC[v:v+1])
    elif r == 2:
        v = int(rd.random()*(26))
        password.append(letterS[v:v+1])
    elif r == 3:
        v = int(rd.random()*(10))
        password.append(numbers[v:v+1])
    else:
        v = int(rd.random()*(33))
        password.append(alpha[v:v+1])

def generator(l):
    for i in range(l):
        selector(i)
    print(*password,sep="")
    t.insert(END,"hi")

def IsNumber():
    text = textin.get()
    try:
        length = int(text)
        generator(length-5)
    except:
        print("Enter a No.")


def compulsory():
    for i in range(4,-1,-1):
        selector(int(i))

compulsory()        # includes compulsororily each type of character

win = Tk()
win.geometry('300x300')
win.title("Password Generator")

textin = StringVar()
e1 = Entry(win , width = 20 , textvariable = textin)
e1.place(x=80 , y=80)

b = Button(win , text=" Go " , command=IsNumber)
b.place(x=120 , y=110)

t = Text(bg='light gray',height=1,width = 15)
t.place(x=80 , y=150)

win.mainloop()

