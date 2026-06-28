import logging

from ai.openai_provider import OpenAIProvider
from ai.gemini_provider import GeminiProvider
from ai.groq_provider import GroqProvider
from ai.openrouter_provider import OpenRouterProvider
from ai.claude_provider import ClaudeProvider

logger = logging.getLogger("BakeBot")


class AIRouter:

    def __init__(self):

        self.providers = [

            GroqProvider(),

            GeminiProvider(),

            OpenRouterProvider(),

            OpenAIProvider(),

            ClaudeProvider()

        ]

        self.current_provider = "None"

    async def generate(

        self,

        system_prompt: str,

        conversation: str

    ):

        last_error = None

        for provider in self.providers:

            try:

                reply = await provider.generate(

                    system_prompt,

                    conversation

                )

                self.current_provider = provider.name

                logger.info(f"AI -> {provider.name}")

                return reply

            except Exception as e:

                logger.warning(

                    f"{provider.name} failed : {e}"

                )

                last_error = e

                continue

        raise Exception(
            f"All AI providers failed.\n{last_error}"
        )
