from pyrogram import Client, filters
from pytgcalls.exceptions import GroupCallNotFound
from Music import Mikki


@Client.on_message(filters.command("unmute"))

async def Unmute_stream(client, message):
    query = " ".join(message.command[1:])
    if query == "channel":
        chat_id = int(message.chat.title)
        type = "Channel"
    else:
        chat_id = message.chat.id
        type = "Group"
    try:
        await Mikki.unmute_stream(chat_id)
        await message.reply(f"**{type} stream Resumed**")
    except GroupCallNotFound:
        await message.reply("**Error:** GroupCall not found!")
