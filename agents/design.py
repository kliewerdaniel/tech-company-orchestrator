import openai
import os
from dotenv import load_dotenv

class DesignAgent:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def process(self, prompt):
        print("Design received the prompt.")

        # Ensure prompt is a dictionary
        if isinstance(prompt, str):
            prompt = {'message': prompt}

        # Extract data from the prompt
        message = prompt.get('message', '')
        code = prompt.get('code', '')
        readme = prompt.get('readme', '')

        # Generate design specifications using OpenAI's API
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced UI/UX designer specializing in creating intuitive, "
                        "accessible, and aesthetically pleasing interfaces for web and mobile applications. "
                        "You are up-to-date with modern design trends, tools, and technologies, and you "
                        "prioritize user-centered design principles."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Based on the detailed product requirements below, please create comprehensive "
                        f"UI/UX design specifications. Your deliverables should include:\n"
                        f"- High-fidelity wireframes\n"
                        f"- User flow diagrams\n"
                        f"- Interactive prototypes (if applicable)\n"
                        f"- Style guides with color schemes, typography, and component libraries\n\n"
                        f"Product Requirements:\n{message}"
                    )
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )

        # Access response attributes using dot notation
        design_spec = response.choices[0].message.content

        # Enhance the message by adding the design specifications
        enhanced_message = message + "\n\n" + design_spec

        # Return the updated prompt as a dictionary
        return {'message': enhanced_message, 'code': code, 'readme': readme}
