import tkinter as tk
from tkinter import *


def user_goal_ph(text):
    global goal_ph
    if text == "": return True
    try:
        goal_ph=float(text)
    except ValueError:
        return False
    return 1 <= goal_ph <= 14


window = Tk()                   #dit maakt de orginele window met titel
window.geometry("300x100")
window.title('Buffy the Buffer Robot')

a= Frame(window)                #dit maakt de vraag zin
a.pack()
label = Label(a, text = "What is your goal pH?\n")
label.grid()


vcmd = (window.register(user_goal_ph), "%P")         #dit roept de limiterende functie op in input window
entry = Entry(window, validate = "key", validatecommand=vcmd)
entry.pack()
entry.focus_set()

b = Button(window,text='Go Buffy!',command=user_goal_ph)
b.pack(side='right')
b = Button(window,text="Nevermind, I'm going for lunch!", command=window.destroy)
b.pack(side='left')
window.mainloop()


print(goal_ph)






''''

def goalpH():
    userinput = int(input("What is your goal pH?\n"))
    while userinput < 1 or userinput >14:
        print("This not a valid input, please enter a pH 1-14")
        userinput = int(input("What is your goal pH?\n"))
    else:
        print("Thank you! Buffy will get to work for you now")
    return userinput


goalpH = goalpH()

''''








