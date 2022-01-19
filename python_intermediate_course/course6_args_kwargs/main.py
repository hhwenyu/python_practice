
current_year = 2020

class Person:
	def __init__(self, name, **kwargs):
		self.name = name
		self.yob = kwargs.get('yob')	
	
		#print(kwargs.items())		
		
	def get_age(self):
		if self.yob:
			return current_year - self.yob


p1 = Person(name = "John" )
print(p1.get_age())


## **kwargs is when you don't know the keyword nor size; kwargs by default is the dict()
'''
current_year = 2020
def get_ages(**kwargs):
	for k,v in kwargs.items():
		print(f"The parm is {k}, and the value is {v}")

get_ages(name='Jim', yob=1996)
'''
## * is the situation when you don't know the size/len; default is iterable list
'''
current_year = 2020
def get_age(*yobs): # *yob is an iterable with unknown size/len
	for yob in yobs:
		print(f'the age for {yob} is {current_year - yob}')


get_age(1998,1996,2000)
'''
