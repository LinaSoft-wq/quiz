from pyrogram.types import KeyboardButton, InlineKeyboardButton
from pyrogram import emoji

back_button = KeyboardButton(f"{emoji.BACK_ARROW} Назад")

help_button = KeyboardButton(f"{emoji.WHITE_QUESTION_MARK} Помощь")

start_quiz_button = KeyboardButton(f"Начать квиз")

print()