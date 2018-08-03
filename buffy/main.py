#!/opt/anaconda/bin/python

from sys import argv
from buffy.robot import Robot
from buffy.buffer import Buffer
import random

def main(*args):
    if len(args) != 2:
        raise Exception("Wrong number of arguments")

    try:
        goal = float(args[1])
    except Exception as e:
        # Raise exception if not a number
        raise e

    if not goal < 14 or not goal > 1:
        raise ValueError("Input has to be between 1 and 14")

    buff = Buffer(random.randint(1, 14))

    buffy = Robot(goal, buff)
    result = buffy.run()

    print(result)

if __name__ == "__main__":
    main(*argv)