people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We should not take the cars")
else:
    print("We can't decide, because cars and peoples are same amount")

if buses > cars:
    print("That's too many buses")
elif buses < cars:
    print("That's too many cars")
else:
    print("We still can't decide")

buses += 25
if people > buses:
    print("Alright, let's just take the buses")
else:
    print("Fine, let's stay home then")
