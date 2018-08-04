#!/opt/anaconda/bin/python

from sys import argv
from buffy.robot import Robot
from buffy.buffer import Buffer
from buffy.input_window import input_window
import random
from buffy.simulation import Simulation

def main():
    """
    :param args: goal pH
    Parse input params

    :return: None
    """

    # Set the goal pH
    goal = input_window()
    # Initialize the simulation
    s = Simulation(pka = 7, c = 0.5, v = 1)
    # Initialize the buffer, using the simulation
    b = Buffer(s, 4)

    # Create buffy
    buffy = Robot(goal, b)
    # Let buffy do its thing
    result = buffy.run()

    print(result)

if __name__ == "__main__":
    main()