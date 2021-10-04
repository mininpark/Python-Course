x = input("Enter your age: ")
y = input("Enter your height: ")
z = input("Enter your weight: ")

print ("How old are you?"), 
#raw_input renamed to input in Python3
#input is here not given
age = input(x)

print ("How tall are you?"),
height = input(y)

print ("How much do you weight?"),
weight = input(z)

print ("So, you're %r old, %r tall and %r heavy." % (
x, y, z))

