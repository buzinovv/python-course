import json

def save_users(users, filename):
    """Сохраняет список пользователей в новый JSON файл"""
    with open(filename, "w") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)
        
def load_users(filename):
    """Загружает список пользователей из JSON файла"""
    with open(filename, "r") as f:
        loaded = json.load(f)
    return loaded       
            
    
users = [
    {"id": 1, "name": "Алексей", "rating": 4.8},
    {"id": 2, "name": "Мария", "rating": 4.2},
    {"id": 3, "name": "Иван", "rating": 3.5},
]

save_users(users, "users.json")
loaded = load_users("users.json")
print(json.dumps(loaded, indent=2, ensure_ascii=False))