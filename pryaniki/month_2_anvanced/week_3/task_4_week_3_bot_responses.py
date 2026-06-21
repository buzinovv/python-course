import asyncio

async def process_message(user_name, processing_time):
    print(f"Обрабатываю сообщение от {user_name}")
    await asyncio.sleep(processing_time)
    return {"user": user_name, "time": processing_time}
async def main():
    dict_users_message = await asyncio.gather(
        process_message("Алексей", 2),
        process_message("Мария", 1),
        process_message("Иван", 3),
        process_message("Анна", 1),
        process_message("Пётр", 2)
    )
    return dict_users_message
users = asyncio.run(main())
total_time = 0
for user in users:
    total_time += user["time"]
fastest_user = min(users, key=lambda user: user["time"])
print (f"Самый быстрый: {fastest_user['user']}, общее время обработки всех: {total_time} сек")
    
