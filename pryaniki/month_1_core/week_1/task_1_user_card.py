user_name = input("Введите имя пользователя: ")
user_age = int(input("Введите возраст: "))
user_city = input("Введите город проживания: ")
user_rating = float(input("Введите рейтинг: "))
is_premium = input("Есть ли у вас премиум статус? Да/Нет: ").lower() == "да"

print(f"Пользователь: {user_name}\nВозраст: {user_age}\nГород: {user_city}\nРейтинг: {user_rating}\nПремиум: {'Да' if is_premium else 'Нет'}")

print(type(user_name))
print(type(user_age))
print(type(user_city))
print(type(user_rating))
print(type(is_premium))