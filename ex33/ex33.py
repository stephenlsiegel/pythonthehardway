# While Loops

# A while-loop will keep executing the block of code under it as long as the boolean expression is True.

# Rules to follow:
	# 1. Use while-loops sparingly (because of infinite loop issue). Usually for-loop is better.
	# 2. Review your while-loops, make sure boolean will become False at some point.
	# 3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.

i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num