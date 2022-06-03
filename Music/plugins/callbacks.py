import yt_dlp
from Music.Client.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup)
from Music.plugins.keyboard import play_markup

@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("menu")) 
async def menu(_, query: CallbackQuery):
     a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    await query.edit_message_text(
        "**Welcome To Menu Of MusicBot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Panel🎛", callback_data="panel"),
                    InlineKeyboardButton("Lyrics🔎", callback_data="lyrics"),
                ],
                [
                    InlineKeyboardButton ("Support⛓", callback="back"),          
                    InlineKeyboardButton("🗑 Close", callback_data="close")
                ],
           ]
        ),
    )

@Client.on_callback_query(filters.regex("panel")) 
async def panel(_, query: CallbackQuery):
     a = await _.get_chat_member(query.message.chat.id, query.from_user.id) 
    await query.edit_message_text(
        "**Here  Is Control Panel Of Music**", 
        reply_markup=InlineKeyboardMarkup(
            [
                 [
                     InlineKeyboardButton("⏸", callback_data="pause"),
                     InlineKeyboardButton("⏹", callback_data="stop"), 
                     InlineKeyboardButton("▶️", callback_data="play"), 
                 ], 
                 [
                     InlineKeyboardButton("🔇", callback_data="mute"), 
                     InlineKeyboardButton("🔊", callback_data="unmute"),
                 ], 
                 [
                     InlineKeyboardButton("Next", callback_data="next"), 
                     InlineKeyboardButton("🔙", callback_data="menu"), 
                 ], 
                 [
                     InlineKeyboardButton("🗑Close", callbackdata="close")
                 ]
            ]
       ),
    ) 
@Client.on_callback_query(filters.regex("next")) 
async def next(_, query: CallbackQuery):
    a = await_.get_chat_member(query.message.chat.id, query.from_user.id) 
   await query.edit_message_text(
       "**Here  Is Control Panel Of Music**",
       reply_markup=InlineKeyboardButton(next_board) 
     )


