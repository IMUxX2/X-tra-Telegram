"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you.""" 
import asyncio 
from telethon import events 
from telethon.tl.types import ChannelParticipantsAdmins 
from platform import uname 
from userbot import ALIVE_NAME 
from userbot.utils import admin_cmd 
 
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot" 
 
@command(outgoing=True, pattern="^.alive$") 
async def amireallyalive(alive): 
    """ For .alive command, check if the bot is running.  """ 
    await alive.edit("**اسم المطور ψ(｀AhMaD´)ψ**\n\n" 
                     "اصدار التنصيب: 6.9.0\nلغة البوت: python\Dev AhMaDSaLiM: @HHMHHH\n" 
                     "تم التنصيب بواسطة: [⌯ AHMAD˼ 00:00 シ فوبيـــآإ ༒](tg://user?id=801023241)\n" 
                     "يمكنك مراسلتي لاي خلل حاصل : استخدم امر .alive اذا اعتقدت ان البوت توقف!\n\nتطرح الملفات والاوامر الخاصة في هذه القناة !\n" 
                     f"حسابي الرسمي: {DEFAULTUSER}\n" 
                     "[قناة البوت اشترك ليصلك كل ما هو جديد](https://t.me/cqcqq)")
© 2020 GitHub, Inc.
