import openai
import os
from dotenv import load_dotenv

class TestingAgent:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def process(self, prompt):
        print("Testing received the prompt.")

        # Ensure prompt is a dictionary
        if isinstance(prompt, str):
            prompt = {'message': prompt}

        # Extract data from the prompt
        message = prompt.get('message', '')
        code = prompt.get('code', '')
        readme = prompt.get('readme', '')

        # Generate test cases using OpenAI's API
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a QA engineer specializing in software testing, including unit testing, "
                        "integration testing, and automated testing frameworks. You ensure software quality "
                        "and reliability by writing comprehensive test cases."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Based on the following codebase, please develop comprehensive test cases. "
                        f"Your deliverables should include:\n"
                        f"- Unit tests covering all critical functions\n"
                        f"- Integration tests for key components\n"
                        f"- Suggestions for automated testing frameworks (e.g., pytest, JUnit)\n\n"
                        f"Codebase:\n{code}"
                    )
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )

            # Access response attributes using dot notation
        test_code = response.choices[0].message.content

            # Append test code to the original code
        code += "\n\n# Test Cases\n" + test_code

            # Update README with testing instructions
        readme += "\n## Testing\nInstructions on how to run the tests."

            # Print debug info
        print(f"TestingAgent updated code length: {len(code)}")

            # Return the updated prompt as a dictionary
        return {'message': message, 'code': code, 'readme': readme}

