from openai import OpenAI

# Replace with your API key
client = OpenAI(api_key="YOUR_API_KEY")

print("=" * 50)
print("      AI Programming Assistant")
print("=" * 50)

while True:
    request = input("\nEnter your programming request (or type 'exit'): ")

    if request.lower() == "exit":
        print("Goodbye!")
        break

    prompt = f"""
You are an expert programming assistant.

Your job is to generate correct, efficient, and legal code.

Instructions:
- Write programs in Python, C, C++, Java, JavaScript, HTML, CSS, SQL, PHP, C#, Go, Rust and other languages.
- Provide complete, well-formatted code.
- Explain the code in simple language.
- Include comments.
- Suggest improvements.
- Help debug errors.
- Generate only legal and safe code.
- Never generate malware or harmful software.
- Provide sample input/output if applicable.
- Give compile/run instructions.

User Request:
{request}
"""

    try:
        response = client.responses.create(
            model="gpt-5.5",
            input=prompt
        )

        print("\n" + "=" * 50)
        print(response.output_text)
        print("=" * 50)

    except Exception as e:
        print("Error:", e)