"""
LLM Interface

Provides a unified interface to language models.
"""

from companion.llm.mock_provider import MockProvider


class LLMInterface:

    def __init__(self):
        self.provider = MockProvider()

    def generate(self, prompt: str) -> str:
        return self.provider.generate(prompt)