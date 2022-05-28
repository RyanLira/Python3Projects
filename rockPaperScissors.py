#Ryan Lira May 27, 2022

#import random 
#you can pick a random item from a list with
#random.choice(['r','t','y'])




import random

def play():
	user = input("What's your choice? r' for rock, 'p' for paper, 's' for scissors\n")
	computer = random.choice(['r','p','s'])

	if user == computer:
		return 'tie'
# r beats s, s beats p, p beats r
	if is_win(user, computer):
		return 'You won!'

	return 'You Lost!'

def is_win(player, opponent):
	if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
	 or (player == 'p' and opponent == 'r'):
		return True

print(play())