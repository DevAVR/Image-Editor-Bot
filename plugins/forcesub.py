import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from helper_funcs.chat_base import TRChatBase

@Client.on_message(filters.photo & filters.private)
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

  await update.reply_text(text="**Join My Updates Channel to use ME 😎 🤭**",
                                    reply_markup=InlineKeyboardMarkup([
                                        [ InlineKeyboardButton(text="Join My Updates Channel", url=f"https://t.me/{update_channel}")]
                                        ])
                                    )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return
