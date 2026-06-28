import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    # =========================
    # Discord
    # =========================

    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    PREFIX = "!"

    # =========================
    # AI Providers
    # =========================

    OPENAI_KEY = os.getenv("OPENAI_KEY")

    GEMINI_KEY = os.getenv("GEMINI_KEY")

    GROQ_KEY = os.getenv("GROQ_KEY")

    CLAUDE_KEY = os.getenv("CLAUDE_KEY")

    OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")

    # =========================
    # Models
    # =========================

    OPENAI_MODEL = "gpt-4.1-mini"

    GEMINI_MODEL = "gemini-2.5-flash"

    GROQ_MODEL = "llama-3.3-70b-versatile"

    CLAUDE_MODEL = "claude-3-5-sonnet-latest"

    OPENROUTER_MODEL = "deepseek/deepseek-chat-v3-0324"

    # =========================
    # Reply Behaviour
    # =========================

    REPLY_CHANCE = 0.30

    REACT_CHANCE = 0.20

    START_CONVERSATION_CHANCE = 0.08

    MAX_CONTEXT_MESSAGES = 15

    MAX_REPLY_WORDS = 25

    # =========================
    # Timers
    # =========================

    MIN_REPLY_DELAY = 2

    MAX_REPLY_DELAY = 8

    MIN_IDLE_CHAT = 1200

    MAX_IDLE_CHAT = 3600

    # =========================
    # Cooldowns
    # =========================

    CHANNEL_COOLDOWN = 180

    USER_COOLDOWN = 120

    # =========================
    # Memory
    # =========================

    MEMORY_DB = "database/bakebot.db"

    HISTORY_LIMIT = 25

    # =========================
    # Emojis
    # =========================

    REACTION_EMOJIS = [

        "😂",
        "😭",
        "💀",
        "🔥",
        "👀",
        "🤣",
        "😎",
        "😴",
        "🗿",
        "👍"

    ]

    # =========================
    # Personality
    # =========================

    PERSONALITY_FILE = "prompts/personality.txt"

    SYSTEM_PROMPT = "prompts/system.txt"

    # =========================
    # Logging
    # =========================

    DEBUG = True
