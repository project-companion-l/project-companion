"""
Abstract interface for language model providers.
"""

from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """Base interface for all LLM providers."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from the prompt."""
        raise NotImplementedError