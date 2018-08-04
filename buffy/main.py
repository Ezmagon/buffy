#!/opt/anaconda/bin/python

from sys import argv
from buffy.robot import Robot
from buffy.buffer import Buffer
from buffy.input_window import input_window
import random
from buffy.simulation import Simulation

def main(*args):
    """
    :param args: goal pH
    Parse input params

    :return: None
    """
    if len(args) != 2:
        raise Exception("Wrong number of arguments")

    try:
        goal = float(args[1])
    except Exception as e:
        # Raise exception if not a number
        raise e

    if not goal < 14 or not goal > 1:
        raise ValueError("Input has to be between 1 and 14")

    goal = input_window()
    s = Simulation(pka = 7, c = 0.5, v = 1)
    b = Buffer(s)

    buffy = Robot(goal, b)
    result = buffy.run()

    print(result)

if __name__ == "__main__":
    main(*argv)