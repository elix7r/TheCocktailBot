import os
import json
import logging
from request_api import get_request
from name import ingredients
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('API_BOT')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def setup_bot_commands():
    bot_commands = [
        types.BotCommand(command="/help", description="Get info about me"),
        types.BotCommand(command="/random", description="set bot for a QnA task"),
    ]
    await bot.set_my_commands(bot_commands)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer(
        'Hi!\nI\'m CocktailBot!\nI help you cock a cocktail.\n'
        '/help - Show bot commands\n'
        '/random - Casual cocktail recipe'
    )


@dp.message_handler(commands=['random'])
async def random_cocktail(message: types.Message):
    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'

    get_request(url)

    with open('json_obj.json') as file:
        templates = json.load(file)

    await message.answer(templates['drinks'][0]['strDrink'] + ' 🍺')
    await message.answer('we\'re gonna need:')
    ingredients_ = ingredients()

    for ingredient in ingredients_:
        await message.answer(ingredient)

    await message.answer(templates['drinks'][0]['strInstructions'])

    await bot.send_photo(message.chat.id, types.InputFile.from_url(templates["drinks"][0]["strDrinkThumb"]))


@dp.message_handler()  # title search cocktail
async def search_cocktail(message: types.Message):
    try:
        cocktail_name = message.text
        URL = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail_name}'

        get_request(URL)

        with open('json_obj.json') as file:
            templates = json.load(file)

        await message.answer(templates['drinks'][0]['strDrink'] + ' 🍺')
        await message.answer(templates['drinks'][0]['strInstructions'])
        await bot.send_photo(message.chat.id, types.InputFile.from_url(templates["drinks"][0]["strDrinkThumb"]))
    except TypeError:
        await message.answer('Sorry, I does not find your request... 😭')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
