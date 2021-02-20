def solution(l):
    ordered_sort_int = sorted(l, reverse=True)
    
    if(sum(ordered_sort_int) % 3 == 0):
        ordered_sort_str = [ str(i) for i in ordered_sort_int]
        return int("".join(ordered_sort_str))
        
    while(sum(ordered_sort_int) % 3 != 0):
        changed_list = [0] # defining this here 

        for x, val in reversed(list(enumerate(ordered_sort_int))):
            reduced_list = [i for i in (ordered_sort_int)]
            reduced_list.pop(x)
            reduced_list_str = [ str(i) for i in reduced_list ]
            changed_list_str = [ str(j) for j in changed_list ]
            print("reduced list: {}".format(reduced_list))
            if((len(ordered_sort_int) == 1) & sum(ordered_sort_int) % 3 != 0):
                print("len reduced list: ".format(len(reduced_list)))
                return 0
            elif((sum(reduced_list) % 3 == 0) & ((int("".join(reduced_list_str)) > (int("".join(changed_list_str)))))):
                # if we never get here then the value of changed_ist will be [0]
                changed_list = reduced_list

        print("changed list: {}".format(changed_list))
        # this is what gets it out of the while loop
        ordered_sort_int = changed_list
        print("len reduced list: {} ".format(ordered_sort_int))

    # print("len reduced list: ".format(ordered_sort_int))

    ordered_sort_str = [str(i) for i in ordered_sort_int]
    return int("".join(ordered_sort_str))

# print(solution([8,5,7,3,2,1]))

# print(solution([3, 1, 4, 1]))
# print(solution([3, 1, 4, 1, 5, 9]))
# print(solution([3, 1, 4, 1, 5, 0, 0, 0]))
# print(solution([1, 4, 4]))
# print(solution([4, 1, 4]))
# print(solution([1, 5]))
# print(solution([4, 5]))
# print(solution([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]))
print(solution([3, 1, 1]))




            # if(len(ordered_sort_int) == 1 & sum(ordered_sort_int) % 3 != 0):
            #     return 0