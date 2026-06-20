import asyncio

async def handle_user(user_name, delay):
    print(f"Начинаю обработку: {user_name}")
    await asyncio.sleep(delay)
    print(f"Готово: {user_name}")
    
async def main():
    await asyncio.gather(handle_user("Миша", 2),handle_user("Ваня", 3),handle_user("Соня", 3))
    
asyncio.run(main())