# Guess the Number

def guessNumber():
	print "\n"
	
	from random import randint

	num = randint(1,100)
	
	print "\"I have selected a random number between 1 and 100 inclusive,\" said the Zombie. You get 6 guesses, and I will tell you whether your guess is high or low."
	
	guess_num = 1
	guess = None
	
	while guess_num <= 6 and guess != num:
		guess = int(raw_input("> "))
		
		if guess < num:
			print "Too low!"
		elif guess > num:
			print "Too high!"
		else:
			break
		
		print "You've used %d of your guesses. Guess again!" % guess_num
		guess_num += 1
	
	if guess == num:
		print "Correct! My number was %d." % num
		return "win"
	else:
		print "My number is %d. You failed to guess the right number." % num
		return "lose"