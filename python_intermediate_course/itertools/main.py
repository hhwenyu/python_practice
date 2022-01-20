## https://docs.python.org/3/library/itertools.html
import itertools
## https://pypi.org/project/more-itertools/
from more_itertools import take
counter = itertools.count(start=5, step=5)
data = [100,200,300,400]
daily_data = list(zip(itertools.count(),data))
print(daily_data)

for item in take(3,data):
	print('take',item)




counter = itertools.cycle(('on','off'))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


counter = itertools.repeat(2,times=3)

squares = map(lambda x : x**2, range(10))
#squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))


squares = itertools.starmap(pow, [(0,2),(1,2),(2,2)])
print(list(squares))


letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3]
selectors = [1,0,0,1]
for item in itertools.compress(letters,selectors):
	print(item)

for item in filter(lambda x : x<2,numbers):
	print(item)
