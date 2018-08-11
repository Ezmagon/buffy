# Custom
from buffy.robot import Robot
from buffy.buffer import Buffer
from buffy.interface import Windows
from buffy.computer_vision import VisionForRobot
from buffy.simulation import Simulation
from buffy.graphs import plot_robot_graphs
# Builtin
import random

def main():
    # Set the goal pH from user input
    win = Windows()
    win.input_window()
    win.choice_window()
    goal = win.phGoal
    # Get choice for starting pH for the demo
    choice = win.choice

    # Choose between pH 7 (standard), a random pH or pH derived from computer vision
    if choice == "standard":
        ph_sim = 7
    elif choice == "random":
        ph_sim = random.uniform(1, 14)
    elif choice == "computervision":
        v = VisionForRobot()
        ph_sim = v.recognize_numbers()
    print("Goal = ", goal, "Choice = ", choice)

    # Initialize the simulation

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