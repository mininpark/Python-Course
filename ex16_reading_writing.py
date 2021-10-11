# COMMANDS LIST
# • open - open the file
# • close —Closes the file. Like File- >Save.. in your editor.
# • read —Reads the contents of the fi le. You can assign the result to a variable.
# • readline —Reads just one line of a text file.
# • truncate —Empties the file. Watch out if you care about the file.
# • write(stuff) —Writes stuff to the file.

from sys import argv

script, filename = argv

print("We're going to erase %r" % filename)
print("If you don't want that, hit CTRL-C (^C)")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")

# open this fi le in ‘write’ mode”—hence the 'w' character.
# There’s also 'r' for “read,” 'a' for append, and modifiers ('w+','r+' and 'a+') on these.
target = open(filename, 'w')

print("Truncating the file. Goodbye")
target.truncate()

print("Now I'm going to ask you for three lines.")
# ask questions for input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
print("Now I'm going to ask you for simple line.")

line_long = input("")
target.write(line_long)
target.write("\n")

print("And finally, we close it.")
target.close()
