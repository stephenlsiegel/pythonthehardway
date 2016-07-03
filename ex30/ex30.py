# Else and If

# Quick note from the last lesson. A colon indicates a "block" of code. We've seen these with functions and if statements.

people = 30
cars = 40
trucks = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."
	
if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
	

# Notes:

# elif functions like if, but it will only run when the if has evaluated to False.

# else does not take a boolean and will always run when the if and all elifs are False.

# QUESTION: What happens if multiple elif blocks are True?

# Python evaluates them sequentially, so it will only run the first one that evaluates to True.