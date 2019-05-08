# count true vales in array

sheepBucket = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]


def count_sheeps(arrayOfSheeps):
    count = 0
    for sheep in arrayOfSheeps:
        if sheep == True:
            count += 1
    return count

print(count_sheeps(sheepBucket))