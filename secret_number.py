#you guess a number the computer comes up with
#Ryan Lira May 27, 2022

import random

#the computer comes up with a number and the user guesses
def guess(x):
	# returns a number between 1 and x
	random_number = random.randint(1,x)
	guess = 0
	while(guess != random_number):
		guess = int(input(f'guess a number between 1 and {x}: '))
		if guess < random_number:
			print("sorry, too low. ")
		elif guess > random_number:
			print("sorry, too high.")
	print("YES FUCK YOU GUESSED MY NUMBER MY DICK IS SO FUCKING HARD RIGHT NOW!!")

#The user comes up with a number and the computer guesses
def computer_guess(x):
	low = 1
	high = x
	feedback = ''
	while feedback != 'c':
		guess = random.randint(low, high)
		feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1

	print(f'Yay! the computer guessed {guess}, corectly!')


which = input("computer guess (computer) or user guess (user)?")
if which == 'computer':
	computer_guess(100)
else:
	guess(100)
