import sys 

n = int(sys.argv[1]) + 1

def find(n):
	sum = 0
	for i in range(n):
		if(i%3 == 0) or (i%5 == 0):
			sum += i
	return sum

print(find(n))

