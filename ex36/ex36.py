# Designing and Debugging

# Rules for If-Statements
	# 1. Every if-statement must have an else.
	# 2. If this else should never run because it doesn't make sense, then you must use a die function in the else that prints out an error message and dies, just like the last exercise. This will find many errors.
	# 3. Never nest if-statements more than two deep and always try to do them one deep.
	# 4. Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences. Put blank lines before and after.
	# 5. Your boolean tests should be simple. If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.
	
# Rules for Loops
	# 1. Use a while-loop only to loop forever, and that means probably never. This only applies to Python; other languages are different.
	# 2. Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over.
	
# The best way to debug a program is to use print to print out the values of variables at points in the program to see where they go wrong.

from sys import exit

def start():
	print "There are 2 outs, the game is tied 5 to 5 in the bottom of the 9th inning. The bases are loaded."
	print "Aroldis Chapman is pitching for the Yankees."
	print ""
	raw_input("> Press enter to continue.") 
	
	posey()
	
def posey():
	print "Buster Posey is hitting for the Giants."
	count = [0,0]
	pitch_num = 1
	buster_hitting = True
	print "The count is %d balls and %d strikes." % (count[0],count[1])
	
	while buster_hitting:
		if count[0] >= 4:
			print "Buster Posey walks. The winning runs scores! Game over."
			exit(0)
		elif count[1] >= 3:
			print "Buster Posey strikes out. We head to extra innings!"
			exit(0)
		else:
			print "Here comes a pitch."
	
		if pitch_num % 3 > 0:
			print "Chapman throws a curveball."
			pitch = "curve"
			choice = raw_input("What does Buster Posey do? (swing, take) > ")
		elif pitch_num % 3 == 0:
			print "Chapman throws a fastball."
			pitch = "fast"
			choice = raw_input("What does Buster Posey do? (swing, take) > ")
		else:
			print "Program has thrown an error in the buster_hitting loop."
		
		if not (choice in ['swing', 'take']):
			print "Buster Posey hits a pop up and the game goes into extra innings."
			buster_hitting = False
		elif pitch == "curve" and choice == "swing":
			print "Posey swings and misses at the curveball."
			count[1] += 1
			print "The count is %d balls and %d strikes." % (count[0],count[1])
			pitch_num += 1
		elif pitch == "curve" and choice == "take":
			print "Posey takes a curveball low for a ball."
			count[0] += 1
			print "The count is %d balls and %d strikes." % (count[0],count[1])
			pitch_num += 1
		elif pitch == "fast" and choice == "swing":
			print "Posey hits a home run and the Giants win 9-5."
			exit(0)
		elif pitch == "fast" and choice == "take":
			print "Posey takes a fastball for a strike."
			count[1] += 1
			print "The count is %d balls and %d strikes." % (count[0],count[1])
			pitch_num += 1
		else:
			print "Your program has thrown an error."

start()