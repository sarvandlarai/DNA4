from config import Config

from ai.openai_provider import OpenAIProvider


class AIRouter:

    def __init__(self):

        self.current_provider = "None"

        self.providers = []

        for provider in Config.AI_PROVIDERS:

            if provider["api_key"]:

                self.providers.append(

                    OpenAIProvider(

                        provider["name"],

                        provider["api_key"],

                        provider["base_url"],

                        provider["model"]

                    )

                )

    async def generate(

        self,

        system_prompt,

        conversation

    ):

        last_error = None

        for provider in self.providers:

            try:

                reply = await provider.generate(

                    system_prompt,

                    conversation

                )

                self.current_provider = provider.name

                return reply

            except Exception as e:

                print(f"{provider.name} failed -> {e}")

                last_error = e

                continue

        raise Exception(last_error)
