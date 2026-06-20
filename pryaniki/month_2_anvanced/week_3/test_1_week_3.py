import asyncio

async def make_coffee():
    print("Начинаю кофе")
    await asyncio.sleep(3)
    print("Кофе готов")

async def make_tea():
    print("Начинаю чай")
    await asyncio.sleep(2)
    print("Чай готов")

async def main():
    await asyncio.gather(make_coffee(), make_tea())  # ОБА запускаются СРАЗУ

asyncio.run(main())