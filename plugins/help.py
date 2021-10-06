from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Cukup Kirim Link Dari Youtube Untuk Mendownload, Contoh : https://youtu.be/6jZVsr7q-tE"
    await message.reply_text(helptxt)
