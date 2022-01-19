## elevator program
# we should receive an input always, user may write a number of not; if the user writes a number, the program should write out the floor number, otherwise if the user writes out, then the program should stop the execution
seen = ''
while True: ## the True and False in the if statement should always captialize
	floor_num = input("Please enter a number: ")
	if not floor_num.lower() == 'out':
		if floor_num == seen:
			print("You have already in this floor!")
		else:	
			print(f"You are on {floor_num} floor")
			seen = floor_num
	else:
		print("You are leaving the program")
		break 
