import asyncio
import random
import time

from core.reactions import ReactionManager
from config import Config


class Scheduler:

    def __init__(self, bot, ai, memory, personality):

        self.bot = bot
        self.ai = ai
        self.memory = memory
        self.personality = personality
        class Scheduler:

    def __init__(self, bot, ai, memory, personality):

        self.bot = bot
        self.ai = ai
        self.memory = memory
        self.personality = personality

        # Initialize reaction manager
        self.reactions = ReactionManager()

        self.running = False

        self.last_channel_reply = {}
        self.last_user_reply = {}

        self.running = False

        self.last_channel_reply = {}
        self.last_user_reply = {}

    # --------------------------
    # Main Loop
    # --------------------------

    async def start(self):

        self.running = True

        while True:

            try:

                await self.random_chat()

            except Exception as e:

                print(e)

            await asyncio.sleep(
                random.randint(
                    Config.MIN_IDLE_CHAT,
                    Config.MAX_IDLE_CHAT
                )
            )

    # --------------------------
    # Message Handler
    # --------------------------

    async def handle_message(self, message):

        if not self.should_reply(message):
            return

        channel = message.channel

        context = self.memory.get_context(channel.id)

        prompt = self.personality.build_prompt(context)

        # thinking delay
        await asyncio.sleep(
            random.uniform(
                Config.MIN_REPLY_DELAY,
                Config.MAX_REPLY_DELAY
            )
        )

        async with channel.typing():

            await asyncio.sleep(
                random.uniform(1, 3)
            )

            reply = await self.ai.generate(
                prompt,
                context
            )

        if not reply:
            return

        await message.reply(
            reply,
            mention_author=False
        )

        now = time.time()

        self.last_channel_reply[channel.id] = now
        self.last_user_reply[message.author.id] = now

        # random reaction
        if random.random() < Config.REACT_CHANCE:

            try:

               emoji = self.reactions.choose(
               message.content
               )

                await message.add_reaction(emoji)

            except:

                pass

    # --------------------------
    # Reply Logic
    # --------------------------

    def should_reply(self, message):

        now = time.time()

        # probability
        if random.random() > Config.REPLY_CHANCE:
            return False

        # ignore commands
        if message.content.startswith(Config.PREFIX):
            return False

        # ignore empty
        if not message.content:
            return False

        # channel cooldown
        last = self.last_channel_reply.get(
            message.channel.id,
            0
        )

        if now - last < Config.CHANNEL_COOLDOWN:
            return False

        # user cooldown
        last = self.last_user_reply.get(
            message.author.id,
            0
        )

        if now - last < Config.USER_COOLDOWN:
            return False

        return True

    # --------------------------
    # Random Conversation
    # --------------------------

    async def random_chat(self):

        if random.random() > Config.START_CONVERSATION_CHANCE:
            return

        if not self.bot.guilds:
            return

        guild = random.choice(
            self.bot.guilds
        )

        channels = []

        for channel in guild.text_channels:

            if channel.permissions_for(
                guild.me
            ).send_messages:

                channels.append(channel)

        if not channels:
            return

        channel = random.choice(channels)

        starters = [

            "What's everyone up to today?",

            "Anyone playing anything fun tonight?",

            "Random question: what's your favorite snack?",

            "What's the best movie you've watched recently?",

            "Anyone got music recommendations?",

            "What's everyone's weekend plan?",

            "Favorite game right now?"

        ]

        await asyncio.sleep(
            random.randint(2, 8)
        )

        async with channel.typing():

            await asyncio.sleep(
                random.randint(2, 5)
            )

            await channel.send(
                random.choice(starters)
            )
