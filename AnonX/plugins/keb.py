from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram.errors import PeerIdInvalid
from asyncio import get_event_loop
import asyncio, os
from pyrogram import Client
from asBASE import asJSON
from config import BOT_TOKEN
from AnonX import app 




db = asJSON("as.json")




SUDORS = [5881570606, 5190136458] 

bot_id = BOT_TOKEN.split(":")[0]




def add_new_user(user_id):
	if is_user(user_id):
		return
	db.sadd(f"botusers&{bot_id}", user_id)
def is_user(user_id):
	try:
		users = get_users()
		if user_id in users:
			return True
		return False
	except:
		return False
def get_users():
	try:
		return db.get(f"botusers&{bot_id}")["set"]
	except:
		return []

def users_backup():
	text = ""
	for user in get_users():
		text += f"{user}\n"
	with open("users.txt", "w+") as f:
		f.write(text)
	return "users.txt"

def del_user(user_id: int):
	if not is_user(user_id):
		return False
	db.srem(f"botusers{bot_id}", user_id)
	return True




@app.on_message(filters.command("start") & filters.private)
async def new_user(bot, msg):
	if not is_user(msg.from_user.id):
		add_new_user(msg.from_user.id)
		text = f"""
• دخل عضو جديد للبوت

• الاسم : {msg.from_user.first_name}
• منشن : {msg.from_user.mention}
• الايدي : {msg.from_user.id}
		"""
		reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"• عدد الاعضاء: {len(get_users())}", callback_data= "users")]])
		if len(SUDORS) > 0:
			for user_id in SUDORS:
				await bot.send_message(int(user_id), text, reply_markup=reply_markup)
		else:
			await bot.send_message(int(SUDORS[0]), text, reply_markup=reply_markup)
@app.on_message(filters.command("tom") & filters.private, group=1)
async def admins(bot, msg):
	if msg.from_user.id in SUDORS:
		reply_markup = ReplyKeyboardMarkup([
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺")],
			[("• قسم التواصل بالبوت •")],
			[("• قسم الإذاعة •"),("• قسم الإحصائيات •")],
			[("• اخفاء الكيبورد •")],
			[("• المبرمجين •"),("• السورس •")],
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺)")]])
		await msg.reply(f"• اهلا عزيزي المطور {msg.from_user.mention}", reply_markup=reply_markup, quote=True)



@app.on_message(filters.regex("• رجوع •") & filters.private, group=1)
async def admins(bot, msg):
	if msg.from_user.id in SUDORS:
		reply_markup = ReplyKeyboardMarkup([
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺")],
			[("• قسم التواصل بالبوت •")],
			[("• قسم الإذاعة •"),("• قسم الإحصائيات •")],
			[("• اخفاء الكيبورد •")],
			[("• المبرمجين •"),("• السورس •")],
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺)")]])
		await msg.reply(f"• اهلا عزيزي المطور {msg.from_user.mention}", reply_markup=reply_markup, quote=True)
		

@app.on_message(filters.regex("• قسم التواصل بالبوت •") & filters.private, group=1)
async def admins(bot, msg):
	if msg.from_user.id in SUDORS:
		reply_markup = ReplyKeyboardMarkup([
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺")],
			[("• تفعيل التواصل •"), ("• تعطيل التواصل •")],
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺")],
			[("• الغاء •"),("• رجوع •")],
			[("• اخفاء الكيبورد •")],
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺)")]])
		await msg.reply(f"• اهلا عزيزي المطور {msg.from_user.mention}", reply_markup=reply_markup, quote=True)





@app.on_message(filters.regex("• قسم الإذاعة •") & filters.private, group=1)
async def admins(bot, msg):
	if msg.from_user.id in SUDORS:
		reply_markup = ReplyKeyboardMarkup([
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺")],
			[("• اذاعه •")],
			[("• اذاعه بالتوجيه •"),("• اذاعه بالتثبيت •")],
			[("• الغاء •"),("• رجوع •")],
			[("• اخفاء الكيبورد •")],
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺)")]])
		await msg.reply(f"• اهلا عزيزي المطور {msg.from_user.mention}", reply_markup=reply_markup, quote=True)



@app.on_message(filters.regex("• قسم الإحصائيات •") & filters.private, group=1)
async def admins(bot, msg):
	if msg.from_user.id in SUDORS:
		reply_markup = ReplyKeyboardMarkup([
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺")],
			[("• الاحصائيات •")],
			[("• جلب النسخة الاحتياطية •"), ("• رفع النسخة الاحتياطية •")],
			[("• الغاء •"),("• رجوع •")],
			[("• اخفاء الكيبورد •")],
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺)")]])
		await msg.reply(f"• اهلا عزيزي المطور {msg.from_user.mention}", reply_markup=reply_markup, quote=True)



@app.on_message(filters.regex("• المبرمجين •") & filters.private, group=1)
async def admins(bot, msg):
	if msg.from_user.id in SUDORS:
		reply_markup = ReplyKeyboardMarkup([
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺")],
			[("• TOM •"), ("• ZEIN •")],
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺")],
			[("• JOK •"),("• LENDA •")],
			[("• رجوع •")],
			[("⩹━★⊷━⌞ 𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍 ⌝━⊶★━⩺)")]])
		await msg.reply(f"• اهلا عزيزي المطور {msg.from_user.mention}", reply_markup=reply_markup, quote=True)




@app.on_message(filters.regex("• السورس •") & filters.private, group=1)
async def admins(bot, msg):
	if msg.from_user.id in SUDORS:
		reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᧁ𝘳ꪮꪊρ ", url=f"https://t.me/SORS0Coo"),
                ],
                [
                    InlineKeyboardButton(
                    "⌞𓏺َِ𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 𓏺َِ𝙎َِ𝙀َِ𝙕َِ𝘼َِ𝙍⌝", url=f"https://t.me/UIU_II"),
                ],
            ])

		await msg.reply_photo(photo=f"https://graph.org/file/99f04dad2ddfb82c1b87d.jpg",caption=f"""𝘛𝘏𝘌 𝘉𝘌𝘚𝘛 𝘚𝘖𝘜𝘙𝘊𝘌 𝘖𝘕 𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔""", reply_markup=reply_markup)






@app.on_message(filters.regex("• TOM •") & filters.private, group=1)
async def yas(client, message):
    usr = await client.get_chat("DEV_TOM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(filters.regex("• ZEIN •") & filters.private, group=1)
async def yas(client, message):
    usr = await client.get_chat("devpokemon")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )





@app.on_message(filters.regex("• JOK •") & filters.private, group=1)
async def yas(client, message):
    usr = await client.get_chat("G_O_OZ")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )




@app.on_message(filters.regex("• LENDA •") & filters.private, group=1)
async def yas(client, message):
    usr = await client.get_chat("ELA_V1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )




@app.on_message(filters.text & filters.private, group=2)
async def cmd(bot, msg):
	if msg.from_user.id in SUDORS:
		if msg.text == "• الغاء •":
			await msg.reply("• تم الغاء كل العمليات", quote=True)
			db.delete(f"{msg.from_user.id}:fbroadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:pinbroadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:broadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:users_up:{bot_id}")
		if msg.text == "• اخفاء الكيبورد •":
			await msg.reply("• تم اخفاء الكيبورد ارسل /start لعرضه مره اخري", reply_markup=ReplyKeyboardRemove(selective=True), quote=True)
		if msg.text == "• الاحصائيات •":
			await msg.reply(f"• عدد الاعضاء: {len(get_users())}\n• عدد المشرفين: {len(SUDORS)}", quote=True)
		if msg.text == "• تفعيل التواصل •":
			if not db.get(f"{msg.from_user.id}:twasl:{bot_id}"):
				await msg.reply("• تم تفعيل التواصل", quote=True)
				db.set(f"{msg.from_user.id}:twasl:{bot_id}", 1)
			else:
				await msg.reply("• التواصل مفعل من قبل", quote=True)
		if msg.text == "• تعطيل التواصل •":
			if db.get(f"{msg.from_user.id}:twasl:{bot_id}"):
				await msg.reply("• تم تعطيل التواصل", quote=True)
				db.delete(f"{msg.from_user.id}:twasl:{bot_id}")
			else:
				await msg.reply("• التواصل غير مفعل", quote=True)
		if msg.text == "• اذاعه •":
			await msg.reply("• ارسل الاذاعه ( نص ، ملف ، جهه اتصال ، متحركه ، ملصق ، صوره )", quote=True)
			db.set(f"{msg.from_user.id}:broadcast:{bot_id}", 1)
			db.delete(f"{msg.from_user.id}:fbroadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:pinbroadcast:{bot_id}")
		if msg.text == "• اذاعه بالتوجيه •":
			await msg.reply("• ارسل الاذاعه ( نص ، ملف ، جهه اتصال ، متحركه ، ملصق ، صوره )", quote=True)
			db.set(f"{msg.from_user.id}:fbroadcast:{bot_id}", 1)
			db.delete(f"{msg.from_user.id}:pinbroadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:broadcast:{bot_id}")
		if msg.text == "• اذاعه بالتثبيت •":
			await msg.reply("• ارسل الاذاعه ( نص ، ملف ، جهه اتصال ، متحركه ، ملصق ، صوره )", quote=True)
			db.set(f"{msg.from_user.id}:pinbroadcast:{bot_id}", 1)
			db.delete(f"{msg.from_user.id}:fbroadcast:{bot_id}")
			db.delete(f"{msg.from_user.id}:broadcast:{bot_id}")
		if msg.text == "• جلب النسخة الاحتياطية •":
			wait = await msg.reply("• انتظر قليلا ..", quote=True)
			await bot.send_document(msg.chat.id, users_backup())
			await wait.delete()
			os.remove("users.txt")
		if msg.text == "• رفع النسخة الاحتياطية •":
			await msg.reply("• ارسل الان نسخه ملف الاعضاء", quote=True)
			db.set(f"{msg.from_user.id}:users_up:{bot_id}", 1)

@app.on_message(filters.private, group=3)
async def forbroacasts(bot, msg):
	if msg.from_user.id in SUDORS and msg.text != "• اذاعه •" and msg.text != "• اذاعه بالتوجيه •" and msg.text != "• اذاعه بالتثبيت •" and msg.text != "• الغاء •" and msg.text != "• رفع النسخة الاحتياطية •" and msg.text != "• اوامر الاذاعه •" and msg.text != "• تعطيل التواصل •" and msg.text != "• تفعيل التواصل •" and msg.text != "• اوامر التواصل •" and msg.text != "• اخفاء الكيبورد •" and msg.text != "• الاحصائيات •":
		if db.get(f"{msg.from_user.id}:broadcast:{bot_id}"):
			db.delete(f"{msg.from_user.id}:broadcast:{bot_id}")
			message = await msg.reply("• جاري الإذاعة ..", quote=True)
			current = 1
			for user in get_users():
				try:
					await msg.copy(int(user))
					progress = (current / len(get_users())) * 100
					current += 1
					if not db.get(f"{msg.from_user.id}:flood:{bot_id}"):
						await message.edit(f"• نسبه الاذاعه {int(progress)}%")
						db.set(f"{msg.from_user.id}:flood:{bot_id}", 1)
						db.expire(f"{msg.from_user.id}:flood:{bot_id}", 4)
				except PeerIdInvalid:
					del_user(int(user))
			await message.edit("• تمت الاذاعه بنجاح")
		if db.get(f"{msg.from_user.id}:pinbroadcast:{bot_id}"):
			db.delete(f"{msg.from_user.id}:pinbroadcast:{bot_id}")
			message = await msg.reply("• جاري الإذاعة ..", quote=True)
			current = 1
			for user in get_users():
				try:
					m = await msg.copy(int(user))
					await m.pin(disable_notification=False,both_sides=True)
					progress = (current / len(get_users())) * 100
					current += 1
					if not db.get(f"{msg.from_user.id}:flood:{bot_id}"):
						await message.edit(f"• نسبه الاذاعه {int(progress)}%")
						db.set(f"{msg.from_user.id}:flood:{bot_id}", 1)
						db.expire(f"{msg.from_user.id}:flood:{bot_id}", 4)
				except PeerIdInvalid:
					del_user(int(user))
			await message.edit("• تمت الاذاعه بنجاح")
		if db.get(f"{msg.from_user.id}:fbroadcast:{bot_id}"):
			db.delete(f"{msg.from_user.id}:fbroadcast:{bot_id}")
			message = await msg.reply("• جاري الإذاعة ..", quote=True)
			current = 1
			for user in get_users():
				try:
					await msg.forward(int(user))
					progress = (current / len(get_users())) * 100
					current += 1
					if not db.get(f"{msg.from_user.id}:flood:{bot_id}"):
						await message.edit(f"• نسبه الاذاعه {int(progress)}%")
						db.set(f"{msg.from_user.id}:flood:{bot_id}", 1)
						db.expire(f"{msg.from_user.id}:flood:{bot_id}", 4)
				except PeerIdInvalid:
					del_user(int(user))
			await message.edit("• تمت الاذاعه بنجاح")
	if msg.document and db.get(f"{msg.from_user.id}:users_up:{bot_id}"):
		message = await msg.reply(f"• انتظر قليلا ..", quote=True)
		await msg.download("./users.txt")
		db.delete(f"botusers{bot_id}")
		file = open("./users.txt", "r", encoding="utf8", errors="ignore")
		for user in file.read().splitlines():
			if not is_user(user):
				add_new_user(user)
		await message.edit(f"• تم رفع نسخه الاعضاء \n• عدد الاعضاء : {len(get_users())}")
		try:
			os.remove("./users.txt")
			db.delete(f"{msg.from_user.id}:users_up:{bot_id}")
		except:
			pass
@app.on_message(filters.private, group=4)
async def twasl(bot, msg):
	if msg.from_user.id not in SUDORS:
		for user in SUDORS:
			if db.get(f"{user}:twasl:{bot_id}"):
				await msg.forward(user)
	if msg.from_user.id in SUDORS:
		if msg.reply_to_message:
			if msg.reply_to_message.forward_from:
				try:
					await msg.copy(msg.reply_to_message.forward_from.id)
					await msg.reply(f"• تم إرسال رسالتك إلى {msg.reply_to_message.forward_from.first_name} بنجاح", quote=True)
				except Exception as Error:
					await msg.reply(f"• لم يتم ارسال رسالتك بسبب: {str(Error)}", quote=True)
					pass






