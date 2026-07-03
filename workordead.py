import asyncio
import random  # Эта штука нужна, чтобы выбирать случайную фразу
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Сюда мы вставим длинный токен от @BotFather
TOKEN = "8790694389:AAGGlE3YfJyI4_aqzibDqZVLUTAw9zl7AIQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 5 разных вариантов текста, как ты её любишь (можешь изменить тексты внутри кавычек на свои)
LOVE_PHRASES = [
    "я люблю тебя больше жизни леликс!!! ❤️",
    "Ты моё самое главное счастье, Лёли! 🥰",
    "Люблю тебя сильнее с каждой секундой! 💞",
    "Ты у меня самая лучшая и неповторимая! 😘",
    "Моё сердце бьется только для тебя, любимая! 💓"
]

# Срабатывает ОДИН РАЗ, когда она нажимает кнопку "Старт" (команда /start)
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("привет лели я тебя люблю ты помнишь?")

# Срабатывает на ВСЕ дальнейшие сообщения в диалоге
@dp.message()
async def echo_love(message: types.Message):
    # Выбираем случайную фразу из нашего списка выше
    random_phrase = random.choice(LOVE_PHRASES)
    await message.answer(random_phrase)

async def main():
    print("Бот успешно запущен и ждет сообщений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
