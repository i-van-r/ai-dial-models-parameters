from task.app.main import run
from task.util.llm_functions import LlmModelSelection  # Adjust if your selector is elsewhere

selector = LlmModelSelection()
selected_model = selector.select_model()
print(f"Using model: {selected_model}")

print(
    "\nThe 'max_tokens' parameter sets the maximum length of the AI's response (in tokens).\n"
    "The AI will stop generating text once it hits this limit.\n"
    "For this test, we'll use max_tokens=10 to see how the response is cut off.\n"
    "Notice that the finish_reason in the response will be 'length', and the content will be unfinished.\n"
)

try:
    max_tokens = input("Enter a max_tokens value (integer) [default is 10]: ").strip()
    if max_tokens == "":
        max_tokens = 42
    else:
        max_tokens = int(max_tokens)
except (ValueError, KeyboardInterrupt):
    print("\nInvalid input. Defaulting max_tokens to 10.")
    max_tokens = 10

run(
    deployment_name=selected_model,
    print_only_content=True,
    max_tokens=10
)