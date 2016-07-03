# What If

people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"
	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs."
	
	
# STUDY DRILLS

# (1) What do you think the if does to the code under it?

# if evaluates the boolean, and if it is True, it executes the code beneath.

# (2) Why does the code under if need to be indented?

# All indented lines after the if boolean: statement are only evaluated if boolean is True. When a line is not indented, the if statement ends.