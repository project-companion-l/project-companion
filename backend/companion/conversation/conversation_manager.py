from companion.conversation.context_builder import ContextBuilder
from companion.conversation.response_router import ResponseRouter


class ConversationManager:
    """Coordinates conversations."""

    def __init__(self, llm):
        self.llm = llm

    def respond(self, message: str) -> str:

        context = ContextBuilder.build(message)

        response = ResponseRouter.route(context.user_message)

        if response is not None:
            return response

        return self.llm.generate(context.user_message)