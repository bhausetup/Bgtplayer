from pyrogram import Client, filters

from Bikash import app
from Bikash.utils.bgtmusic.bk import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("bikash")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def bikash(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/60475df3ad2977e20128b.jpg",
        caption=f"""🥀 𝐂𝐡𝐞𝐫𝐫𝐲 𝐈𝐬 𝐎𝐰𝐧𝐞𝐫 𝐎𝐟 𝐅𝐢𝐳𝐚 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 🌺, 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐂𝐡𝐞𝐫𝐫𝐲 ♕, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤, 𝐓𝐡𝐞𝐧 𝐂𝐥𝐢𝐜𝐤 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 𝐁𝐮𝐭𝐭𝐨𝐧 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 [𝐂𝐡𝐞𝐫𝐫𝐲](https://t.me/DRACULA_CHEERY)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐂𝐡𝐞𝐫𝐫𝐲 🥀", url=f"https://t.me/DRACULA_CHEERY")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝐂𝐡𝐞𝐫𝐫𝐲𝐅𝐢𝐳𝐚 🥀", url=f"https://t.me/I_LOVE_YOU_MY_HEARTBEET")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/ISHQ00_I"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/ITSBOTS")
                ]
            ]
        ),
    )
