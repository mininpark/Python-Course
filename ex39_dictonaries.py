# dictionary or hash maps
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

print(states)

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
print(cities)

# add more cities with ['']
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print(cities)

print('-' * 10)
# print one city with ID
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
# print one state with ID
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# abbreviation = shorten version
# what is going inside of the argumentation, is not that important
# ___.items(): to return the list with all dictionary keys with values
print('-' * 10)
print(cities.items())
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has %s" % (state, abbrev, cities[abbrev]))

# ...get() method returns the value for the specified key if the key is in the dictionary
print('-' * 10)
state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas")

power = cities.get('CA', 'hpa')
print(power)

city = cities.get('TX', 'Does not exist')
print("The city for the state 'TX' is: %s" % city)



