def groups_per_user(group_dictionary):
    user_groups = {}

    for key in group_dictionary:
        print(key + "->")
        print(group_dictionary[key])
        for user in group_dictionary[key]:
            if(user not in user_groups):
                user_groups[user] = [key]                
            elif(user in user_groups):
                user_groups[user].append(key)

        #     print(group_dictionary[x][0])
        print("\n")
        # 
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
        "public": ["admin", "userB"],
        "administrator": ["admin"] }))