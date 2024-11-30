import openai
import os
from dotenv import load_dotenv

class EngineeringAgent:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def process(self, prompt):
        print("Engineering received the prompt.")

        # Ensure prompt is a dictionary
        if isinstance(prompt, str):
            prompt = {'message': prompt}

        # Extract data
        message = prompt.get('message', '')
        code = prompt.get('code', '')
        readme = prompt.get('readme', '')

        # Generate code using OpenAI's API
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a senior software engineer with expertise in designing and developing "
                        "high-quality, scalable, and maintainable software solutions. You follow best practices "
                        "in software architecture, design patterns, code documentation, and testing."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Using the following specifications, please develop the software application. "
                        f"Ensure the code is well-documented, follows coding standards, and includes unit tests. "
                        f"Consider performance, scalability, and maintainability in your implementation.\n\n"
                        f"Specifications:\n{message}"
                    )
                }
            ],
            max_tokens=1500,
            temperature=0.7
        )

 # Access response attributes using dot notation
        engineering_code = response.choices[0].message.content

            # Append or initialize the code
        if code:
                code += "\n\n# Engineering Code\n" + engineering_code
        else:
                code = "# Engineering Code\n" + engineering_code

            # Update README placeholder
        readme += "\n## Project Documentation\n\n"

            # Print debug info
        print(f"EngineeringAgent updated code length: {len(code)}")

            # Return the updated prompt as a dictionary
        return {'message': message, 'code': code, 'readme': readme}
