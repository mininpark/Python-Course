#WRITE DOWN IN TERMINAL

#MY OWN VERSION
def kaymak_and_honey(kaymak_count, honey_count):
    print ("I have now %dg kaymak!" % kaymak_count)
    print ("I have now %d bottles honey!" % honey_count)

kaymak_and_honey(200,4)

#cheese_and_crackers is the name of function with two variables.
#so that under this name there are 4 PRINT functions
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have %d cheeses!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")

#1. ALTERNATIVE
print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#2. ALTERNATIVE
print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#3. ALTERNATIVE
print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#4. ALTERNATIVE
print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

