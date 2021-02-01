from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from helper_funcs.chat_base import TRChatBase

@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    if update.from_user.id in Config.BANNED_USERS:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.BANNED_USER_TEXT,
            reply_to_message_id=update.message_id
        )
        return
    TRChatBase(update.from_user.id, update.text, "photo")
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("🤭 Sorry Dude, You are **B A N N E D 🤣🤣🤣**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="**Join My Updates Channel to use ME 😎 🤭**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="Select your required mode from below!ㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="BRIGHT", callback_data="bright"),
                        InlineKeyboardButton(text="MIXED", callback_data="mix"),
                        InlineKeyboardButton(text="B&W", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="CIRCLE", callback_data="circle"),
                        InlineKeyboardButton(text="BLUR", callback_data="blur"),
                        InlineKeyboardButton(text="BORDER", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="STICKER", callback_data="stick"),
                        InlineKeyboardButton(text="ROTATE", callback_data="rotate"),
                        InlineKeyboardButton(text="CONTRAST", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="SEPIA", callback_data="sepia"),
                        InlineKeyboardButton(text="PENCIL", callback_data="pencil"),
                        InlineKeyboardButton(text="CARTOON", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="INVERT", callback_data="inverted"),
                        InlineKeyboardButton(text="GLITCH", callback_data="glitch"),
                        InlineKeyboardButton(
                            text="REMOVE BG", callback_data="removebg"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="CLOSE", callback_data="close_e"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return
