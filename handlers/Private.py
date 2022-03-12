import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10d469ec236d49a43650c.jpg",
        caption=f"""**ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ ɪs ᴛʜᴇ ɴᴇxᴛ ʟᴇᴠᴇʟ ᴏғ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴛʜᴀᴛ ʜᴀs ʙᴇsᴛ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ ᴀɴᴅ ᴛʜᴇ ᴛʜɪs ᴍᴜsɪᴄ ʙᴏᴛ sᴍᴀsʜ ᴛʜᴇᴍ ᴏғ ᴀʟʟ sᴇʀᴠᴇʀ ᴏғ ᴍᴜsɪᴄ ʙᴏᴛ ᴀss...

🇴ᴡɴᴇʀ :- [Yᴀsʜ ʀᴀᴊ](https://t.me/give_up_to_god)
🇸ᴜᴘᴘᴏʀᴛ 🇬ʀᴏᴜᴘ   » [Aʟᴇxᴀ Xᴅ Gʀᴏᴜᴘ](https://t.me/Alexa_xd_group)
🇩ɪsᴄᴜss 🇬ʀᴏᴜᴘ  » [Dᴇᴍᴏɴ Cʀᴇᴀᴛᴏʀs Sᴜᴘᴘᴏʀᴛ](https://t.me/Demon_Support_Group)

🇫ᴇᴍᴀʟᴇ 🇴ᴡɴᴇʀ  » [Sᴀᴋsʜɪ](https://t.me/Itzz_Aruu_babee)
🇺ᴘᴅᴀᴛᴇ 🇨ʜᴀɴɴᴇʟ  » [Dᴇᴍᴏɴ Cʀᴇᴀᴛᴏʀs](https://t.me/Demon_Creators)

ɪғ ʏᴏᴜ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴀɴᴅ ɪssᴜᴇ sᴏ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇsᴇ ɪᴅ = [ʏᴀsʜ ʀᴀᴊ](https://t.me/give_up_to_god)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🅲︎ʀᴀᴢʏ 🅳︎ᴘᴢ 🆉︎ᴏɴᴇ", url=f"https://t.me/Crazy_dpz_zone")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["yash"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/10d469ec236d49a43650c.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ ᴀᴘᴘᴇᴀʟ ᴏɴ ᴛʜᴇsᴇ ɢʀᴏᴜᴘ ", url=f"https://t.me/Alexa_xd_group")
                ]
            ]
        ),
    )
