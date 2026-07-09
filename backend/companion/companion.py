from companion.core.identity_kernel import IdentityKernel
from companion.conversation.conversation_manager import ConversationManager
from companion.llm.llm_interface import LLMInterface
from companion.utils.config import Config


class Companion:
    """Main entry point for Project Companion."""

    def __init__(self):
        self.config = Config()
        self.identity = IdentityKernel()

        self.llm = LLMInterface()

        self.conversation = ConversationManager(
            llm=self.llm
        )

    def start(self):
        print(f"{self.identity.name} is starting...")

    def chat(self, message):
        return self.conversation.respond(message)