from task.app.main import run
from task.util.llm_functions import LlmModelSelection

def main():
    # Initialize model selector and get user's model choice
    model_selector = LlmModelSelection()
    model = model_selector.select_model()

    # Explain what presence_penalty does
    print("\nPresence Penalty Parameter:")
    print("This parameter penalizes new tokens based on whether they appear in the text so far,")
    print("increasing the model's likelihood to talk about new topics.")
    print("Range: -2.0 to 2.0 (Default: 0.0)")
    print("Higher values (positive) result in more topic diversity.")
    print("Lower values (negative) result in more focus on existing topics.")
    print("Note: This parameter might be ignored by Anthropic and Gemini models.\n")

    # Get presence_penalty value from user
    while True:
        try:
            presence_penalty_input = input("Enter a presence_penalty value (-2.0 to 2.0, default is 0.0): ")

            # Use default if empty input
            if presence_penalty_input == "":
                presence_penalty = 0.0
                break

            presence_penalty = float(presence_penalty_input)
            if -2.0 <= presence_penalty <= 2.0:
                break
            else:
                print("Value must be between -2.0 and 2.0. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nUsing presence_penalty = {presence_penalty}")
    print("Type your question or 'exit' to quit. Try questions that might benefit from topic diversity.")
    

    # Run the conversation with the specified presence_penalty
    run(
        deployment_name=model,
        print_only_content=True,
        presence_penalty=presence_penalty
    )

    print("\nObservation:")
    print("- Higher presence_penalty (e.g., 2.0): The LLM tends to explore more diverse topics")
    print("  related to the main question, covering a broader range of concepts.")
    print("- Lower presence_penalty (e.g., -2.0): The LLM tends to stay more focused on")
    print("  the core concepts and may repeat similar explanations.")

if __name__ == "__main__":
    main()