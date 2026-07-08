"""
Project Companion

Companion is the central coordinator of the entire system.

It coordinates conversations, memory, identity,
and external AI providers.

The Companion itself does not perform reasoning.
It orchestrates the components that together form
a lifelong companion.
"""

from companion.conversation.conversation_manager import ConversationManager


class Companion:
    """Main entry point for Project Companion."""

    def __init__(self) -> None:
        self.conversation = ConversationManager()

    def start(self) -> None:
        """Initialize the Companion."""
        print("Project Companion is starting...")

    def chat(self, message: str) -> str:
        """Handle a conversation with the user."""
        return self.conversation.respond(message)