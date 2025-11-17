from task.app.main import run

# List of available models for this task
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

# Explanation of temperature parameter
print(
    "\nThe 'temperature' parameter controls the randomness/creativity of the model's output.\n"
    " - Lower values (e.g., 0.0) make the output more deterministic and focused.\n"
    " - Higher values (e.g., 1.0 or above) make the output more random and creative.\n"
    " - Typical range: 0.0 to 2.0 (default is 1.0).\n"
    "Try values between 0.0 and 1.0 for this task. (You can also try 2.1 to see what happens!)\n"
)

# Temperature parameter selection
try:
    temp_input = input("Enter the temperature value (0.0–2.0) [default 1.0]: ").strip()
    if temp_input == "":
        temperature = 1.0
    else:
        temperature = float(temp_input)
    if not (0.0 <= temperature <= 2.0):
        print("Temperature out of recommended range (0.0–2.0). Proceeding anyway.")
except (ValueError, KeyboardInterrupt):
    print("\nInvalid input. Defaulting temperature to 1.0.")
    temperature = 1.0

print(f"Using temperature = {temperature}")

run(
    deployment_name=selected_model,
    print_only_content=True,
    temperature=temperature
)