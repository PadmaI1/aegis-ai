from assistant import get_response, client


def main():
    history = []

    print("AI Safety and Risks Tutor")
    print("Type 'exit' to quit.")

    try:
        while True:
            question = input("\nYou: ").strip()

            if question.lower() == "exit":
                break

            if not question:
                continue

            response = get_response(question, history)

            if response is None:
                continue

            print("\nGemini:", response.answer)

            if response.key_points:
                print("\nKey points:")
                for point in response.key_points:
                    print(f"- {point}")

            if response.follow_up_question:
                print("\nFollow-up:", response.follow_up_question)

            history = history[-6:]

    finally:
        client.close()


if __name__ == "__main__":
    main()