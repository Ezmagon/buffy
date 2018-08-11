#!/usr/bin/env python3

from sys import argv
from buffy.robot import Robot
from buffy.buffer import Buffer
from buffy.interface import Windows
from buffy.computer_vision import VisionForRobot
import random
from buffy.simulation import Simulation
#import threading
#from buffy.Robot_graphics import robot_run
from buffy.graphs import plot_robot_graphs

def main():
    """
    :param args: goal pH
    Parse input params
    :return: None
    """
    # Set the goal pH
    win = Windows()
    win.input_window()
    win.choice_window()
    goal = win.phGoal
    choice = win.choice
    if choice == "standard":
        ph_sim = 7
    elif choice == "random":
        ph_sim = random.uniform(1, 14)
    elif choice == "computervision":
        v = VisionForRobot()
        ph_sim = v.recognize_numbers()

    #gfx_thread = threading.Thread(target=robot_run)
    #gfx_thread.start()

    print("Goal = ", goal, "Choice = ", choice)
    # Initialize the simulation
    s = Simulation(pka=7, c=0.5, v=1, start=ph_sim)
    # Initialize the buffer, using the simulation
    b = Buffer(s, 4)

    # Create buffy
    buffy = Robot(goal, b)
    # Let buffy do its thing
    result = buffy.run()
    #input("Press key to plot")
    plot_robot_graphs(buffy)
    #input("Plot done, press key")
    print(result)

if __name__ == "__main__":
    main()