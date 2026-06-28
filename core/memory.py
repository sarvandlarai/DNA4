from collections import defaultdict, deque
import discord

from config import Config


class MemoryManager:

    def __init__(self):

        # channel_id -> last messages
        self.channel_history = defaultdict(
            lambda: deque(maxlen=Config.HISTORY_LIMIT)
        )

        # simple user memory
        self.user_memory = defaultdict(dict)

    async def store_message(self, message: discord.Message):

        if not message.content:
            return

        self.channel_history[message.channel.id].append({

            "author": message.author.display_name,

            "author_id": message.author.id,

            "content": message.content,

            "channel": message.channel.name

        })

    def get_context(self, channel_id):

        history = self.channel_history.get(channel_id, [])

        lines = []

        for msg in history:

            lines.append(
                f"{msg['author']}: {msg['content']}"
            )

        return "\n".join(lines)

    def remember(self, user_id, key, value):

        self.user_memory[user_id][key] = value

    def recall(self, user_id, key):

        return self.user_memory.get(user_id, {}).get(key)

    def clear_channel(self, channel_id):

        if channel_id in self.channel_history:
            self.channel_history[channel_id].clear()

    def message_count(self, channel_id):

        return len(
            self.channel_history.get(channel_id, [])
        )
