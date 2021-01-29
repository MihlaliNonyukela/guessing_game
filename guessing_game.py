import random
random_num = random.randint(1,100)
num_trials = 0
while num_trials !=10:
	user_input = int(input("Please enter your guess: "))	# immediately transforming the input (string) into an integer
	
	num_trials = num_trials + 1
	if user_input == random_num:
		print("Congratulations! You have found the correct number in", num_trials, "trials!")
		random_num = random.randint(1,100)					# generating the next secret number to be discovered in the next round
		num_trials = 0										# resetting the counter of trials
		print("New guessing session starting now.")
		continue											# jumping back to the beginning of the loop
	else:			# the user has not found the right number, let's check if they have gone beyond the max number of trials
		if num_trials == 10: 
			print("Sorry, you failed to find the right number (", random_num, ") in 10 trials.")
			print("New guessing session starting now.")
			random_num = random.randint(1,100)				# generating the next secret number to be discovered in the next round
			num_trials = 0									# resetting the counter of trials
			continue
		else:	# not necessary to write the "else" here, due to the "continue" on the previous line, but there's nothing wrong with writing it
			if user_input > random_num:
				print("Go smaller")
			else:
				print("Go bigger")

# end of the program
print("Thanks for playing this game with me!")
