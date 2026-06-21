import asyncio

async def load_profile(user, delay):
    print("Загружаю профиль...")
    await asyncio.sleep(delay)
    print("Профиль загружен")
async def load_orders(user, delay):
    print("Загружаю историю заказов...")
    await asyncio.sleep(delay)
    print("История загружена")
async def load_recommendations(user, delay):
    print("Загружаю рекомендации...")
    await asyncio.sleep(delay)
    print("Рекомендации загружены")
async def main():
    await asyncio.gather(load_profile("Миша", 1), load_orders("Миша", 2), load_recommendations("Миша", 3))
asyncio.run(main())