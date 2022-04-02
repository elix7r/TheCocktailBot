import os
import requests
import json
import logging
from request_api import get_request

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('API_BOT')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands=['random'])
async def random_cocktail(message: types.Message):
    url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'

    get_request(url)

    with open('json_obj.json') as file:
        templates = json.load(file)
    # print(type(templates))
    # print(templates["drinks"][0]["strDrinkThumb"])
    # print(templates['drinks']['strDrinkThumb'])

    await message.answer(templates["drinks"][0]["strDrinkThumb"])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
