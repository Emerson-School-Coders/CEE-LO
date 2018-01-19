#imports
from random import randint
from time import sleep
import sys

#stores which roll users are on
on_roll = {
	"user": 0,
	"computer": 0
}

#dice textures
dice_text = {
	1: " -------\n|       |\n|   0   |\n|       |\n -------",
	2: " -------\n| 0     |\n|       |\n|     0 |\n -------",
	3: " -------\n| 0     |\n|   0   |\n|     0 |\n -------",
	4: " -------\n| 0   0 |\n|       |\n| 0   0 |\n -------",
	5: " -------\n| 0   0 |\n|   0   |\n| 0   0 |\n -------",
	6: " -------\n| 0   0 |\n| 0   0 |\n| 0   0 |\n -------"
}

#stores rolls of players
rolled_nums = {
	"user": [],
	"computer": []
}

#stores score of player
user_score = {
	"user": False,
	"computer": False
}

#sets who should be rolling
allowed_to_roll = True

#rolls numbers
def roll_it(user):
	for i in range(3):
		roll = randint(1, 6)
		rolled_nums[user].append(roll)
		
#checks for numbers
def match_check(rolls):
    #Tells what score to return
	score = False
	
	#Tells if there's a match
	match = False
	
	#checks for instawin/instalose
	for num1 in rolls:
		for num2 in rolls:
			for num3 in rolls:
				if num1 == 1 and num2 == 2 and num3 == 3:
					match = True
					score = 0
				elif num1 == 4 and num2 == 5 and num3 == 6:
					match = True
					score = 13
					
	#checks if all three nums are the same
	if rolls[0] == rolls[1] and rolls[1] == rolls[2]:
		match = True
		score = rolls[0] + 6
	
	#checks for "numbers"
	#finds matched numbers
	seen = set()
	for number in rolls:
		if number in seen:
			for num in rolls:
				if num != number:
					match = True
					score = num
		else:
			seen.add(number)
	
	#returns whether there was a match and what the score was
	return [score, match]
	
#decides which dice should be printed
def dice_check(numbers):
	for n in numbers:
		print(dice_text[n]) ; sleep(0.8)

#makes text print slower
def print_slowly(text):
	for l in text:
		if l != "	":
			print(l, end = "")
			sys.stdout.flush()
			sleep(0.07)
		else:
			sleep(1)
			
#gets user to press enter to proceed
def press_enter(text):
	get_input = input(text)
	return get_input

#responds to rolls
def respond(user):
	s = match_check(rolled_nums[user])[0]
	m = match_check(rolled_nums[user])[1]
	
	match = False
	
	if m == True:
		user_score[user] = s
		if user == "user":
			print_slowly("You got a match.	\n")
			match = True
		else:
			print_slowly("I got a match.	\n")
			match = True
	else:
		if user == "user":
			print_slowly("You didn't get a match.	\n")
			match = False
		else:
			print_slowly("I didn't get a match.	\n")
			match = False
	
	return match
			
def roll(user):
	if user == "user":
		if on_roll[user] == 0:
			print_slowly("Press enter to roll...")
		else:
			print_slowly("Press enter to roll again...")
		press_enter("")
	else:
		if on_roll[user] == 0:
			print_slowly("Now I will roll...	\n")
		else:
			print_slowly("I will roll again...	\n")
	rolled_nums[user] = []
	roll_it(user)
	on_roll[user] += 1
	dice_check(rolled_nums[user])

def user_roll():
	while True:
		roll("user")
		if respond("user") == True:
			break
			
def ye_function():	
	on_roll["user"] = 0
	on_roll["computer"] = 0
	
	y_or_n = press_enter("")
	
	while True:
		if "y" in y_or_n:
			user_roll()
			break
		elif "n" in y_or_n:
			print_slowly("Ok.	 See you later then...")
			exit()
		else:
			print_slowly('That was NOT the requested input!	\nPlease type "y" or "n". ')
			y_or_n = press_enter("")
		
			
def computer_roll():
	while True:
		if user_score["user"] == 13:
			print_slowly("You got a 4, 5, and 6!	\nThere is no way I can win.	\nGood game!	\nWould you like to play again? (y/n) ")
			ye_function()
			
		roll("computer")
		if respond("computer") == True:
			if user_score["user"] > user_score["computer"]:
				print_slowly("You beat me!	\nGood game.	\nWould you like to play again? (y/n) ")
				ye_function()
				
			else:
				print_slowly("I won!	\nThanks for playing.	\nWould you like to play again? (y/n) ")
				ye_function()
	
#logo
print("  _____     _____    _____          __        ______  \n /  __  \  |   __|  |   __|        |  |      /  __  \ \n|  /  \_/  |  |_    |  |_    ___   |  |     |  /  \  |\n|  |   _   |   _|   |   _|  |___|  |  |     | |    | |\n|  \__/ \  |  |__   |  |__         |  |___  |  \__/  |\n \______/  |_____|  |_____|        |______|  \______/ \n")
press_enter("	       Press enter to start...\n")

print_slowly("Hello user!	\n")
while True:
	user_roll()
	computer_roll()
	
	
			
	
