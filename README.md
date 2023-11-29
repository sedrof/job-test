OpenAI Chat Completion Python Script
This Python script demonstrates how to interact with OpenAI's Chat Completion API using the OpenAI Python library. It showcases two methods of generating chat completions: the standard completion method and the streaming completion method.

Features
Standard Completion Method:

Uses the regular Chat Completion API endpoint.
Iterates through a list of prompts and generates completions for each prompt.
Saves completions to a file.
Streaming Completion Method:

Utilizes the streaming API to receive completions in chunks.
Iterates through a list of prompts and aggregates the received completion chunks.
Saves completions to a file.
Getting Started
Prerequisites:

Python installed on your system.
openai Python package installed (pip install -r requirements.txt).
Setup:

Create an auth.py file and add your OpenAI API key (See auth_example.py for format).
Running the Script:

Execute python main.py to run the script.
Adjust the user_prompts list in main.py to customize prompts.
Output:

The script saves chat completions to streaming_chat_completions.txt.
File Structure
auth.py: Contains your OpenAI API key.
main.py: The main Python script demonstrating chat completions.
.env: API Keys
.gitignore: Ignores the venv directory to exclude virtual environment files.
Author
Abdulla
