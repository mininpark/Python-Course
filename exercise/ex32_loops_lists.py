the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies',2 ,'dimes',3, 'quarters']

for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type: %s" % fruit)

# %r if we don't know what' in it
for i in change:
    print("I got %r" % i)

# build lists, first start with an empty list
elements = []

# FUNCTION RANGE from 0 to 5
for i in range(0, 6):
    print("Adding %d to the list" % i)
    # append is add something to the end
    elements.append(i)

# now we can print them out
for i in elements:
    print("Element was: %d" % i)

# from 1 to 4 range
mina = []
for z in range(1, 5):
    mina.append(z)
    print(mina)
