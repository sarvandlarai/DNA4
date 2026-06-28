import asyncio
import logging
import discord
from discord.ext import commands

from config import Config

# Core
from core.scheduler import Scheduler
from core.memory import MemoryManager
from core.personality import Personality

# AI
from ai.router import AIRouter

# ===========================
# Logging
# ===========================

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s | %(message)s"
)

logger = logging.getLogger("BakeBot")

# ===========================
# Discord Intents
# ===========================

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.reactions = True

bot = commands.Bot(
    command_prefix=Config.PREFIX,
    intents=intents,
    help_command=None
)

# ===========================
# Global Managers
# ===========================

memory = MemoryManager()
personality = Personality()
ai = AIRouter()

scheduler = Scheduler(
    bot=bot,
    ai=ai,
    memory=memory,
    personality=personality
)

# ===========================
# Ready
# ===========================

@bot.event
async def on_ready():

    logger.info("-"*40)
    logger.info(f"Logged in as {bot.user}")
    logger.info(f"Servers : {len(bot.guilds)}")
    logger.info("BakeBot Online")
    logger.info("-"*40)

    if not scheduler.running:
        bot.loop.create_task(scheduler.start())

# ===========================
# Message Event
# ===========================

@bot.event
async def on_message(message: discord.Message):

    if message.author.bot:
        return

    # save message
    await memory.store_message(message)

    # commands
    await bot.process_commands(message)

    # scheduler decides if reply
    await scheduler.handle_message(message)

# ===========================
# Basic Commands
# ===========================

@bot.command()
async def ping(ctx):

    latency = round(bot.latency * 1000)

    await ctx.send(f"Pong! `{latency}ms`")

@bot.command()
async def stats(ctx):

    embed = discord.Embed(
        title="BakeBot",
        colour=0x2ecc71
    )

    embed.add_field(
        name="Servers",
        value=str(len(bot.guilds))
    )

    embed.add_field(
        name="Latency",
        value=f"{round(bot.latency*1000)} ms"
    )

    embed.add_field(
        name="AI Provider",
        value=ai.current_provider
    )

    await ctx.send(embed=embed)

# ===========================
# Run
# ===========================

def main():

    bot.run(Config.DISCORD_TOKEN)

if __name__ == "__main__":
    main()
