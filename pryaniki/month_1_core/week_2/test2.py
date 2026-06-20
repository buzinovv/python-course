def find_users_by_interests(users, target_interests):
    result = []
    target_set = set(target_interests)  # превращаем в множество для удобства
    #target_set = ["Python", "Gaming"]
    
    for user in users:
        user_interests = set(user["interests"])       
        if target_set <= user_interests: 
            result.append(user["name"])
    
    return result