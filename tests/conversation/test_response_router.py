from companion.conversation.response_router import ResponseRouter


def test_greeting():

    response = ResponseRouter.route("こんにちは")

    assert response is not None
    assert "こんにちは" in response