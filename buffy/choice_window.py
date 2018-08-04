from tkinter import *

def choice_window():

    """this creates the window and title of the window"""
    window = Tk()                   #dit maakt de orginele window met titel
    window.geometry("300x150")
    window.title('Buffy the Buffer Robot')

    a = Frame(window)                #dit maakt de vraag zin
    a.pack()
    label = Label(a, text = "Choose start pH:\n")
    label.grid()

    """Three buttons that currently do nothing"""
    b = Button(window,text='Standard')
    b.pack(side='top')
    b = Button(window,text="Random pH")
    b.pack(side='top')
    b = Button(window,text="Computer vision")
    b.pack(side='top')

    window.mainloop()

output = choice_window()












