from task.app.main import run
from task.util.llm_functions import LlmModelSelection

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

llmSelector = LlmModelSelection()
selected_model = llmSelector.select_model()

print(f"✅ Using model: {selected_model}")

run(
    deployment_name=selected_model,
    print_request=False,
    print_only_content=True
)