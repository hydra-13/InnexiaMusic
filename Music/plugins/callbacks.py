import yt_dlp
from Music.Client.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup)
from Music.plugins.keyboard.play import play_markup, next_markup, menu_markup, panel_markup

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("menu")) 
async def menu(_, query: CallbackQuery):
     a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    await query.edit_message_text(
        "**Welcome To Menu Of MusicBot :**",
        reply_markup=InlineKeyboardMarkup(mdnu_markup), 
   ) 

@Client.on_callback_query(filters.regex("panel")) 
async def panel(_, query: CallbackQuery):
     a = await _.get_chat_member(query.message.chat.id, query.from_user.id) 
    await query.edit_message_text(
        "**Here  Is Control Panel Of Music**", 
        reply_markup=InlineKeyboardMarkup(panel_markup), 
    ) 

# @Client.on_callback_query(filters.regex("next")) 
# async def next(_, query: CallbackQuery):
#    a = await_.get_chat_member(query.message.chat.id, query.from_user.id) 
#   await query.edit_message_text(
 #      "**Here  Is Control Panel Of Music**",
#       reply_markup=InlineKeyboardButton(next_markup), 
#     )

@Client.on_callback_query(filters.regex("play"))
async def on_resumeTrue(_, CallbackQuery):  
    a = await app.get_chat_member(CallbackQuery.message.chat.id , CallbackQuery.from_user.id)
    if not a.can_manage_voice_chats:
        return await CallbackQuery.answer("You must be admin with permissions:\n\n❌ » manage_video_chats", show_alert=True)
    chat_id = CallbackQuery.message.chat.id
    if await is_active_chat(chat_id):
        if await is_music_playing(chat_id):
            await CallbackQuery.answer("❌ no music is paused", show_alert=True)
            return    
        else:
            await music_on(chat_id)
            await Mikki.resume_stream(chat_id)
            await CallbackQuery.answer("streaming resumed")
            await CallbackQuery.edit_message_text(f"▶ music playback has resumed", reply_markup=menu_markup)
    else:
        await CallbackQuery.answer(f"❌ no music is currently playing", show_alert=True)
   

