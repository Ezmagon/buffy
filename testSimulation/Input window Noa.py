from tkinter import *

def printtext():
    global e
    string = e.get()
    return string

window = Tk()

window.title("Buffy the Buffer Robot")
window.geometry("300x200")

app = Frame(window)
app.grid()
label = Label(app, text = "What is your goal pH?\n")
label.grid()

e = Entry(window)
e.pack()
e.focus_set()

app = Frame(window)
app.grid()
button = Button(app, text = "Go Buffy!")
button.grid()


window.mainloop()


'''
def goalpH():
    userinput = int(input("What is your goal pH?\n"))
    while userinput < 1 or userinput >14:
        print("This not a valid input, please enter a pH 1-14")
        userinput = int(input("What is your goal pH?\n"))
    else:
        print("Thank you! Buffy will get to work for you now")
    return userinput


goalpH = goalpH()

'''








