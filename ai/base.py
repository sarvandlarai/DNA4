from abc import ABC, abstractmethod


class BaseProvider(ABC):

    name = "Unknown"

    @abstractmethod
    async def generate(
        self,
        system_prompt: str,
        conversation: str
    ) -> str:
        pass
