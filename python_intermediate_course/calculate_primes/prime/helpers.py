
def is_prime(num):
	if num > 1:
		for n in range(2,num//2):
			if num % n != 0:
				continue
			else:
				return False
	return True


