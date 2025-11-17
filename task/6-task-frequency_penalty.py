from task.app.main import run
from task.util.llm_functions import LlmModelSelection

selector = LlmModelSelection()
selected_model = selector.select_model()
print(f"Using model: {selected_model}")

print(
    "\nThe 'frequency_penalty' parameter penalizes tokens based on their existing frequency in the text.\n"
    "Higher values (0.0 to 2.0) decrease the likelihood of repeating the same line verbatim.\n"
    "Lower values (-2.0 to 0.0) increase repetition.\n"
    "Default value is 0.0.\n"
    "Let's test different values to see how it affects repetition in responses.\n"
)

try:
    frequency_penalty = input("Enter a frequency_penalty value (-2.0 to 2.0) [default is 0.8]: ").strip()
    if frequency_penalty == "":
        frequency_penalty = 0.8
    else:
        frequency_penalty = float(frequency_penalty)
        # Ensure the value is within the valid range
        if frequency_penalty < -2.0 or frequency_penalty > 2.0:
            print("Value out of range. Using default value 0.8 instead.")
            frequency_penalty = 0.8
except (ValueError, KeyboardInterrupt):
    print("\nInvalid input. Defaulting frequency_penalty to 0.8.")
    frequency_penalty = 0.8

print(f"\nUsing frequency_penalty = {frequency_penalty}")
print("Ask a question that might lead to repetitive responses to see the effect.")

run(
    deployment_name=selected_model,
    print_only_content=True,
    frequency_penalty=frequency_penalty
)

# Note: Try comparing responses with different frequency_penalty values:
# Negative values (-1.0 to -2.0): Likely to produce more repetitive text
# Zero (0.0): Default behavior
# Positive values (1.0 to 2.0): Less repetitive, more varied responses
#
# For Anthropic and Gemini models, this parameter might be ignored.