from pydantic import BaseModel


class AssistantResponse(BaseModel):
    answer: str
    key_points: list[str]
    follow_up_question: str | None = None