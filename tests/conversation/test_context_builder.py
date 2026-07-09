from companion.conversation.context_builder import ContextBuilder


def test_context_builder():

    context = ContextBuilder.build("こんにちは")

    assert context.user_message == "こんにちは"