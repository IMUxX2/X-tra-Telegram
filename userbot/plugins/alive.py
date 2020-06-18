"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you.""" 

import asyncio 

from telethon import events 

from telethon.tl.types import ChannelParticipantsAdmins 

from platform import uname 

from userbot import ALIVE_NAME 

from userbot.utils import admin_cmd 

 

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @IMUxXx" 

 

@command(outgoing=True, pattern="^.alive$") 

async def amireallyalive(alive): 

    """ For .alive command, check if the bot is running.  """ 

    await alive.edit("**اسم المطور ψ(｀Hayder ´)ψ**\n\n" 

                     "اصدار التنصيب: 6.9.0\n

لغة البوت: python\

Dev : @IMUxXx \n" 

                     "تم التنصيب بواسطة: [أيموڪــــس • 𝚒𝙼𝚄𝚇 •❥͜͡🇱🇷✿⇣ ](tg://user?id=713019532)\n" 

                     "يمكنك مراسلتي لاي خلل حاصل : استخدم امر .alive اذا اعتقدت ان البوت توقف!\n\nتطرح الملفات والاوامر الخاصة في هذه القناة !\n" 

                     f"حسابي الرسمي`: {DEFAULTUSER}\n" 

                     "[قناة البوت اشترك ليصلك كل ما هو جديد](https://t.me/z3iio)")

© 2020 GitHub, Inc.
