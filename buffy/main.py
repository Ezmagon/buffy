from buffy.robot import Robot

def main():

    #b = Buffer()

    buffy = Robot(10)
    buffy.evaluate()

    #result = run(buffy)

    #i.show_result(result)

def run(r):
    """
    Main loop
    Input: r (Robot)
    :return:
    """
    r.observe()

if __name__ == "__main__":
    main()