def solution(l):
    ordered_sort_int = sorted(l, reverse=True)

    if (sum(ordered_sort_int)%3 == 0):
        ordered_sort_str = [ str(i) for i in ordered_sort_int]
        return int("".join(ordered_sort_str))

    # digit remover while loop
    while(sum(ordered_sort_int) % 3 != 0):
        # if the remainder is a number in the list remove it
        changed_list = [0]
        for x, val in reversed(list(enumerate(ordered_sort_int))):
            # include everything but the current item
            print("\ndon't include: {} {}".format(x, val))
            reduced_list = [i for i in (ordered_sort_int)]
            reduced_list.pop(x)
            # print("reduced list: {}".format(reduced_list))
            reduced_list_str = [ str(i) for i in reduced_list]
            print(reduced_list_str)
            changed_list_str = [ str(j) for j in changed_list]
            print(changed_list_str)
            if((sum(reduced_list)%3 == 0) & ((int("".join(reduced_list_str)) > (int("".join(changed_list_str)))))):
                changed_list = reduced_list
                print("changed list: {}".format(changed_list))
        ordered_sort_int = changed_list
    
    print("The code: {}".format(ordered_sort_int))
        


# new_random_list = [3, 1, 4, 1, 5, 9]
# new_random_list = [3, 1, 4, 1, 5, 5]
# solution(new_random_list)


new_random_list = [3, 1, 4, 1]
print(solution(new_random_list))
