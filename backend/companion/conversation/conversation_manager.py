"""
Conversation Manager

Coordinates every conversation.

Responsibilities include:

- Context Building
- Prompt Management
- LLM Communication
- Response Validation
- Reflection Triggering
"""

class ConversationManager:
    """Coordinates conversations."""

    def respond(self, message: str) -> str:
        return f"(Prototype) You said: {message}"