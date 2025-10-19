from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import Poll
import config
import buttons
import keyboards
from custom_filters import button_filter

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="my_cool_bot",
)

@bot.on_message(filters=filters.command("start") | button_filter(buttons.back_button))
async def start_command(client: Client, message: Message):
    await message.reply("Привет!",
        reply_markup = keyboards.main_keyboard
    )

@bot.on_message(filters=filters.command("help") | button_filter(buttons.back_button))
async def help(client: Client, message: Message):
    await message.reply("Краткое руководство",
        reply_markup = keyboards.main_keyboard
    )


bot.run()

