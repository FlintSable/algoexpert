def past(h,m,s):
	mili = 0
	hours = h * (36*10**5)
	min = m * (6*10**4)
	sec = s * (1*10**3)
	return hours + min + sec + mili

# print(past(1,0,0))