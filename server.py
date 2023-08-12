import os
import json
import logging
from util import get_json_file
from ingredients import get_cocktail_ingredients
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("API_TELEGRAM_BOT")
RANDOM_COCKTAIL_URI = "https://www.thecocktaildb.com/api/json/v1/1/random.php"

logging.basicConfig(level=logging.INFO)
telegram_bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(telegram_bot)


@dispatcher.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer(
        "Hi!\nI'm CocktailBot!\nI help you cock a cocktail.\n"
        "Send me the name of the cocktail and I'll find it 🍸\n"
        "/help - Show bot commands\n"
        "/random - Casual cocktail recipe"
    )


@dispatcher.message_handler(commands=["random"])
async def random_cocktail(message: types.Message):
    get_json_file(RANDOM_COCKTAIL_URI)

    with open("json_obj.json") as file:
        templates = json.load(file)

    await message.answer(templates["drinks"][0]["strDrink"] + " 🍺")
    await message.answer("we're gonna need:")

    ingredients: list = get_cocktail_ingredients()

    for ingredient in ingredients:
        await message.answer(ingredient)

    await message.answer(templates["drinks"][0]["strInstructions"])

    await telegram_bot.send_photo(
        message.chat.id,
        types.InputFile.from_url(templates["drinks"][0]["strDrinkThumb"]),
    )


@dispatcher.message_handler()  # title search cocktail
async def search_cocktail(message: types.Message):
    try:
        cocktail_name = message.text
        URL = (
            f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail_name}"
        )

        get_json_file(URL)  # get json file

        with open("json_obj.json") as file:
            templates = json.load(file)

        await message.answer(templates["drinks"][0]["strDrink"] + " 🍺")

        await message.answer("we're gonna need:")
        ingredients_ = get_cocktail_ingredients()

        for ingredient in ingredients_:
            await message.answer(ingredient)

        await message.answer(templates["drinks"][0]["strInstructions"])
        await telegram_bot.send_photo(
            message.chat.id,
            types.InputFile.from_url(templates["drinks"][0]["strDrinkThumb"]),
        )
    except TypeError:
        await message.answer("Sorry, I doesn't find your request... 😭")


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)
