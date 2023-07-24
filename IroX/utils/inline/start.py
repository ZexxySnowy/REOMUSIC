from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="✼ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ✼",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(text="♙︎ ʜᴇʟᴘ ♙︎", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="❖ sᴇᴛᴛɪɴɢs ❖", callback_data="settings_helper"),
        ],
        ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✼ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ✼",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            ),
            InlineKeyboardButton(
                text="✼ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ✼",
                url=f"https://t.me/{BOT_USERNAME}?startchannel=new",
            )
        ],
        [
            InlineKeyboardButton(text="☃˹ꜱᴜᴘᴘᴏʀᴛ˼☃", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="♢˹ᴜᴘᴅᴀᴛᴇꜱ˼♢", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="✯ Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ ✯", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="☠Sᴏᴜʀᴄᴇ☠", callback_data="source"),
            InlineKeyboardButton(text="♡ 𝐎ᴡɴᴇʀ ♡", user_id=OWNER),
        ],
    ]
    return buttons

close_key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]
            ]
        )
