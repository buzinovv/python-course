def user_stats(users):
    """Вычисляет статистику по списку пользователей"""
    all_stats = {
        "total_users": 0,
        "avg_rating": 0.0,
        "total_posts": 0,
        "top_user": None,            
    }
    
    rating_sum = 0
    
    for user in users:
        all_stats["total_users"] += 1
        all_stats["total_posts"] += user["posts"]
        rating_sum += user["rating"]
    
    all_stats["avg_rating"] = round(rating_sum / all_stats["total_users"], 2)
    
    all_stats["top_user"] = max(users, key=lambda user: user["rating"])
    
    return all_stats
        
    
    
    
users = [
    {"name": "Алексей", "rating": 4.8, "posts": 15},
    {"name": "Мария", "rating": 4.2, "posts": 8},
    {"name": "Иван", "rating": 3.5, "posts": 22},
]
result = user_stats(users)
print(result)