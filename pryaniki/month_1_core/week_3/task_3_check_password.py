def check_password_strength(password):
    """Оценка надёжности пароля по длине и наличинию цифр."""
    password_length = len(password)
    character_password = 0
    for symbol in password:
        if symbol.isdigit():
            character_password += 1
    if password_length < 6:
        return "Слабый"
    elif password_length <= 10:
        return "Средний"
    elif password_length > 10 and character_password > 0:
        return "Сильный"
    else:
        return "Средний"        

user_password = input("Введите пароль: ")
user_password = check_password_strength(user_password)
print(user_password)