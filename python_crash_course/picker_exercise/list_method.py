people = ["Allen", "Michael", 10, "John", False , "Ben"]
print(people.index(10))
print(people[1::2])
people.append("Kurt")
print(people)
people.extend(["Hua","Jim"])

print(people)

people.remove(10)
print(people)

people.remove(False)
people.sort()
print(people)
