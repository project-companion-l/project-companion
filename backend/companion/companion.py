from companion.core.identity_kernel import IdentityKernel
from companion.conversation.conversation_manager import ConversationManager
from companion.utils.config import Config

class Companion:
    """Main entry point for Project Companion."""

    def __init__(self):
        self.identity = IdentityKernel()
        self.conversation = ConversationManager()
        self.config = Config()
    
    def start(self):
        print(f"{self.identity.name} is starting...")

    def chat(self, message):
        return self.conversation.respond(message)