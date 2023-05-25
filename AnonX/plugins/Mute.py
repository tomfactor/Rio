from pyrogram import Client, filters

from config import OWNER_ID

from AnonX.misc import SUDOERS

from AnonX import app

from strings.filters import command

all_locked = False

chat_locked = False

photo_locked = False

video_locked = False

link_locked = False

sticker_locked = False

forward_locked = False

reply_locked = False

SUDOERS = SUDOERS

OWNER_ID = OWNER_ID

def is_sudoer(_, __, message):

    return message.from_user.id in SUDOERS or message.from_user.id == OWNER_ID

def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID

@app.on_message(command("قفل الكل") & filters.create(is_sudoer))

def lock_all(client, message):

    global all_locked, chat_locked, photo_locked, video_locked, link_locked, sticker_locked, forward_locked, reply_locked

    if all_locked:

        message.reply_text("العناصر مقفولة بالفعل.")

    else:

        all_locked = True

        chat_locked = True

        photo_locked = True

        video_locked = True

        link_locked = True

        sticker_locked = True

        forward_locked = True

        reply_locked = True

        message.reply_text("تم قفل جميع العناصر.")

@app.on_message(command("قفل الدردشه") & filters.create(is_sudoer))

def lock_chat(client, message):

    global chat_locked

    if chat_locked:

        message.reply_text("الدردشة مقفولة بالفعل.")

    else:

        chat_locked = True

        message.reply_text("تم قفل الدردشة.")

@app.on_message(command("قفل الصور") & filters.create(is_sudoer))

def lock_photos(client, message):

    global photo_locked

    if photo_locked:

        message.reply_text("الصور مقفولة بالفعل.")

    else:

        photo_locked = True

        message.reply_text("تم قفل الصور.")

@app.on_message(command("قفل الفيديو") & filters.create(is_sudoer))

def lock_videos(client, message):

    global video_locked

    if video_locked:

        message.reply_text("الفيديو مقفول بالفعل.")

    else:

        video_locked = True

        message.reply_text("تم قفل الفيديو.")

@app.on_message(command("قفل الروابط") & filters.create(is_sudoer))

def lock_links(client, message):

    global link_locked

    if link_locked:

        message.reply_text("الروابط مقفولة بالفعل.")

    else:

        link_locked = True

        message.reply_text("تم قفل الروابط.")

@app.on_message(command("قفل الملصقات") & filters.create(is_sudoer))

def lock_stickers(client, message):

    global sticker_locked

    if sticker_locked:

        message.reply_text("الملصقات مقفولة بالفعل.")

    else:

        sticker_locked = True

        message.reply_text("تم قفل الملصقات.")

@app.on_message(command("قفل التوجيه") & filters.create(is_sudoer))

def lock_forwarded_messages(client, message):

    global forward_locked

    if forward_locked:

        message.reply_text("التوجيه مقفول بالفعل.")

    else:

        forward_locked = True

        message.reply_text("تم قفل التوجيه.")

@app.on_message(command("قفل الردود") & filters.create(is_sudoer))

def lock_reply_messages(client, message):

    global reply_locked

    if reply_locked:

        message.reply_text("الردود مقفولة بالفعل.")

    else:

        reply_locked = True

        message.reply_text("تم قفل الردود.")

@app.on_message(command("فتح الكل") & filters.create(is_sudoer))

def unlock_all(client, message):

    global all_locked, chat_locked, photo_locked, video_locked, link_locked, sticker_locked, forward_locked, reply_locked

    if not all_locked:

        message.reply_text("العناصر مفتوحة بالفعل.")

    else:

        all_locked = False

        chat_locked = False

        photo_locked = False

        video_locked = False

        link_locked = False

        sticker_locked = False

        forward_locked = False

        reply_locked = False

        message.reply_text("تم فتح جميع العناصر.")

@app.on_message(command("فتح الدردشه") & filters.create(is_sudoer))

def unlock_chat(client, message):

    global chat_locked

    if not chat_locked:

        message.reply_text("الدردشة مفتوحة بالفعل.")

    else:

        chat_locked = False

        message.reply_text("تم فتح الدردشة.")

@app.on_message(command("فتح الصور") & filters.create(is_sudoer))

def unlock_photos(client, message):

    global photo_locked

    if not photo_locked:

        message.reply_text("الصور مفتوحة بالفعل.")

    else:

        photo_locked = False

        message.reply_text("تم فتح الصور.")

@app.on_message(command("فتح الفيديو") & filters.create(is_sudoer))

def unlock_videos(client, message):

    global video_locked

    if not video_locked:

        message.reply_text("الفيديو مفتوح بالفعل.")

    else:

        video_locked = False

        message.reply_text("تم فتح الفيديو.")

@app.on_message(command("فتح الروابط") & filters.create(is_sudoer))

def unlock_links(client, message):

    global link_locked

    if not link_locked:

        message.reply_text("الروابط مفتوحة بالفعل.")

    else:

        link_locked = False

        message.reply_text("تم فتح الروابط.")

@app.on_message(command("فتح الملصقات") & filters.create(is_sudoer))

def unlock_stickers(client, message):

    global sticker_locked

    if not sticker_locked:

        message.reply_text("الملصقات مفتوحة بالفعل.")

    else:

        sticker_locked = False

        message.reply_text("تم فتح الملصقات.")

@app.on_message(command("فتح التوجيه") & filters.create(is_sudoer))

def unlock_forwarded_messages(client, message):

    global forward_locked

    if not forward_locked:

        message.reply_text("التوجيه مفتوح بالفعل.")

    else:

        forward_locked = False

        message.reply_text("تم فتح التوجيه.")

@app.on_message(command("فتح الردود") & filters.create(is_sudoer))

def unlock_reply_messages(client, message):

    global reply_locked

    if not reply_locked:

        message.reply_text("الردود مفتوحة بالفعل.")

    else:

        reply_locked = False

        message.reply_text("تم فتح الردود.")

@app.on_message()

def delete_message(client, message):

    global chat_locked, photo_locked, video_locked, link_locked, sticker_locked, forward_locked, reply_locked

    is_admin = is_sudoer(client, None, message) or is_owner(client, None, message)

    if message.text:

        command = message.text.lower()

        if command.startswith("قفل الكل") or command.startswith("قفل الدردشة") or command.startswith("قفل الصور") or command.startswith("قفل الفيديو") or command.startswith("قفل الروابط") or command.startswith("قفل الملصقات") or command.startswith("قفل التوجيه") or command.startswith("قفل الردود")or command.startswith("فتح الكل")or command.startswith("فتح الدردشة") or command.startswith("فتح الصور") or command.startswith("فتح الفيديو") or command.startswith("فتح الروابط") or command.startswith("فتح الملصقات") or command.startswith("فتح التوجيه") or command.startswith("فتح الردود"):

            if not is_admin:

                message.reply_text("يجب ان تكون مطور لتتمكن من استخدام هذا الامر")

            return

    

    if chat_locked and not is_admin:

        message.delete()

    elif photo_locked and message.photo and not is_admin:

        message.delete()

    elif video_locked and message.video and not is_admin:

        message.delete()

    elif link_locked and ("http://" in message.text or "https://" in message.text) and not is_admin:

        message.delete()

    elif sticker_locked and message.sticker and not is_admin:

        message.delete()

    elif all_locked and not is_admin:

        message.delete()

    elif forward_locked and message.forward_from and not is_admin:

        message.delete()

    elif reply_locked and message.reply_to_message and not is_admin:

        message.delete()

    elif all_locked and (message.text or message.photo or message.video or message.sticker or message.forward_from or message.reply_to_message) and not is_admin:

        message.delete()
