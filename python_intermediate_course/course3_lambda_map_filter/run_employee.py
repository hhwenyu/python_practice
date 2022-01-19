from employees import employees

#print(employees)

get_older_40 = lambda emp: emp['age'] > 40 
print(list(filter(get_older_40,employees)))



## solution 1: lambda, map and filter

get_older_40 = lambda emp: emp['name'] if  emp['age'] > 40 else None
print(get_older_40)

emp_over_40 = map(get_older_40,employees)

print(type(filter(None,emp_over_40)))

### solution with some functions
#def get_older_40(employees_list):
#	to_return_list = []
#	for employee in employees_list:
#		if employee['age'] > 40:
#			to_return_list.append(employee['name'])	
#
#	return to_return_list
#
#over_40 = get_older_40(employees)
#print(over_40)
