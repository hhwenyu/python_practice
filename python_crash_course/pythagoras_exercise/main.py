# write a function that will accept three parameters
# print to the user if the given three numbers applies the pythagoras formula
## a ** 2 + b ** 2 = c ** 2

lt = input("Please enter three numbers!")

num = lt.split(',')
print(len(num))

print(f"You entered {num}")
a,b,c = map(int,num)
def pythagoras( a, b, c):
	left_hand = a ** 2 + b ** 2
	right_hand = c ** 2
	if left_hand == right_hand:
		print(f"The combindation of {a}, {b}, and {c} supports pythagoras law!")
	else:
		print(f"The combindation of {a}, {b}, and {c} don't follow pythagoras law!")


pythagoras(a,b,c)
