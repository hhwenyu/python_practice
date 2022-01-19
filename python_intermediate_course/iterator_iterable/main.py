# nums is list which is iterable 
nums = [1,2,3]

# dir(nums) with __iter__; then num.__iter__ is iterator

#i_nums = nums.__iter__
#i_nums = iter(nums)
#print(i_nums,dir(i_nums),next(i_nums),next(i_nums),next(i_nums),next(i_nums))



## how the for loop loops the list nums
nums = [1,2,3]
for i in nums:
	print(i)
## backend
i_nums = iter(nums)
while True:
	try:
		item = next(i_nums)
		print(item)
	except StopIteration:
		break
