import json
from aiogram import Bot, Dispatcher, executor, types
from main import check_news_update
from aiogram.dispatcher.filters import Text

bot = Bot(token='')
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Все новости", "Последние 5 новостей"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Лента новостей", reply_markup=keyboard)

@dp.message_handler(Text(equals = "Все новости"))
async def get_all_news(message: types.Message):
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    for k, v in news_dict.items():
        news = f"{v['article_date']}\n" \
            f"{v['article_url']}"

        await message.answer(news)


@dp.message_handler(Text(equals = "Последние 5 новостей"))
async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len (fresh_news) >= 1:
        for k, v in news_dict.items():
            news = f"{v['article_date']}\n" \
                   f"{v['article_url']}"
            await message.answer(news)
    else:
        await message("новых новостей нет")

if __name__ == '__main__':
    executor.start_polling(dp)