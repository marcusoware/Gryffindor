def check_parity(num):
	try:
		if num % 2 == 0:
			return f"even"
		else:
			return "odd"
	except ValueError:
		return "Error"
	
check = ((check_parity(input("enter a number: "))))
print(check)
	




