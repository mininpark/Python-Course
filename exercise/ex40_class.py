# CLASS are like mini-MODULES
class MyStuff(object):
    # init function and self.tangerine is for setting the tangerine variable
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    # MyStuff hav an apple()function
    def apple(self):
        print("I am classy apples!")

# This is not working
# MyStuff.apple()
# For using class we need OBJECTS e.g. thing = MyStuff()


thing = MyStuff()
thing.apple()
print(thing.tangerine)
# self: Inside the functions in a class, self is a variable for the instance/object being accessed.


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't ant to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They really around the family",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
