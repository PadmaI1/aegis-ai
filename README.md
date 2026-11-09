# AegisAI— An Interactive AI Safety and Risks Tutor

An interactive, conversational AI tutor built with Python and Google's Gemini API to help users understand AI safety, risks, alignment, security, and responsible AI development.

## Features

- **AI Safety Education:** Learn about AI alignment, control, and responsible AI development.
- **AI Risks:** Explore hallucinations, bias, privacy concerns, misinformation, and societal risks.
- **AI Security:** Understand prompt injection, adversarial attacks, vulnerabilities, and AI misuse.
- **Conversational Learning:** Maintains conversation history to support follow-up questions.
- **Structured Responses:** Generates predictable JSON responses using Gemini and validates them with Pydantic.
- **Error Handling:** Handles API errors and invalid model responses.
- **Automated Testing:** Includes tests using pytest without requiring real API calls.

## Topics Covered

- AI alignment and control
- Hallucinations and model reliability
- Bias, fairness, and discrimination
- Privacy and data protection
- Prompt injection and adversarial attacks
- Autonomous AI agents and their risks
- Deepfakes and misinformation
- AI governance and regulation
- Societal and existential risks of advanced AI
- AI safety techniques and mitigation strategies

## Tech Stack

- **Language:** Python 3.12
- **LLM:** Google Gemini API
- **SDK:** `google-genai`
- **Structured Outputs:** Pydantic
- **Environment Management:** python-dotenv, uv
- **Testing:** pytest

## Project Structure

```text
ai-safety-tutor/
├── main.py
├── assistant.py
├── schemas.py
├── tests/
│   └── test_assistant.py
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd ai-safety-tutor
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Get an API key from [Google AI Studio](https://aistudio.google.com/).

### 4. Run the application

```bash
uv run python main.py
```

### 5. Run tests

```bash
uv run pytest -v
```

## Example Usage

```text
AI Safety and Risks Tutor
Type 'exit' to quit.

You: What is AI alignment?

Gemini:
[An explanation of AI alignment]

Key points:
- ...
- ...

Follow-up:
Would you like to learn about alignment challenges?
```

## Project Goals

This project explores practical LLM application development while making AI safety concepts more accessible.

It demonstrates:
- Integrating an LLM API into a Python application.
- Designing structured LLM outputs.
- Managing conversational context.
- Handling API failures.
- Validating model responses.
- Writing automated tests for AI applications.

