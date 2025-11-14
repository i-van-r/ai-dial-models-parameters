from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# List of models to test
models = [
    'gpt-4o',
    'claude-3-7-sonnet@20250219',
    'gemini-2.5-pro'
]


print("Select a model to run:")
for idx, model in enumerate(models, 1):
    print(f"{idx}. {model}")

try:
    user_input = input(f"Enter the model number (1-{len(models)}) [default 1]: ").strip()
    if user_input == "":
        selected_idx = 1
    else:
        selected_idx = int(user_input)
    if not (1 <= selected_idx <= len(models)):
        print(f"️Invalid selection. Defaulting to: {models[0]}")
        selected_model = models[0]
    else:
        selected_model = models[selected_idx - 1]
except (ValueError, KeyboardInterrupt):
    print(f"️Invalid input. Defaulting to: {models[0]}")
    selected_model = models[0]

print(f"✅ Using model: {selected_model}")

run(
    deployment_name=selected_model,
    print_request=False,
    print_only_content=True
)