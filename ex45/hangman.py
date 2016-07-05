# Hangman

def hangmanGame():
	print "\n"

	from random import randint

	wordsFile = open('words.txt', 'r')

	words = []

	for line in wordsFile:
		words.append(line.strip())

	randomWord = words[randint(0,len(words)-1)]
	randomWordSecret = '_' * len(randomWord)

	randomWordAsSet = set()
	for ltr in randomWord:
		randomWordAsSet.add(ltr)

	randomWordAsList = []
	for ltr in randomWord:
		randomWordAsList.append(ltr)

	randomWordSecretAsList = []
	for ltr in randomWordSecret:
		randomWordSecretAsList.append(ltr)

	lettersToGuess = len(randomWordAsSet)

	incorrectGuesses = 0
	correctLetters = 0
	lettersGuessed = set()

	print "Welcome to Hangman! Your word has %d letters. You lose on your 7th incorrect guess. Press enter to continue." % len(randomWord)
	raw_input()	

	while incorrectGuesses <= 6 and correctLetters < lettersToGuess:
		print "\n"

		# Start each round by printing number of incorrect guesses, number of remaining guesses, and board
		print "You've made %d incorrect guesses. You have %d incorrect guesses remaining." % (incorrectGuesses, 6 - incorrectGuesses) 

		board = ""
		for ltr in randomWordSecretAsList:
			board = board + ltr + " "

		print board

		# Take a guess
		guess = raw_input("Guess a letter: ")

		# Check whether letter has already been guessed
		if guess in lettersGuessed:
			print "\n"
			print "You've already guessed %s, dummy." % guess ,
			raw_input("Press enter to continue.")
		# Now check whether letter is in the set
		elif guess in randomWordAsSet:
			randomWordAsSet.remove(guess) # remove the letter from the set
			lettersGuessed.add(guess) # add the letter to lettersGuessed set

			correctLetters += 1

			ind = 0
			for ltr in randomWordAsList:
				if ltr == guess:
					randomWordSecretAsList[ind] = ltr
					ind += 1
				else:
					ind += 1
		
		# Now check whether letter is in the set
		elif not (guess in randomWordAsSet):
			incorrectGuesses += 1
			lettersGuessed.add(guess)

		else:
			continue

	if correctLetters == lettersToGuess:
		print "You win! The word was %s." % randomWord
		return "win"
	elif correctLetters < lettersToGuess:
		print "You lose! The word was: %s." % randomWord
		return "lose"





