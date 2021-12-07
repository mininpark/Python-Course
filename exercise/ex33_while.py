i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    # i = i + 1
    i += 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)


print("The numbers: ")
# x can be everything. num, x, y, z, ect.
for x in numbers:
    print(x)

