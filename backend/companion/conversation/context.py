"""
Conversation Context

Represents the current state of a conversation.
"""

from dataclasses import dataclass


@dataclass
class ConversationContext:
    """Information required to generate a response."""

    user_message: str