from task.app.main import run
from task.util.llm_functions import LlmModelSelection

llmSelector = LlmModelSelection()
selected_model = llmSelector.select_model()

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