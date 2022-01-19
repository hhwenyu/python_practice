## its a iterator
class Myrange:
	def __init__(self,start,end):
		self.value = start
		self.end = end

	def __iter__(self):
		return self
	
	def __next__(self):
		if self.value >= self.end:
			raise StopIteration
		current = self.value
		self.value += 1
		return current

## generator is an iterator but doesn't need to crate the dunder method __iter__ and __next__, which is much easier readable 
def My_range(start,end):
	while start < end:
		yield start
		start += 1



nums = Myrange(1,10)
#nums = My_range(1,10)
for num in nums:
	print(num)


i_nums = iter(nums)
while True:
        try:
                item = next(i_nums)
                print(item)
        except StopIteration:
                break
