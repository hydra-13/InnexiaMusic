from pyrogram import Client, filters
from pytgcalls.exceptions import GroupCallNotFound
from Music import Mikki


@Client.on_message(filters.command(["end", "stop"]))

async def end(client, message):
    query = " ".join(message.command[1:])
    if query == "channel":
        chat_id = int(message.chat.title)
        type = "Channel"
    else:
        chat_id = message.chat.id
        type = "Group"
    try:
        await Mikki.leave_group_call(chat_id)
        await message.reply(f"**{type} stream Ended!**")
    except GroupCallNotFound:
        await message.reply("**Error:** GroupCall not found!")
