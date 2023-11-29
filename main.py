from openai import OpenAI

from auth import API_KEY

client = OpenAI(
    api_key = API_KEY,
)

def get_streaming_chat_completion(prompt_text):
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_text}],
        stream=True,
    )
    completion = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            completion += chunk.choices[0].delta.content
    return completion.strip()


def perform_multiple_streaming_completions(prompt_list):
    completions = {}
    for index, prompt in enumerate(prompt_list, start=1):
        completion = get_streaming_chat_completion(prompt)
        completions[f"Prompt {index}: {prompt}"] = completion
    return completions


user_prompts = [
    "Say this is a test",
    "What is the future of artificial intelligence?",
    "Tell me about your favorite book."
]

all_completions = perform_multiple_streaming_completions(user_prompts)

with open("streaming_chat_completions.txt", "w") as file:
    for prompt, completion in all_completions.items():
        file.write(f"{prompt}\n")
        file.write(f"Completion: {completion}\n\n")