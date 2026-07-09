"""
Response Router

Determines how a user message should be handled.
"""

from companion.conversation.response_templates import ResponseTemplates


class ResponseRouter:

    @staticmethod
    def route(message: str) -> str:

        message = message.strip()

        if message in ResponseTemplates.GREETINGS:
            return ResponseTemplates.GREETINGS[message]

        if message in ResponseTemplates.FAREWELLS:
            return ResponseTemplates.FAREWELLS[message]

        return None