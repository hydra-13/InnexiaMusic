import asyncio
from pytgcalls import idle
from Music import LOG_CHAT
from Music.Client.tgcalls import Mikki, Bot, sex 

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await Bot.start()
    await Bot.send_message(
                           LOG_CHAT,
                           "<b>InnexiaMusic Bot Successfully Started!</b>"
    ), 

    print("[INFO]: STARTING PYTGCALLS CLIENT")

    await Mikki.start()
    await idle()
    await sex.send_message(
                            LOGGER,
                            "<b>Innexia Music Assistant Successfully Started!</b>"
    ), 
    await sex.join_chat("RexomaSupport"), 
    await sex.join_chat("RexomaUpdate") 
    print("[INFO]: STOPPING BOT & USERBOT")    
    await Bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot()) 
