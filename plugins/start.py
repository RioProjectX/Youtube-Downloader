from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel 📣", url="https://t.me/rioprojects")],
        [InlineKeyboardButton(
            "Diskusi 📢", url="https://t.me/riogroupsupport")]
        [InlineKeyboardButton(
            "Developer ✳", url="https://t.me/fckualot")]
    ])
    welcomed = f"Halo <b>{message.from_user.first_name} Saya Adalah Youtube Downloader , Saya Dibuat untuk Mendownloas Video Dari Youtube</b>\n/help untuk Info Lebih Lanjut."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
