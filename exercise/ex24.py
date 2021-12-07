print("Let's practice everything.")
# put one ' in ''single-quote
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("- - - - - - - - - - - - - - ")
print(poem)
print("- - - - - - - - - - - - - - ")


five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

# started is a local (temporary) variable. It's not necessary to have
def secret_formula(x):
    jelly_beans = x * 500
    # int is for integer()
    jars = int(jelly_beans / 1000)
    crates = int(jars / 100)
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))
print("We have {} beans, {} jars, and {} crates.".format(beans, jars, crates))

new_start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(new_start_point))
