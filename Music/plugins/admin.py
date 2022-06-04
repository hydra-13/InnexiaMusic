from pyrogram import Client 




# from. Yukki

@Client.on_message(command(["stop", "end"]) & other_filters)
async def stop_cmd(_, message): 
    if message.sender_chat:
        return await message.reply_text("you're an __Anonymous__ Admin !\n\n» revert back to user account.") 
    permission = "can_manage_voice_chats"
    m = await adminsOnly(permission, message)
    if m == 1:
        return
    checking = message.from_user.mention
    chat_id = message.chat.id
    if await is_active_chat(chat_id):
        try:
            clear(message.chat.id)
        except QueueEmpty:
            pass                        
        await remove_active_chat(chat_id)
        await Mikki.leave_group_call(message.chat.id)
        await message.reply_text("**Stopped Streaming...**") 
    else:
        return await message.reply_text("❌ **no music is currently playing**")
