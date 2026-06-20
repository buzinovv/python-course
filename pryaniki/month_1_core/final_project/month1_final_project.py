import json
from pathlib import Path
from collections import Counter

def save_users(users, filename):
    """Сохраняет пользователей в файл"""
    with open(filename, "w") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)
     
def load_users(filename):
    """Выгружает пользователей из файла"""
    file_path = Path(filename)
    
    if not file_path.exists():
        return []
    
    with open(filename, "r") as f:
        loaded = json.load(f)
    return loaded

def add_user(users, name, age, interests):
    """Добавляет нового пользователя с автоматическим ID."""

    if len(users) == 0:
        new_id = 1  # если список пустой — первый ID = 1
    else:
        max_id = max(user["id"] for user in users)
        new_id = max_id + 1
    
    new_user = {
        "id": new_id,
        "name": name,
        "age": age,
        "interests": interests
    }
    
    users.append(new_user)
    
    return users

def show_all_users(users):
    """Выводит всех пользователей."""
    print("=== ПОЛЬЗОВАТЕЛИ ===")
    for user in users: 
        interests_text = ", ".join(user["interests"])
        print(f"ID: {user['id']}, Имя: {user['name']}, Возраст: {user['age']}, Интересы: {interests_text}")
    
def find_user_by_interest(users, interest):
    """Возвращает пользователей с указанным интересом"""
    return [user for user in users if interest in user["interests"]]
    
def get_statistics(users):
    result = {
        "total_users": 0,
        "avg_age": 0,
        "top_interests": None
    }
    
    total_age = 0
    
    all_interests = []
    
    for user in users:
        result["total_users"] += 1
        total_age += user["age"]
        all_interests.extend(user["interests"])
    
    counter = Counter(all_interests)
    top_3 = counter.most_common(3)
    result["top_interests"] = [item[0] for item in top_3]
    result["avg_age"] = total_age / result["total_users"]
    
    return result


def main():
    users = load_users("month_1_core/final_project/users.json")
    
    while True:
        print("\n=== МЕНЕДЖЕР ПОЛЬЗОВАТЕЛЕЙ ===")
        print("1. Добавить пользователя")
        print("2. Показать всех пользователей")
        print("3. Найти пользователей по интересу")
        print("4. Показать статистику")
        print("5. Найти пользователя по ID")
        print("6. Выйти")
        
        choice = input("Введите действие: ")
        
        if choice == "1":
            name = input("Введите имя: ")
            age = int(input("Введите возраст: "))
            interests = []
            
            choise_interests = input("Хотите добавить интересы? Да/Нет ")
            if choise_interests == "Да": 
                while True:
                    print("Введите слово (Стоп) если закончили! ")          
                    add_interests = input("Введите интересы пользователя: ")
                    if add_interests.lower() == "стоп":
                        print("Завершаем ввод...")
                        break
                    else:
                        interests.append(add_interests)
                        print("Интерес добавлен! ")  
            users = add_user(users, name, age, interests)
            save_users(users, "month_1_core/final_project/users.json")
            print("Пользователь добавлен!")
        elif choice == "2":
            show_all_users(users)
        elif choice == "3":
            interest = input("Введите интересы пользователя:")
            result = find_user_by_interest(users, interest)
            print("=== Пользователи с похожими интересами ===")
            print(json.dumps(result, indent=2, ensure_ascii=False))
        elif choice == "4":
            result = get_statistics(users)
            print("Общая статистика пользователей")
            print(json.dumps(result, indent=2, ensure_ascii=False))
        elif choice == "5":
            user_id = int(input("Введите ID пользователя: "))
            user_info = []
            for i in users:
                if user_id == i["id"]:
                    user_info.append(i)
            print(f"=== Информация о пользователя по ID: {user_id} ===")
            print(f"ID: {user_info[0]['id']}, Name: {user_info[0]['name']}, Age: {user_info[0]['age']}, Interests: {user_info[0]['interests']}")
                
        elif choice == "6":
            print("Выход из меню.")
            break
        else:
            print("Такого действия нет!")

main()


