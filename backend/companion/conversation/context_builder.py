"""
Context Builder

Builds the conversation context.
"""

from companion.conversation.context import ConversationContext


class ContextBuilder:
    """Creates ConversationContext objects."""

    @staticmethod
    def build(message: str) -> ConversationContext:
        return ConversationContext(
            user_message=message.strip()
        )