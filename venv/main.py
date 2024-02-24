import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.utils.markdown import hbold

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6403293465:AAEk8q5PZNzhwKh4FwPhfMoKMjVqm_GuDt8"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


# --- REPLY MENU MARKUP ---
def r_main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Про нас🤭")],
            [KeyboardButton(text="Під-меню"), KeyboardButton(text="Інлайн меню")]
        ],
        resize_keyboard=True
    )
    return kb


def r_sub_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Item1")],
            [KeyboardButton(text="Item2"), KeyboardButton(text="Item3")],
            [KeyboardButton(text="Item4"), KeyboardButton(text="Item5")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )
    return kb


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I'm live!", reply_markup=r_sub_menu())


@dp.message()
async def reply_kb_handler(message: types.Message) -> None:
    msg = message.text
    cid = message.from_user.id
    if msg == "Про нас🤭":
        # await bot.send_message(cid, "Some Text")
        text = ("Люблю відео ігри і котів")
        await message.answer(text)
    elif msg == "Під-меню":
        await message.answer("Ви перейшли в під меню!", reply_markup= r_sub_menu() )
    elif msg == "Інлайн меню":
        await message.answer("Ви перейшли в інлайн меню!")


async def main() -> None:
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())