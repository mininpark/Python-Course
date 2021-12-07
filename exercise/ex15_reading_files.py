# import the arguments from system, that it's already given
from sys import argv
# two arguments (filename has based on actual file name
script, filename = argv
# txt is the name of function to open the file
txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
# what is the meaning of "> "
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
