def filter_users_by_rating(users, min_rating):
    """Фильтрует пользователей по минимальному рейтингу."""
    #eligible_users = []
    #for user in users:
    #    if user["rating"] >= min_rating:
    #        eligible_users.append(user["rating"])
    #return eligible_users
    return [user["name"] for user in users if user["rating"] >= min_rating]
    
    
    
users = [
    {"name": "Алексей", "rating": 4.8},
    {"name": "Мария", "rating": 3.2},
    {"name": "Иван", "rating": 4.5},
    {"name": "Анна", "rating": 2.1},
]
result = filter_users_by_rating(users, 4.0)
print(result)