from types import SimpleNamespace

import assistant
from schemas import AssistantResponse

from google.genai import errors


def test_get_response(monkeypatch):
    def fake_generate_content(**kwargs):
        return SimpleNamespace(
            text='{"answer": "A list is mutable.", '
                 '"key_points": ["Lists can be changed"], '
                 '"follow_up_question": null}'
        )

    monkeypatch.setattr(
        assistant.client.models,
        "generate_content",
        fake_generate_content,
    )

    history = []

    result = assistant.get_response("Are lists mutable?", history)

    assert isinstance(result, AssistantResponse)
    assert result.answer == "A list is mutable."
    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[1]["role"] == "model"

def test_get_response_api_error(monkeypatch):
    def fake_generate_content(**kwargs):
        raise errors.APIError(
            code=429,
            response_json={
                "error": {
                    "message": "Rate limit exceeded",
                    "status": "RESOURCE_EXHAUSTED"
                }
            },
        )

    monkeypatch.setattr(
        assistant.client.models,
        "generate_content",
        fake_generate_content,
    )

    history = []

    result = assistant.get_response("Explain Python lists", history)

    assert result is None
    assert history == []