
### iternator
'''
class Sentence:
	def __init__(self, input:str):
		self.input = input.split()
	def __iter__(self):
		return self
	def __next__(self):
		if self.input:
			return self.input.pop(0)
		else:
			raise StopIteration

'''

## generate an generator		
## solution 1
#def Sentence(input:str):
#	words = input.split(' ')
#	while words:
#		yield words.pop(0)

## solution 2 
def Sentence(sentence):
	yield from sentence.split()


my_sentence = Sentence('This is a test')		 
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
''''
my_sentence = Sentence('This is a test')
for word in my_sentence:
	print(word)
'''
