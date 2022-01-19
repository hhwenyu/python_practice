
student_name = "john doe"
is_snowing = False 
is_raining = False
if not (is_snowing or is_raining): 
	print(f"""
	Hi {student_name.title()}:
	Today weather is nice, you should come school today.
	""")
else:
	print(f"""
	Hi {student_name.title()}:
	The weather today is not so good, please stay at home.
	""")
