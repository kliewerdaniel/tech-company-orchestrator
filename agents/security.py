import openai
import os
from dotenv import load_dotenv

class SecurityAgent:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def process(self, prompt):
        print("Security received the prompt.")

        # Ensure prompt is a dictionary
        if isinstance(prompt, str):
            prompt = {'message': prompt}

        # Extract data from the prompt
        message = prompt.get('message', '')
        code = prompt.get('code', '')
        readme = prompt.get('readme', '')

        # Analyze code for security vulnerabilities using OpenAI's API
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a cybersecurity expert specializing in application security, threat modeling, "
                        "and secure coding practices. You are proficient in identifying vulnerabilities and "
                        "providing recommendations to enhance security."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Please review the following codebase for security vulnerabilities and provide detailed "
                        f"recommendations for improvements. Your analysis should cover:\n"
                        f"- Common vulnerabilities (e.g., SQL injection, XSS, CSRF)\n"
                        f"- Authentication and authorization mechanisms\n"
                        f"- Data encryption and protection\n"
                        f"- Compliance with security standards (e.g., OWASP Top Ten)\n\n"
                        f"Codebase:\n{code}"
                    )
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )


            # Access response attributes using dot notation
        security_feedback = response.choices[0].message.content

            # Append security improvements to the code
        code += "\n\n# Security Improvements\n" + security_feedback

            # Update README with security considerations
        readme += "\n## Security\nDetails on security measures implemented."

            # Print debug info
        print(f"SecurityAgent updated code length: {len(code)}")

            # Return the updated prompt as a dictionary
        return {'message': message, 'code': code, 'readme': readme}    