import os
import shutil
import asyncio
from re import findall
from bing_image_downloader import downloader
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message


def sanitize_filename(name: str) -> str:
    return "".join(c if c.isalnum() or c in " ._-" else "_" for c in name)


@Client.on_message(filters.command(["img", "image"], prefixes=["/", "!"]))
async def google_img_search(client: Client, message: Message):
    chat_id = message.chat.id

    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("❍ ᴘʀᴏᴠɪᴅᴇ ᴀɴ ɪᴍᴀɢᴇ ǫᴜɪᴇʀʏ ᴛᴏ sᴇᴀʀᴄʜ!")

    lim = findall(r"lim=\d+", query)
    try:
        lim = int(lim[0].replace("lim=", ""))
        query = query.replace(f"lim={lim}", "")
    except IndexError:
        lim = 6  # Default limit

    query = sanitize_filename(query.strip())
    download_dir = "downloads"
    images_dir = os.path.join(download_dir, query)

    os.makedirs(download_dir, exist_ok=True)

    try:
        downloader.download(query, limit=lim, output_dir=download_dir, adult_filter_off=True, force_replace=True, timeout=60)
        if not os.listdir(images_dir):
            raise Exception("No images were downloaded.")
        lst = [os.path.join(images_dir, img) for img in os.listdir(images_dir) if img.endswith((".jpg", ".png", ".jpeg"))][:lim]
    except Exception as e:
        return await message.reply(f"❍ ᴇʀʀᴏʀ ɪɴ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ɪᴍᴀɢᴇs: {e}")

    msg = await message.reply("❍ 𝐀ᴜʀᴀ 𝐁ᴇᴀᴛs ғɪɴᴅɪɴɢ ɪᴍᴀɢᴇs.....")

    try:
        await client.send_media_group(
            chat_id=chat_id,
            media=[InputMediaPhoto(media=img) for img in lst],
            reply_to_message_id=message.id
        )
        await msg.delete()
    except Exception as e:
        await msg.delete()
        return await message.reply(f"❍ ᴇʀʀᴏʀ ɪɴ sᴇɴᴅɪɴɢ ɪᴍᴀɢᴇs: {e}")

    asyncio.create_task(delete_folder_after_delay(images_dir, delay=600))


async def delete_folder_after_delay(path: str, delay: int):
    await asyncio.sleep(delay)
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)
