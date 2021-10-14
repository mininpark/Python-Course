ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait! There is not 10 things in that list. Let's fix that")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Corn", "Frisbee", "Banana", "Girl", "Boy"]

# length of stuff (length is different from index)
while len(stuff) != 10:
    # the last of the list pop
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # append each of "next_one" in to "stuff"
    stuff.append(next_one)
    print("There's %d items now" % len(stuff))

print("There we go: ", stuff)

# 0. index of the list
print(stuff[0])
# 1. index of the list
print(stuff[1])

# -1 from the behind of the list (last one)
print(stuff[-1])
print(stuff.pop())

print(stuff)
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
