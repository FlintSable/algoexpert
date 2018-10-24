import sys 

n = int(sys.argv[1])

def simple_multiplcation(number):
	if(number % 2 == 0):
		number *= 8
	elif(number % 2 != 0):
		number *= 9
	return number


print(simple_multiplcation(n))

