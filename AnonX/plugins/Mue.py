from strings import get_command
from pyrogram import Client, filters, idle

from pyrogram.enums import ChatMemberStatus

from typing import List, Union

from AnonX.utils.database import *

from AnonX import app

from pyrogram import filters

  

  

  

mutes = []

@app.on_message(command("كتم") & filters.group)

async def mute(app,message):

   member = await message.chat.get_member(message.from_user.id)

   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:

     return await message.reply("الادمن بس الي يستخدمو الامر")

   else:

     if not message.reply_to_message:

       return await message.reply("• اعمل ريب الاول ع الي هتكتمو")

     member = await message.chat.get_member(message.reply_to_message.from_user.id)

     if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:

       return await message.reply("مينفعش اكتم ادمن")

     chat_id = str(message.chat.id)

     user_id = str(message.reply_to_message.from_user.id)

     x = "{}@{}".format(chat_id,user_id)

     if x in mutes:

       return await message.reply("مهو مكتوم اصلا")

     else:

       mutes.append(x)

       return await message.reply("{} اتكتم بواسطة {} .".format(message.reply_to_message.from_user.mention,message.from_user.mention))

       

@app.on_message(command("الغاء الكتم") & filters.group)

async def unmute(app,message):

   member = await message.chat.get_member(message.from_user.id)

   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:

     return await message.reply("الادمن بس الي يستخدمو الامر")

   else:

     if not message.reply_to_message:

       return await message.reply("• اعمل ريب علي هتلغي كتمو")

     member = await message.chat.get_member(message.reply_to_message.from_user.id)

     if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:

       return await message.reply("مينفعش تنفذ الامر ع ادمن")

     chat_id = str(message.chat.id)

     user_id = str(message.reply_to_message.from_user.id)

     x = "{}@{}".format(chat_id,user_id)

     if not x in mutes:

       return await message.reply("مهو مش مكتوم اصلا يسطا")

     else:

       mutes.remove(x)

       return await message.reply("{} تم الغاء كتمه بواسطة {} .".format(message.reply_to_message.from_user.mention,message.from_user.mention))

@app.on_message(command("المكتومين") & filters.group)

def get_dmute(app, message):

   if len(mutes) == 0: return

   member = message.chat.get_member(message.from_user.id)

   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:

     return message.reply("الادمن بس الي يقدرو يستخدمو الامر")

   ch = message.chat.id

   c = 0

   text = "• Mutes list in this chat :\n\n"

   for a in mutes:

     chat_id = int(a.split("@")[0])

     user_id = int(a.split("@")[1])

     if chat_id == ch:

        user = app.get_users(user_id)

        text += f"- {user.mention}\n"

        c += 1

   if c == 0: return message.reply("مفيش مكتومين هنا")

   message.reply(f"{text}")

@app.on_message(filters.group)

def del_msg(_,m):

   if m.from_user:

     chat_id = str(m.chat.id)

     user_id = str(m.from_user.id)

     x = "{}@{}".format(chat_id,user_id)

   for a in mutes:

     if a == x: 

       m.delete()

       break

