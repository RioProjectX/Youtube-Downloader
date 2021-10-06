from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel 📢", url="https://t.me/rioprojects")],
        [InlineKeyboardButton(
            "Diskusi 📣 ", url="https://t.me/riogroupsupport")]
    ])
    welcomed = f"Halo <b>{message.from_user.first_name} Saya Adalah Youtube Downloader Maintaned By @fckualot , Cukup Kirim Link Dari Youtube.</b>\n/help Untuk Info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
