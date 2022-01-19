import random

pp = ["Allen", "Michael", "John", "Ben"]

print(pp)
#solution 1
#rand = random.randint(0,len(pp)-1)
#print(rand,pp.pop(rand))
#print(pp)

chosen_pp = random.choice(pp)
print(chosen_pp)
pp.remove(chosen_pp)
print(pp)
