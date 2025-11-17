

class LlmModelSelection:

    def __init__(self):
        # List of models to test
        self.models = [
            'gpt-4o',
            'claude-3-7-sonnet@20250219',
            'gemini-2.5-pro'
        ]


    def select_model(self):
        print("Select a model to run:")
        for idx, model in enumerate(self.models, 1):
            print(f"{idx}. {model}")

        try:
            user_input = input(f"Enter the model number (1-{len(self.models)}) [default 1]: ").strip()
            if user_input == "":
                selected_idx = 1
            else:
                selected_idx = int(user_input)
            if not (1 <= selected_idx <= len(self.models)):
                print(f"️Invalid selection. Defaulting to: {self.models[0]}")
                selected_model = self.models[0]
            else:
                selected_model = self.models[selected_idx - 1]
        except (ValueError, KeyboardInterrupt):
            print(f"️Invalid input. Defaulting to: {self.models[0]}")
            selected_model = self.models[0]
        return selected_model