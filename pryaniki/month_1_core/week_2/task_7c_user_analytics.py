#import json

def get_active_users(users):
    """Возвращает список имён активных пользователей"""
    result = []
    
    for user in users:
        if user["is_active"] == True:
            result.append(user["name"])
    return result
def get_user_summary(users):
    """Возвращает статистику по всем пользователям"""
    result = {
        "total_users": 0,
        "active_users": 0,
        "avg_rating": 0.0,
        "total_posts": 0,
        "most_posts": None,      
    }
      
    total_rating = 0
    
    for user in users:
        result["total_users"] += 1
        result["total_posts"] += user["posts"]
        total_rating += user["rating"]
        if user["is_active"] == True:
            result["active_users"] += 1
        
    result["avg_rating"] = round(total_rating / result["total_users"], 2)
    
    user_with_most_posts = max(users, key=lambda user: user["posts"])
    result["most_posts"] = user_with_most_posts["name"]
    
    return result  
def find_users_by_interests(users, target_interests):
    """Возвращает имена пользователей с указанным фильтром интересов"""
    
    result = []
    target_set = set(target_interests)
      
    for user in users:
        user_interests = set(user["interests"])
        if target_set <= user_interests:
            result.append(user["name"])
        
        
    
    return result
    
users = [
    {
        "id": 1,
        "name": "Алексей",
        "rating": 4.8,
        "posts": 15,
        "interests": ["Python", "AI", "Gaming"],
        "is_active": True
    },
    {
        "id": 2,
        "name": "Мария",
        "rating": 3.2,
        "posts": 5,
        "interests": ["Python", "Web"],
        "is_active": False
    },
    {
        "id": 3,
        "name": "Иван",
        "rating": 4.5,
        "posts": 22,
        "interests": ["DevOps", "Python", "Gaming"],
        "is_active": True
    },
]

result = get_active_users(users)
print(result)

result = get_user_summary(users)
print(result)
#print(json.dumps(result, ensure_ascii=False, indent=2))

result = find_users_by_interests(users, ["Python", "Gaming"])
print(result)