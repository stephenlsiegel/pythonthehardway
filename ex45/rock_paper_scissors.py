# Rock-Paper-Scissors

# rock beats scissors
# scissors beats paper
# paper beats rock

from random import randint

comp_dict = {1:"rock", 2:"paper", 3:"scissors"}

player_record = [0,0]

print "Welcome to Rock-Paper-Scissors. You must beat the computer 5 times before it beats you 5 times to advance."

while player_record[0] < 5 and player_record[1] < 5:
	
	comp_play = comp_dict[randint(1,3)]
	
	human_play = raw_input("Your choice > ")
	
	if human_play == comp_play:
		print "Computer plays %s." % comp_play
		print "----- Draw! Play again. -----"
	
	elif (human_play == "rock" and comp_play == "paper") or (human_play == "paper" and comp_play == "scissors") or (human_play == "scissors" and comp_play == "rock"):
		print "Computer plays %s." % comp_play
		print "----- Computer wins! -----"
		player_record[1] += 1
		print "Your record is now %d wins and %d losses." % (player_record[0], player_record[1])
	
	elif (human_play == "rock" and comp_play == "scissors") or (human_play == "paper" and comp_play == "rock") or (human_play == "scissors" and comp_play == "paper"):
		print "Computer plays %s." % comp_play
		print "----- You win! -----"
		player_record[0] += 1
		print "Your record is now %d wins and %d losses." % (player_record[0], player_record[1])
	
	else:
		print "Error. Please enter \"rock\", \"paper\", or \"scissors\" without the quotes."
		
if player_record[0] >= 5:
	print "You won 5 games before the computer. Congratulations, you advance!"
elif player_record[1] >= 5:
	print "You lost 5 games before beating the computer 5 times. You die."
else:
	print "Error: the loop broke before player had won or lost 5 games. Player record is %d wins and %d losses." % (player_record[0], player_record[1])