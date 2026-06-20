def format_user_tag(full_name, city):
    """Формирует тег пользователя вида @имя_город."""
    full_name = full_name.split()
    city = city.split()
    user_tag = (full_name[0]+"_"+"_".join(city)).lower()
    return user_tag

full_name = input("Введите полное имя: ")
city = input("Введите город: ")
username = format_user_tag(full_name,city)
print(f"@{username}")