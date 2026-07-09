"""
Mock provider for development.
"""

from companion.llm.provider import LLMProvider


class MockProvider(LLMProvider):

    def generate(self, prompt: str) -> str:
        return f"(Mock LLM) {prompt}"