# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import config
from pyrogram import Client
from pytgcalls import PyTgCalls

from config import SESSION_NAME, API_ID, API_HASH
from . import queues

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)


from pytgcalls import PyTgCalls
from pyrogram import Client

api_id = "24620300"
api_hash = "9a098f01aa56c836f2e34aee4b7ef963"
bot_token = "8155721991:AAG5s1mh3gykXE7JEovgolr7vO2FPhpx6fk"

# Create pyrogram client instance
client = Client("my_account", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Initialize pytgcalls
pytgcalls = PyTgCalls(client)

# Example of handling stream stop or end event
@pytgcalls.on_stream_stop()  # Use the correct event handler if on_stream_end doesn't exist
def on_stream_end_handler(stream):
    print(f"Stream ended: {stream}")

# Start the client and pytgcalls
client.start()


    if queues.is_empty(chat_id):
        pytgcalls.leave_group_call(chat_id)
    else:
        pytgcalls.change_stream(
            chat_id, queues.get(chat_id)["file"]
        )


run = pytgcalls.run
