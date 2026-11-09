from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai import errors
from pydantic import ValidationError
from schemas import AssistantResponse

load_dotenv()

client = genai.Client()

MODEL = "gemini-3-flash-preview"

SYSTEM_INSTRUCTION = """
You are an AI Safety and Risks Tutor.

Your purpose is to teach users about artificial intelligence,
its potential risks, safety challenges, and responsible development.

Cover topics such as:
- AI alignment and control
- Hallucinations and reliability
- Bias and fairness
- Privacy and data protection
- AI security and adversarial attacks
- Prompt injection and misuse
- Autonomous AI agents and their risks
- Deepfakes and misinformation
- AI governance and regulation
- Existential and societal risks of advanced AI

Teaching guidelines:
- Explain concepts clearly, starting with fundamentals.
- Use practical examples and real-world scenarios.
- Explain both the potential benefits and risks of AI.
- Distinguish established evidence from speculation.
- Avoid sensationalism and exaggerated claims.
- Explain possible mitigation strategies.
- Encourage critical thinking rather than presenting
  one viewpoint as unquestionably correct.

Return your response using the required structured format.
"""


def get_response(question: str, history: list) -> AssistantResponse | None:
    user_message = {
        "role": "user",
        "parts": [{"text": question}]
    }

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=history + [user_message],
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
                response_schema=AssistantResponse,
            ),
        )

        result = AssistantResponse.model_validate_json(response.text)

    except errors.APIError as error:
        print(f"\nGemini API error ({error.code}): {error.message}")
        return None

    except ValidationError as error:
        print("\nGemini returned an invalid response:", error)
        return None

    except Exception as error:
        print(f"\nUnexpected error: {error}")
        return None

    history.append(user_message)
    history.append({
        "role": "model",
        "parts": [{"text": result.model_dump_json()}]
    })

    return result