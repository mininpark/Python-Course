# Room tour for having a new room mate

# while and for loop using maybe
def drink_tea():
    print("what kind of tea do you like?")


def start():
    drinks = ["tea", "cola", "coffee"]
    print("""Welcome to our home. Do you want to have something to drink?""")
    print("We have", ' '.join(drinks))
    answer = input("> ")

    if answer == "tea":
        print("I might like you as my roommate")
        drink_tea()
    elif answer == "cola":
        print("Hmmm")
    elif answer == "coffee":
        print("How dare you drink coffee at my home. get out")
        exit(0)
    else:
        print ("you are picky")


start()