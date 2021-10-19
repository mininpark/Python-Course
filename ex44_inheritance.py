# Inheritance
# Inheritance is used to indicate that one class will get most or all of its features from a parent class.
# This happens implicitly whenever you write class Foo(Bar), which says “Make a class Foo that
# inherits from Bar.” When you do this, the language makes any action that you do on instances of
# Foo also work as if they were done to an instance of Bar. Doing this lets you put common functionality
# in the Bar class, then specialize that functionality in the Foo class as needed.

# OVERRIDE

# class Parent(object):
#    def override(self):
#        print("Parent override")


# class Child(Parent):
#    def override(self):
#        print("Child override")


class Parent(object):
    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()


class Strawberry(object):
    def __init__(self, stuff):
        self.stuff = stuff
        super(Strawberry, self).__init__()


result = Strawberry
print(result.__init__())



