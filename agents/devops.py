import openai
import os
from dotenv import load_dotenv

class DevOpsAgent:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def process(self, prompt):
        print("DevOps received the prompt.")

        # Ensure prompt is a dictionary
        if isinstance(prompt, str):
            prompt = {'message': prompt}

        # Extract data from the prompt
        message = prompt.get('message', '')
        code = prompt.get('code', '')
        readme = prompt.get('readme', '')

        # Generate deployment scripts using OpenAI's API
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a seasoned DevOps engineer with expertise in designing and implementing "
                        "CI/CD pipelines, infrastructure as code, and scalable deployment strategies. "
                        "You are familiar with cloud platforms (AWS, Azure, GCP), containerization, and "
                        "orchestration tools like Docker and Kubernetes."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Based on the following codebase, please create comprehensive deployment scripts "
                        f"and CI/CD pipelines. Ensure the infrastructure is scalable, secure, and follows "
                        f"best practices. Your deliverables should include:\n"
                        f"- Infrastructure as Code (IaC) scripts (e.g., Terraform, CloudFormation)\n"
                        f"- CI/CD pipeline configurations (e.g., Jenkinsfile, GitHub Actions workflows)\n"
                        f"- Deployment scripts (e.g., Dockerfiles, Kubernetes manifests)\n\n"
                        f"Codebase:\n{code}"
                    )
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )


            # Access response attributes using dot notation
        devops_code = response.choices[0].message.content

            # Append DevOps scripts to the code
        code += "\n\n# DevOps Scripts and Configurations\n" + devops_code

            # Update README with deployment instructions
        readme += "\n## Deployment\nInstructions on deployment and CI/CD."

            # Print debug info
        print(f"DevOpsAgent updated code length: {len(code)}")

            # Return the updated prompt as a dictionary
        return {'message': message, 'code': code, 'readme': readme}