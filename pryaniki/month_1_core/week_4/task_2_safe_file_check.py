from pathlib import Path
import json

def check_and_load(filename):
    """Проверяет существование файла перед загрузкой."""
    file_path = Path(filename)  # превращаем строку в объект Path
    
    if file_path.exists():  # проверяем — True или False
        # Файл существует — загружаем данные
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    else:
        # Файла нет — сообщаем и возвращаем пустой список
        print(f"Файл {filename} не найден, создаю пустой список")
        return []


# Тест 1: файл существует
result = check_and_load("users.json")
print(json.dumps(result, indent=2, ensure_ascii=False))

# Тест 2: файл не существует
result = check_and_load("nonexistent.json")
print(result)