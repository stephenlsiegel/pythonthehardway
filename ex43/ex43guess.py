from random import randint

code = "%d%d%d" % (randint(0,9), randint(0,9), randint(0,9))
guesses = 0
guess = raw_input("My guess is > ")

print "Guess a number between 0 and 999. You get 10 guesses."

while guesses < 10 and guess != code:
	print "Wrong!"
	
	if int(guess) > int(code):
		print "Your guess was too high!"
	else:
		print "Your guess was too low!"
		
	guesses += 1
	print "You've used %d of 10 guesses." % (guesses)
	guess = raw_input("My new guess is > ")

if guess == code:
	print "Correct!"
	print "You guessed %s and the code is %s!" % (guess, code)
else:
	print "You've used all your guesses without getting the right answer."
	print "You lose."
	print "The code was %s." % (code) 