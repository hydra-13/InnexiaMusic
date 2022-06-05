from pyrogram import Client, filters
from Music import Mikki


@Client.on_message(filters.command("volume"))

async def change_volume(client, message):
    range = message.command[1]
    chat_id = message.chat.id
    try:
        await Mikki.change_volume_call(chat_id, volume=int(range))
        await message.reply(f"**Volume changed to:** `{range}%`")
    except Exception as e:
        await message.reply(f"**Error:** {e}")
