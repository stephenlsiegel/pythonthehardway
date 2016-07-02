# Functions and Variables

# One point to realize: the variables in your function are NOT connected to the variables in your script. Here's an example:

# This creates the function cheese_and_crackers, which takes two numeric arguments and prints out 4 lines.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket\n"

# This calls cheese_and_crackers with arguments 20 and 30
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# This creates two variables which are then passed in as arguments to cheese_and_crackers
print "Or we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This does math to calculate the arguments to cheese_and_crackers
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# This does math with variables as the arguments to cheese_and_crackers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

