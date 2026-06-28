from groq import AsyncGroq

from config import Config
from ai.base import BaseProvider


class GroqProvider(BaseProvider):

    name = "Groq"

    def __init__(self):

        self.client = AsyncGroq(
            api_key=Config.GROQ_KEY
        )

    async def generate(
        self,
        system_prompt: str,
        conversation: str
    ) -> str:

        response = await self.client.chat.completions.create(

            model=Config.GROQ_MODEL,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": conversation
                }

            ],

            temperature=1,

            max_tokens=120,

            top_p=1,

        )

        return response.choices[0].message.content.strip()
