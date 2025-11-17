from task.app.main import run
from task.util.llm_functions import LlmModelSelection

llmSelector = LlmModelSelection()
selected_model = llmSelector.select_model()

print(f"Using model: {selected_model}")

# n parameter input
try:
    n_input = input("Enter the number of completions to generate (n, 1-5) [default 1]: ").strip()
    if n_input == "":
        n_value = 1
    else:
        n_value = int(n_input)
    if not (1 <= n_value <= 5):
        print("Invalid n value. Defaulting to 1.")
        n_value = 1
except (ValueError, KeyboardInterrupt):
    print("Invalid input. Defaulting n to 1.")
    n_value = 1

print(f"Using n = {n_value}")

run(
    deployment_name=selected_model,
    print_request=False,
    print_only_content=True,
    n=n_value
)