import asyncio

async def cook_dish(cnt, name, time_sec):
    # Готовим блюдо
    print(f"Забронировали столик - нужна сервировка {cnt}")
    print(f"Начинаем готовить: {name}")
    await asyncio.sleep(time_sec)
    print(f"Сервировка стола {cnt} готова")
    print(f"{name} готово!")
    return name, cnt
#
# async def table_setting(cnt, time_sec):
#     print(f"Забронировали место - нужна сервировка стола {cnt}! \n")
#     await asyncio.sleep(time_sec)
#     print(f"Сервировка стола {cnt} готова")
#     return cnt

async def main():
    # print("Бронь стола!!!")
    # answer = await asyncio.gather(
    #     table_setting('1', 1),
    #     table_setting('3', 2),
    #     table_setting('2', 3)
    # )
    # print("-- Столы готовы к прибытию гостей --")

    print("Заказ принят! \n")
    # Готовим 3 блюда параллельно
    results = await asyncio.gather(
        cook_dish(1, "Паста", 2),
        cook_dish(3, "Салат", 1),
        cook_dish(2, "Суп", 3)
    )

    print(f"Столы готовы, все блюда готовы: {results}")

if __name__ == "__main__":
    asyncio.run(main())