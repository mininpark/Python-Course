# decimal number put in %d postion 
x = "There are %d types of people" % 10
#string variables
binary = "binary"
do_not = "don't"
# put variables in %s position 
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

#print %r whatever it's written and put variables in %r postion
print ("I said: %r." % x)
# for using '', it's because of style
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Ist't that joke su funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."
# why? adding two of them into one sentence? for putting a variable in it
print (w + e)