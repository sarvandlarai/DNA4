from openai import AsyncOpenAI

from ai.base import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(

        self,

        name,

        api_key,

        base_url,

        model

    ):

        self.name = name

        self.model = model

        self.client = AsyncOpenAI(

            api_key=api_key,

            base_url=base_url

        )

    async def generate(

        self,

        system_prompt,

        conversation

    ):

        response = await self.client.chat.completions.create(

            model=self.model,

            temperature=1,

            max_tokens=120,

            messages=[

                {

                    "role":"system",

                    "content":system_prompt

                },

                {

                    "role":"user",

                    "content":conversation

                }

            ]

        )

        return response.choices[0].message.content.strip()
