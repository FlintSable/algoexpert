def solution(l):
    print("sum of list: {}".format(sum(l)))
    print("%3: {}".format(sum(l) % 3))
    if(sum(l) % 3 == 0):
        return int("".join([ str(i) for i in sorted(l, reverse=True)] ))
    elif((len(l) == 1) & sum(l) % 3 != 0):
        return 0
    elif((sum(l) % 3) in l):
        # remove the first best digit if it makes % 3 == 0
        l.pop(l.index(sum(l) % 3))
        print(sum(l) % 3)
        return int("".join([ str(i) for i in sorted(l, reverse=True)] ))

    # eval best case to remove
    ordered_sort_int = sorted(l, reverse=True)
    changed_list = ordered_sort_int
    # for x, val in reversed(list(enumerate(ordered_sort_int))):
    for x, val in list(enumerate(ordered_sort_int)):
        reduced_list = [i for i in (ordered_sort_int)]
        reduced_list.pop(x)
        reduced_list_str = [ str(i) for i in reduced_list ]
        changed_list_str = [ str(j) for j in changed_list ]

        if((sum(reduced_list) % 3 == 0)):
            print("meets guide")
            changed_list = reduced_list

    if(sum(changed_list) % 3 == 0):
        return int("".join([ str(i) for i in sorted(changed_list, reverse=True)] ))
    elif(ordered_sort_int == changed_list):
        print(((sum(ordered_sort_int) % 3 == 2)) & (sum(ordered_sort_int[-2:]) % 2 == 0))
        if(((sum(ordered_sort_int) % 3 == 2)) & (sum(ordered_sort_int[-2:]) % 2 == 0)):
            ordered_sort_int = ordered_sort_int[:-2]
            return int("".join([ str(i) for i in sorted(ordered_sort_int, reverse=True)] ))

        return int("".join([ str(i) for i in sorted(changed_list, reverse=True)] ))

    # eval an option to remove multiple items to make the number % 3 == 0
    return l

# print(solution([3, 1, 4, 1, 5, 9]))
# print(solution([3, 1, 4, 1]))
# print(solution([3, 1, 4, 1, 2, 5, 9]))
# print(solution([3,4,2,5,9]))
# print(solution([1, 4, 4]))
# print(solution([4, 1, 4]))
# print(solution([1, 5]))
# print(solution([4, 5]))
print(solution([3, 1, 1]))
# print(solution([0]))
# print(solution([7]))

# print(solution([1,1,4]))


print(solution([7, 7, 7, 7]))
