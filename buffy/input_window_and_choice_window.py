from tkinter import *
from buffy.buffer import Buffer
import sys

class Windows():
    def __init__(self):
        self.phGoal = 1
        self.choice = "standard"
        pass

    def choice_window(self):
        def standard():
            self.choice = "standard"
            window.destroy()

        def random():
            self.choice = "random"
            window.destroy()

        def computer_vision():
            self.choice = "computervision"
            window.destroy()

        """this creates the window and title of the window"""
        window = Tk()                   #dit maakt de orginele window met titel
        window.geometry("300x80")
        window.title('Buffy the Buffer Robot')

        a = Frame(window)                #dit maakt de vraag zin
        a.pack()
        label = Label(a, text = "Press to start computer vision!\n")
        label.grid()

        """Three buttons that currently do nothing"""
        # b = Button(window,text='Standard = 7', command=standard)
        # b.pack(side='top')
        # b = Button(window,text="Random pH", command=random)
        # b.pack(side='top')
        b = Button(window,text="Computer vision", command=computer_vision)
        b.pack(side='top')

        window.mainloop()

    def input_window(self):
        """This creates out user input window and stores the goal pH for later use"""
        def user_goal_ph(inp):
            self.phGoal
            if inp == "": return True
            try:
                self.phGoal = float(inp)
            except ValueError:
                return False
            return 1 <= self.phGoal <= 14


        window = Tk()                   #dit maakt de orginele window met titel
        window.geometry("300x100")
        window.title('Buffy the Buffer Robot')

        a = Frame(window)                #dit maakt de vraag zin
        a.pack()
        label = Label(a, text = "What is your goal pH?\n")
        label.grid()


        vcmd = (window.register(user_goal_ph), "%P")    # dit roept de limiterende functie
                                                        #  op in input window
        entry = Entry(window, validate = "key", validatecommand=vcmd)
        entry.pack()
        entry.focus_set()


        """command destroys window and loads choice_window"""
        b = Button(window,text='Go Buffy!', command=window.destroy)
        b.pack(side='right')
        b = Button(window,text="Nevermind, I'm going for lunch!", command=sys.exit)
        b.pack(side='left')

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








