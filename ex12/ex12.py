# Prompting People

# For raw_input(), if you put a string inside the parentheses, it will prompt the user with that string.

# We can rewrite exercise 12 just using raw_input
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r years old, %r tall and %r heavy." % (age, height, weight)


# pydoc will generate documentation from python models, try running:

# pydoc raw_input