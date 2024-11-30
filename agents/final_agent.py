import openai
import os
from dotenv import load_dotenv

class FinalAgent:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def process(self, prompt):
        print("FinalAgent is checking if the process is complete.")

        # Extract data
        message = prompt.get('message', '')
        code = prompt.get('code', '')
        readme = prompt.get('readme', '')

        try:
            # Use OpenAI to determine if the process is complete
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a project manager verifying if a software project is ready for deployment. "
                            "Check if all aspects like product requirements, design specs, code, testing, "
                            "security, and deployment scripts are complete and coherent."
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Based on the following project details, determine if the project is complete and ready "
                            f"for deployment. Provide a 'Yes' or 'No' answer with a brief explanation.\n\n"
                            f"Message:\n{message}\n\nCode:\n{code}\n\nREADME:\n{readme}"
                        )
                    }
                ],
                max_tokens=100,
                temperature=0.0
            )

            # Get the assistant's reply
            assistant_reply = response.choices[0].message.content.strip().lower()
            print(f"FinalAgent's assessment: {assistant_reply}")

            # Decide based on assistant's reply
            if 'yes' in assistant_reply:
                return True
            else:
                return False

        except Exception as e:
            print(f"An error occurred in FinalAgent: {e}")
            raise
