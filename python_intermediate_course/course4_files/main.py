## write 

with open('alpha.txt','r') as f_in:
	with open('echo.txt','a') as f_out:
		for line in f_in:
			items = line.strip('\n').split(' ')
			#print(items)
			#for item in items:
			#	print(item)
			f_out.write(' '.join(items))## join a list by ' '
			f_out.write('\n')

	#f.write('\n')
	


## read multiple files from a directory
'''
import os

files = os.listdir(os.curdir)

for single_file in files:
	print(single_file)
	if single_file.endswith('.txt'):
		with open(single_file) as f:
			print(f.read())
'''

## solution 2: context manager
'''
with open('alpha.txt') as f:
	
	single_line = f.readline()
	print(f'header: {single_line}')
	f.seek(0) ## re-set the pointer back to row 0
	for line in f:
		print(line,end='')



	#lines = f.readlines()
	#for line in lines:
	#	print(line,end = '')


	#read entire file/content once
	#content = f.read()
	#print(f.read())



print(f.closed)
print(f.mode)
print(f.name)
'''
## solution 1: regular way to read the file
'''
f = open('alpha.txt') ## default is read, so you can ignore 'r'
content = f.read()
print(content)
f.close()

'''




