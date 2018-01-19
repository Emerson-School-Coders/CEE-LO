#scoring
scoring = {
	
}
user_score = 0
computer_score = 0

#import randint
from random import randint

#stores rolls
rolls = {
	"computer": [],
	"user": []
}

#counts rolls
roll_counter = 0

#turns off rolling when computer has a number.
rolling = True

#code for computer's rolls

#loop to roll dice
while rolling == True:
	while roll_counter < 3:
		roll = randint(1, 6)
		rolls["computer"].append(roll)
		#checks for instawin/instalose
		for numa in rolls["computer"]:
			if numa == 1:
				for numb in rolls["computer"]:
					if numb == 2:
						for numc in rolls["computer"]:
							if numc == 3:
								computer_score = 0
								rolling = False
			elif numa == 4:
				for numb in rolls["computer"]:
					if numb == 5:
						for numc in rolls["computer"]:
							if numc == 6:
								computer_score = 0
								rolling = False
		#thing for checking if two numbers in rolls["computer"] are equal
		seen = set()
		for number in rolls["computer"]:
			if number in seen:
				#fixes the issue, idk y
				rolls["computer"].remove(number)
				rolls["computer"].remove(number)
			else:
				seen.add(number)
		roll_counter += 1
	if len(rolls["computer"]) == 1:
		#makes your number from ^^ your score
		computer_score = rolls["computer"][0]
		rolling = False
print(rolls)
print(computer_score)