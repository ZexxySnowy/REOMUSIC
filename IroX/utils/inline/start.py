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
                text="✼ 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴩ ✼",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            ),
            InlineKeyboardButton(
                text="✼ 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐂ʜᴀɴɴᴇʟ ✼",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
        [
            InlineKeyboardButton(text="☃˹ꜱᴜᴘᴘᴏʀᴛ˼☃", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="♪˹ᴜᴘᴅᴀᴛᴇꜱ˼♪", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="✯ Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ ✯", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="☠Sᴏᴜʀᴄᴇ☠", url=config.GITHUB_REPO),
            InlineKeyboardButton(text="ღ 𝐎ᴡɴᴇʀ ღ", user_id=OWNER),
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
