def find_common_interests(users_list):
    """Поиск общих интересов пользователей"""
    common_interests = set(users_list[0]["interests"])
    
    for i in range(1,len(users_list)):
        user_interests = set(users_list[i]["interests"])
        common_interests = common_interests & user_interests
        
    result = sorted(common_interests)
    return result
    
    
    
users_list = [
    {"name": "Алексей", "interests": ["Python", "AI", "Games"]},
    {"name": "Мария", "interests": ["Python", "Web", "AI"]},
    {"name": "Иван", "interests": ["Python", "DevOps", "AI"]},
]
result = find_common_interests(users_list)
print(result)