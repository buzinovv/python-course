import json

users = [
    {"id": 1, "name": "Алексей"},
    {"id": 2, "name": "Мария"},
]

# Сохранить:
with open("users.json", "w") as f:
    json.dump(users, f, indent=2, ensure_ascii=False)
# После этой строки на диске появится файл users.json

# Загрузить:
with open("users.json", "r") as f:
    loaded = json.load(f)

print(loaded)
# [{"id": 1, "name": "Алексей"}, {"id": 2, "name": "Мария"}]