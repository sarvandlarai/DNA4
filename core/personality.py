from pathlib import Path

from config import Config


class Personality:

    def __init__(self):

        self.personality = ""
        self.system = ""

        self.load()

    def load(self):

        personality_file = Path(
            Config.PERSONALITY_FILE
        )

        system_file = Path(
            Config.SYSTEM_PROMPT
        )

        if personality_file.exists():

            self.personality = personality_file.read_text(
                encoding="utf-8"
            )

        else:

            self.personality = ""

        if system_file.exists():

            self.system = system_file.read_text(
                encoding="utf-8"
            )

        else:

            self.system = ""

    def build_prompt(self, context):

        return f"""
{self.system}

{self.personality}

------------------------
Recent Conversation
------------------------

{context}

------------------------
Instructions
------------------------

Reply naturally to the latest message if it makes sense.

Keep replies short.

Do not write paragraphs.

Use Discord style.

Don't repeat yourself.

Reply with ONLY the message.
"""

    def reload(self):

        self.load()
