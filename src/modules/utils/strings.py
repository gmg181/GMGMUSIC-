#  Copyright (c) 2025 AshokShau
#  Licensed under the GNU AGPL v3.0: https://www.gnu.org/licenses/agpl-3.0.html
#  Part of the TgMusicBot project. All rights reserved where applicable.


PmStartText = """
Hey {0}, 🥀

Tʜɪs ɪs <b>{1}</b>!

Vᴇʀsɪᴏɴ <b>v{2}</b>

➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.

◈ <b>Sᴜᴘᴘᴏʀᴛᴇᴅ Pʟᴀᴛғᴏʀᴍ</b>

☘ Y͛O͛U͛T͛U͛B͛E͛ 

☘ S͛O͛O͛T͛I͛F͛Y͛

☘ J͛I͛O͛ S͛A͛V͛V͛A͛N͛

☘ T͛E͛L͛E͛G͛R͛A͛M͛

──────────────────
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.
"""

StartText = """
<b>нєу {0}, 🥀</b>

<b>{1}</b> Is Aᴄᴛɪᴠᴇ Nᴏᴡ Aɴᴅ Rᴇᴀᴅʏ Tᴏ Pʟᴀʏ Mᴜsɪᴄ ❀</b>

───────────────
Nᴇᴇᴅ Hᴇʟᴘ Oʀ Gᴏᴛ A Qᴜᴇsᴛɪᴏɴ

Join our <a href='{2}'>Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ</a> — ᴡᴇ ᴀʀᴇ ғᴏʀ ʏᴏᴜ 💬
"""

UserCommands = """
<b>Available Commands for Users:</b>

/start – Start the bot.
/play [song name or reply to audio] – Play music in voice chat.
/vplay [song name or reply to video] – Play video in voice chat.
/privacy – View privacy policy.
/lang – Change the bot's language.

"""

AdminCommands = """
<b>Available Commands for Admins:</b>

/skip – Skip the current track.
/pause – Pause the music.
/resume – Resume playback.
/end – Stop the stream.
/remove [x] – Remove the xth song from the queue.
/seek [seconds] – Seek to a specific time.
/mute – Mute the stream.
/unmute – Unmute the stream.
/volume [1-200] – Adjust volume.
/loop [1 to 10 or 0] – Loop the current song (0 to disable).
/queue – Show the song queue.
/clear – Clear the queue.
/speed [0.5-4.0] – Adjust playback speed.
/song [song name or reply to audio] – Download song from YouTube or Spotify.
/setplaytype [0 or 1] – Set the default play type.
"""

ChatOwnerCommands = """
<b>Chat Owner Commands:</b>

/auth [reply] – Authorize a user to use admin commands.
/unauth [reply] – Revoke a user's authorization.
/authlist – Show the list of authorized users.
/reload – Refresh the list of admins in the group.
/buttons – Toggle playback buttons display.
/thumb – Toggle thumbnail display.
/autoend [on/off] – Automatically ends voice chats when no one is listening.
/channelplay [off | reply to channel message] – Connect Group to a channel.
"""

BotDevsCommands = """
<b>Bot Developer Commands:</b>

/stats – Show bot usage statistics.
/logger – Enable or disable logging.
/broadcast [reply] – Broadcast a message to all users and chats.
/activevc – Show currently active voice chats.
/clearallassistants - clear ALL assistant associations.
"""
