

def middleFinder(triList):
	sortedList = triList.copy()
	sortedList.sort()
	middleValue = sortedList[1]
	print(triList)
	for idx, val in enumerate(triList):
		if(val == middleValue):
			middleIndex = idx

	return middleIndex

print(middleFinder([2,3,1]))
