from itertools import combinations

def solution(l):
    l.sort(reverse=True) # sort the in decending order
    for i in reversed(range(1, len(l) + 1)): # loop through the list from the smallest numbers
        print("what is this for: {}".format(i)) # this first loop setup the index for the next loop

        for tup_variant in combinations(l, i): # combinations creates variations of lists with i values in it
            if sum(tup_variant) % 3 == 0: 
                # return int("".join(map(str, tup_variant))) # this line joins all the items in the tuple 
                # but first it maps to each item str
                return int("".join([ str(i) for i in tup_variant] ))
                
    return 0


print(solution([3, 1, 4, 1, 5, 9]))
# print(solution([3, 1, 4, 1]))
# print(solution([3, 1, 4, 1, 2, 5, 9]))
# print(solution([3,4,2,5,9]))
# print(solution([1, 4, 4]))
# print(solution([4, 1, 4]))
# print(solution([1, 5]))
# print(solution([4, 5]))
# print(solution([0]))
# print(solution([7]))

# print(solution([1,1,4]))


# print(solution([7, 7, 7, 7]))
print(solution([3, 1, 1]))
