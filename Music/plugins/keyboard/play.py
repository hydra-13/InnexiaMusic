import random
from pyrogram.types import InlineKeyboardButton

def play_markup(_, chat_id):
    buttons = [
        [           
            InlineKeyboardButton(
                text="Menu",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Close",
                callback_data="close"
            )
        ],
    ]
    return buttons


def next_markup(_, chat_id):
    buttons = [
         [
            InlineKeyboardButton(
                 text="15%", 
                 callback_data="vol1"), 
            InlineKeyboardButton(
                 text="50%", 
                 callback_data="vol2"), 
         ], 
         [
            InlineKeyboardButton(
                 text="75%", 
                 callback_query="vol3"), 
            InlineKeyboardButton(
                  text="100%", 
                  callback_query="vol4")
         ], 
         [
            InlineKeyboardButton(
                  text="Close",
                  callback_data="close") 
         ], 
      ]
