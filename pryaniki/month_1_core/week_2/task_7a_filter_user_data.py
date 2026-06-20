def filter_user_data(user, exclude_keys):
    """Возвращает словарь без указанных ключей"""
    result = {}
    for field, value in user.items():
        if field not in exclude_keys:
            result[field] = value
    return result
        
    
user = {
    "name": "Алексей",
    "email": "alex@mail.com",
    "password": "secret123",  # конфиденциально!
    "age": 28,
    "phone": "+7-999-123-45-67",  # конфиденциально!
}

result = filter_user_data(user, ["password", "phone", "email"])
print(result)
# {"name": "Алексей", "email": "alex@mail.com", "age": 28}