def build_user_index(users):
    """Поиск пользователя по ID"""
    #return {user["id"]: user for user in users}
    
    index_dict = {}

    for user in users:
        user_id = user["id"]  
        index_dict[user_id] = user
    
    return index_dict

    
    
    
    
users = [
    {"id": 1, "name": "Алексей", "rating": 4.8},
    {"id": 2, "name": "Мария", "rating": 4.2},
    {"id": 3, "name": "Иван", "rating": 3.5},
]
result = build_user_index(users)
#print(result)
# {
#   1: {"id": 1, "name": "Алексей", "rating": 4.8},
#   2: {"id": 2, "name": "Мария", "rating": 4.2},
#   3: {"id": 3, "name": "Иван", "rating": 3.5},
# }

# Теперь быстро найти по ID:
print(result[1])  # {"id": 2, "name": "Мария", "rating": 4.2}