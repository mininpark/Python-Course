# import the arguments from system, that it's already given
from sys import argv
# two arguments
script, filename = argv
# new command OPEN filename.txt form
txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
# what is the meaning of "> "
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
