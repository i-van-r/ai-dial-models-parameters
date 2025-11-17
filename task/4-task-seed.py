from task.app.main import run
from task.util.llm_functions import LlmModelSelection

selector = LlmModelSelection()
selected_model = selector.select_model()
print(f"Using model: {selected_model}")

print(
    "\nThe 'seed' parameter makes the model's output more deterministic (less random).\n"
    "If you use the same seed and prompt, you should get the same result each time.\n"
    "Common seeds: 42, 123, 1000. Default is None (random).\n"
    "Note: For Anthropic and Gemini models, this parameter will be ignored.\n"
)

try:
    seed_input = input("Enter a seed value (integer) [default 42]: ").strip()
    if seed_input == "":
        seed_value = 42
    else:
        seed_value = int(seed_input)
except (ValueError, KeyboardInterrupt):
    print("\nInvalid input. Defaulting seed to 42.")
    seed_value = 42

print(f"Using seed = {seed_value}")
print("n is set to 5 (number of completions per request)")

run(
    deployment_name=selected_model,
    print_only_content=True,
    seed=seed_value,
    n=5
)