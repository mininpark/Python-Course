from sys import argv
from os.path import exists

script, from_file, to_file = argv

# THis script can be shorten by one line!! HOW?
print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

# LENGTH OF INPUT FILE DATA
print("The input file is %d bytes long" % len(indata))
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL- C to abort.")
# HINT RETURN OR NOT TO CHECK
input()

# the forward version from out_file will be deleted and renewed from new file copy
out_file = open(to_file, 'w')
out_file.write(indata)

print("Now, I'm opening the new file for copying...")
print("Alright, all done.")

out_file.close()
in_file.close()