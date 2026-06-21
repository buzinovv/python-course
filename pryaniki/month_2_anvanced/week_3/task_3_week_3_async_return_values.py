import asyncio
import json

async def fetch_user_rating(user_name, delay):
    print(f"Проверяю рейтинг: {user_name}")
    await asyncio.sleep(delay)
    return {"name": user_name, "rating": 4}
async def main():
    results = await asyncio.gather(fetch_user_rating("Миша", 1),fetch_user_rating("Ваня", 2),fetch_user_rating("Соня", 3))
    for user in results:
        print(f"Пользователь: {user['name']}, Рейтинг: {user['rating']}")
    
    return results
        
        
results = asyncio.run(main())
#print(json.dumps(results, indent=2, ensure_ascii=False))
