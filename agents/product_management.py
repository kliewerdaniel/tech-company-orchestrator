import openai
import os
from dotenv import load_dotenv

class ProductManagementAgent:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def process(self, prompt):
        print("Product Management received the prompt.")

        # Ensure prompt is a dictionary
        if isinstance(prompt, str):
            prompt = {'message': prompt}

        # Extract data from the prompt
        message = prompt.get('message', '')
        code = prompt.get('code', '')
        readme = prompt.get('readme', '')

        # Define product requirements using OpenAI's API
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced product manager adept at translating ideas into detailed "
                        "product requirements and user stories. You focus on delivering value to customers "
                        "while aligning with business objectives and technical feasibility."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Please expand on the following idea by developing comprehensive product requirements. "
                        f"Include user personas, user stories with acceptance criteria, feature prioritization, "
                        f"and success metrics. Ensure the requirements are clear, actionable, and align with "
                        f"modern software development practices.\n\n"
                        f"Idea:\n{message}"
                    )
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )

        # Access response attributes using dot notation
        product_requirements = response.choices[0].message.content

        # Enhance the message by adding product requirements
        enhanced_message = message + "\n\n" + product_requirements

        # Return the updated prompt as a dictionary
        return {'message': enhanced_message, 'code': code, 'readme': readme}
