from task.app.main import run

# List of available models
models = [
    'gpt-4o',
    'claude-3-7-sonnet@20250219',
    'gemini-2.5-pro'
]

print("Select a model to run:")
for idx, model in enumerate(models, 1):
    print(f"{idx}. {model}")

# Model selection
try:
    user_input = input(f"Enter the model number (1-{len(models)}) [default 1]: ").strip()
    if user_input == "":
        selected_idx = 1
    else:
        selected_idx = int(user_input)
    if not (1 <= selected_idx <= len(models)):
        print(f"Invalid selection. Defaulting to: {models[0]}")
        selected_model = models[0]
    else:
        selected_model = models[selected_idx - 1]
except (ValueError, KeyboardInterrupt):
    print(f"Invalid input. Defaulting to: {models[0]}")
    selected_model = models[0]

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