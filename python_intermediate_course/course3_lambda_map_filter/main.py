
#def square(num):
#	return num ** 2

## lambda
#square = lambda num : num ** 2

#result_of_five = square(5)
#print(result_of_five)

#multiply = lambda x,y: x * y
#print(multiply(10,5))



##map(): executes a specified function for each item in an iterable

#def even_numbers(list_of_numbers):
#	even = []
#	for number in list_of_numbers:
#		if number % 2 == 0:
#			even.append(number)
#	return even
#
#print(even_numbers(range(1,10)))


def even_number(number):
	if number % 2 == 0:
		return number

## use map, the first argument is the function without (), and the input argument of that function
even_digits = map(even_number, range(1,10))
even_digits_filtered = filter(None,(even_digits))
print(type(even_digits),list(even_digits_filtered))





