def filter_users_by_gpu(laptops, gpu):
    """Фильтрует ноутбуки по заданному фильтру."""
    #eligible_users = []
    #for user in users:
    #    if user["rating"] >= min_rating:
    #        eligible_users.append(user["rating"])
    #return eligible_users
    return [laptop["name"] for laptop in laptops if laptop["gpu"] == gpu]
    
    
    
laptops = [
    {"name": "Ноутбук ACER", "gpu": "RTX 5080"},
    {"name": "Ноутбук LENOVO", "gpu": "RTX 5080"},
    {"name": "Ноутбук MacBook Neo", "gpu": "RTX 5080"},
    {"name": "Ноутбук Xiaomi", "gpu": "RTX 5060"},
]
result = filter_users_by_gpu(laptops, "RTX 5060")
print(result)