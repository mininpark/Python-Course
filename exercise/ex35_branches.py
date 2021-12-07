from sys import exit

def bear_room():
    print("""There is a bear here. \nThe bear has a bunch of honey. \nThe fat bear is in front of another door. \nHow are you going to move the bear?""")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go it through now. you can open door")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")


def gold_room():
    print("This room is full of gold. How much do you wanna take?")

    next = input("> ")
    # what makes this?
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        # game done
        # EXIT(0)
        # On many operating systems, a program can abort with exit(0), and the number passed in will
        # indicate an error or not. If you do exit(1), then it will be an error, but exit(0) will be a good
        # exit. The reason it’s backward from normal boolean logic (with 0==False) is that you can use
        # different numbers to indicate different error results. You can do exit(100) for a different error
        # result than exit(2) or exit(1).
        exit(0)
    else:
        dead("You are greedy bastard!")


def evil_room():
    print("""Here you see the great evil Cthulhu. 
    He, it whatever stares at you and you go insane.
    Do you flee for your life or eat your head?""")

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty")
    else:
        evil_room()

def dead(why):
    # why argument gives the each dead(""), and more message added and exit
    print(why, "You dead!")
    exit(0)

def start():
    print("""You are in a dark room. \nThere is a door to your right and left. \nWhich one do you take?""")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        evil_room()
    else:
        dead("You trumble around the room til you starve.")

start()
