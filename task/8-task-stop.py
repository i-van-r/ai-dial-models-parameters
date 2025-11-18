from task.app.main import run
from task.util.llm_functions import LlmModelSelection

def main():
    # Initialize model selector and get user's model choice
    model_selector = LlmModelSelection()
    model = model_selector.select_model()

    # Explain what stop parameter does
    print("\nStop Parameter:")
    print("This parameter tells the AI to stop generating text when it encounters specific words or phrases.")
    print("It works like setting custom 'end of response' triggers.")
    print("Type: string or list of strings")
    print("Default: None")
    print("Note: This parameter might work differently across various model providers.\n")

    # Show stop parameter options
    print("Select a stop parameter configuration:")
    print("1. Stop after a double newline (stop=\"\n\n\")")
    print("2. Stop at specific section headers [\"**Embedding Layer**\", \"**Transformer Blocks**\", \"**Training**\"]")
    print("3. No stop parameter (default)")
    print("4. Custom stop parameter")

    # Get user's choice of stop parameter
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ")
            if choice == "1":
                stop_param = "\n\n"
                break
            elif choice == "2":
                stop_param = ["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
                break
            elif choice == "3":
                stop_param = None
                break
            elif choice == "4":
                custom_stop = input("Enter your custom stop parameter (comma-separated for multiple values): ")
                if "," in custom_stop:
                    stop_param = [s.strip() for s in custom_stop.split(",")]
                else:
                    stop_param = custom_stop
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid option.")

    # Ask if user wants to see the full response JSON
    print_content_only = True
    show_full = input("\nDo you want to see the full response JSON including finish_reason? (y/N): ").lower()
    if show_full == "y":
        print_content_only = False

    print("\n=== Testing Stop Parameter ===")
    print(f"Using stop = {stop_param}")
    print(f"Print only content = {print_content_only}")
    print("\nThe model will now explain the key components of a Large Language Model architecture.\n")

    # Run the conversation with the specified stop parameter
    print("\nSuggested query: 'Explain the key components of a Large Language Model architecture'")
    print("This will help demonstrate the stop parameter's effect on structured content.\n")
    
    run(
        deployment_name=model,
        print_only_content=print_content_only,
        stop=stop_param
    )

    # Explain the concept and use cases
    print("\nObservation:")
    print("- The 'stop' parameter can be used to control when the model stops generating text.")
    print("- This can be useful for:")
    print("  1. Creating specific response formats")
    print("  2. Implementing content policies/guardrails")
    print("  3. Preventing the model from discussing certain topics")
    print("  4. Forcing brevity in responses")
    print("\nExample use case: A company named 'Pear' might use stop=[\"Apple is cool\", \"Apple top\"]")
    print("to prevent the model from saying positive things about a competitor.")
    print("\nWhen the 'stop' parameter triggers, the 'finish_reason' in the response will be 'stop'")
    print("rather than the usual 'stop_sequence' or 'length'.")

if __name__ == "__main__":
    main()