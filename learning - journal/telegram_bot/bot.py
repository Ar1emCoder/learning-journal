import asyncio
from aiogram import Bot, Dispatcher, types
from recipes import find_recipes, get_babushka_recipes

# Вставь свой токен
API_TOKEN = '8428805523:AAHFD5N7ePL98q9Fjuc-RgBWf0x7TeP79DI'

# Создаём объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message()
async def echo(message: types.Message):
    if message.text == '/start':
        await message.answer("Привет! Я бот-шеф. Напиши /help, чтобы узнать, что я умею.")
    elif message.text == '/help':
        await message.answer(
            "Я помогу приготовить еду из того, что есть в холодильнике.\n"
            "Просто напиши продукты через запятую, например:\n"
            "картошка, лук, яйца"
        )
    elif message.text == '/info':
        await message.answer(
            "Я бот, меня написал начинающий программист - Ar1emCoder"
        )
    elif ',' in message.text:
        products = []
        for p in message.text.split(','):
            clean = p.strip().lower()
            products.append(clean)
        found = find_recipes(products)

        if found:
            answer = "Можно приготовить:\n\n"
            for r in found:
                answer += f"- {r['name']}\n"
            answer += "\nНапиши название рецепта, чтобы увидеть инструкцию."
        else:
            answer = "Ничего не нашёл. Попробуйте другие продукты или добавь ещё."

        await message.answer(answer)
    elif message.text == '/babushka':
        babushka_recipes = get_babushka_recipes()
        if babushka_recipes:
            answer = "👵 Бабушкины рецепты:\n\n"
            for r in babushka_recipes:
                answer += f"• {r['name']}\n"
            await message.answer(answer)
        else:
            await message.answer('👵 Пока нет бабушкиных рецептов. Добавлю скоро!')
    else:
        await message.answer(f"Ты написал: {message.text}")

# Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())rm bot_old.py