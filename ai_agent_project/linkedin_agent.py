from langchain.prompts import PromptTemplate

# Mock LLM class to simulate AI output (free version)
class MockLLM:
    def __call__(self, prompt):
        # Generates a fake LinkedIn post for demo
        return (
            "🌟 LinkedIn Post 🌟\n\n"
            f"Topic: {prompt.split('\"')[1]}\n\n"
            "This is a professional LinkedIn-style post generated for demo purposes. "
            "It is structured, engaging, and written in the requested language. "
            "You can replace this mock with a real LLM later for real AI outputs."
        )

# Initialize the mock LLM
llm = MockLLM()

# Define the prompt template
template = """
You are a professional LinkedIn content writer.
Write a LinkedIn post about "{topic}" in {language}.
The post should:
- Be professional but engaging
- Use storytelling or insights where possible
- Length: 2 to 4 paragraphs
- Avoid hashtags and emojis
"""

prompt = PromptTemplate(
    input_variables=["topic", "language"],
    template=template
)

# Function to generate LinkedIn post
def generate_linkedin_post(topic, language="English"):
    final_prompt = prompt.format(topic=topic, language=language)
    response = llm(final_prompt)
    return response

# Main program
if __name__ == "__main__":
    topic = input("Enter topic: ")
    language = input("Enter language (English, Bengali, Spanish): ")
    post = generate_linkedin_post(topic, language)
    print("\n🔹 Generated LinkedIn Post:\n")
    print(post)
