def solution(l):
    ordered_sort_int = sorted(l, reverse=True)
    
    if(sum(ordered_sort_int) % 3 == 0):
        ordered_sort_str = [ str(i) for i in ordered_sort_int]
        return int("".join(ordered_sort_str))
        
    while(sum(ordered_sort_int) % 3 != 0):
        changed_list = [0]
        for x, val in reversed(list(enumerate(ordered_sort_int))):
            reduced_list = [i for i in (ordered_sort_int)]
            reduced_list.pop(x)
            reduced_list_str = [ str(i) for i in reduced_list ]
            changed_list_str = [ str(j) for j in changed_list ]
            if((len(ordered_sort_int) == 1) & sum(ordered_sort_int) % 3 != 0):
                return 0
            elif((sum(reduced_list) % 3 == 0) & ((int("".join(reduced_list_str)) > (int("".join(changed_list_str)))))):
                changed_list = reduced_list
        ordered_sort_int = changed_list

        

    ordered_sort_str = [str(i) for i in ordered_sort_int]
    return int("".join(ordered_sort_str))

# print(solution([8,5,7,3,2,1]))

print(solution([1, 9]))

            # if(len(ordered_sort_int) == 1 & sum(ordered_sort_int) % 3 != 0):
            #     return 0