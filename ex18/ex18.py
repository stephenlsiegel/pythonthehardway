# Names, Variables, Code, Functions

# Functions do three things:
	# 1. They name pieces of code the way variables name strings and numbers.
	# 2. They take arguments the wya your scripts take argv
	# 3. Using 1 and 2 they let you make your own "mini scripts" or "tiny commands."
	
# You create a function using the word def

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothin'."
	
print_two("Stephen", "Siegel")
print_two_again("Stephen", "Siegel")
print_one("First!")
print_none()

# Function Checklist:
# 1. Did you start your function with def?
# 2. Does your function name have only characters and underscores?
# 3. Did you put an open parenthesis ( right after the function name?
# 4. Did you put your arguments after the parenthesis separated by commas?
# 5. Did you make each argument unique (no duplicated names)?
# 6. Did you put a close parenthesis and a colon ): after the arguments?
# 7. Did you indent all lines of code you want in the function four spaces? No more, no less.
# 8. Did you end you function by going back to writing with no indent?

# When you run or call a function, check these things:
# 1. Did you call/use/run this function by typing its name?
# 2. Did you put the ( character after the name to run it?
# 3. Did you put the values you want into the parenthesis separated by commas?
# 4. Did you end the function call with a ) character?

