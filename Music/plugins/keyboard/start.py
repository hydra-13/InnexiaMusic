# this file is under @TeamRexoma
# © 2022 GNU LICENSE 3 @Trex_2_0 // @piroXpower // @SakaOp
# © Kang With credits

def start_markup(_, user.id):
    buttons = [
                [
                  InlineKeyboardButton(text="Help And Commands", callback="help"), 
                ], 
                [
                  InlineKeyboardButton(text="Support", callback_data="support"), 
                  InlineKeyboardButton(text="Owner", user_id=OWNER) 
                ], 
                [
                  InlineKeyboardButton(text="Assistant", user_id=ASSISTANT), 
                  InlineKeyboardButton(text="Source Code", url=f"{source}") 
                ], 
                [
                  InlineKeyboardButton(text="Add Me To Your Group", url=f"t.me/{bn}/startgroup=true") 
                ]
             ]
            return buttons

def help_markup(_, user.id):
    buttons = [ 
               [
                 InlineKeyboardButton(text="Play", callback_data="play"), 
                 InlineKeyboardButton(text="Admin", callback_data="admin") 
               ], 
               [
                 InlineKeyboardButton(text="Sudo/Own", callback_data="sudo"), 
                 InlineKeyboardButton(text="Extra", callback_data="extra") 
               ], 
               [
                 InlineKeyboardButton(text="Close", callback_data="close") 
               ]
              ]
           return buttons
def close_markup(_, user.id):
    buttons = [
                 [ 
                    InlineKeyboardButton(text="Close", callback_data="close")
                 ]
              ]
           return buttons 
