from pyrogram import Client, filters

from config import OWNER_ID

from AnonX.misc import SUDOERS

from AnonX import app

chat_locked = False

SUDOERS = SUDOERS

OWNER_ID = OWNER_ID

def is_sudoer(_, __, message):

    return message.from_user.id in SUDOERS or message.from_user.id == OWNER_ID

def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID

@app.on_message(filters.command("lock") & filters.create(is_sudoer))

def lock_chat(client, message):

    global chat_locked

    

    chat_locked = True

    

    message.reply_text("تم قفل الدردشة.")

@app.on_message(filters.command("unlock") & filters.create(is_sudoer))

def unlock_chat(client, message):

    global chat_locked

    

    chat_locked = False

    

    message.reply_text("تم فتح الدردشة.")

@app.on_message()

def delete_message(client, message):

    global chat_locked

    

    if chat_locked and not (is_sudoer(client, None, message) or is_owner(client, None, message)):

        message.delete()

