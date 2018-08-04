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

def input_window():

    """This creates out user input window and stores the goal pH for later use"""

    def user_goal_ph(inp):
        global goal_ph
        if inp == "": return True
        try:
            goal_ph=float(inp)
        except ValueError:
            return False
        return 1 <= goal_ph <= 14


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

    """combines window.destroy command and choice_window"""
    def func1(evt=None):
        window.destroy()
        choice_window()

    """command destroys window and loads choice_window"""
    b = Button(window,text='Go Buffy!', command=func1)
    b.pack(side='right')
    b = Button(window,text="Nevermind, I'm going for lunch!", command=window.destroy)
    b.pack(side='left')

    window.mainloop()

    return goal_ph


output = input_window()
print("Output = " + str(output))



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








