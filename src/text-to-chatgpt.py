import openai
import os

# Set up your API token
openai.api_key = os.getenv('OPENAI_API_KEY')

# Submit a prompt to ChatGPT
response = openai.Completion.create(
  engine="davinci",
  prompt="What is the population of the world?",
  max_tokens=50
)

# Print the response
print(response.choices[0].text.strip())

# import requests

# # Set the API endpoint
# endpoint = "https://api.openai.com/v1/completions"

# # Set the headers with your API key
# headers = {
#     "Authorization": "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",
#     "Content-Type": "application/json"
# }

# # Define the prompt and model parameters
# data = {
#     "prompt": "What is the population of the world?",
#     "model": "text-davinci-003",
#     "max_tokens": 100
# }

# # Make the API request
# response = requests.post(endpoint, json=data, headers=headers)

# # Get the text response 
# text = response.json()['choices'][0]['text']

# print(text)
