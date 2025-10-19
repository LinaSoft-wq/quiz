from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

import buttons

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.start_quiz_button]
        [buttons.help_button]

    ],
    resize_keyboard=True,
)

inline_keyboard = InlineKeyboardMarkup(
 [
 [buttons._inline_button],
 [buttons._inline_button],
 ],
)

