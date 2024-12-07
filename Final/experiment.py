import json
from openai import OpenAI
import time

# Load the data
with open('prompted_mcq_data.json', 'r') as f:
    data = json.load(f)

# Function to get response from GPT-4
def get_gpt4_response(client, question_text):
    messages = [
        {"role": "system", "content": "Complete the given sentence."},
        
        {"role": "user", "content": question_text}
    ]
    completion  = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        temperature=0.7
    )
    return completion.choices[0].message.content.strip()


openai_client = OpenAI(
    api_key=''
)

# Apply the function to each entry in batches
batch_size = 100  # Adjust batch size as needed
for i in range(0, len(data), batch_size):
    batch = data[i:i + batch_size]
    for entry in batch:
        entry['response1'] = get_gpt4_response(openai_client, entry['text1'])
        entry['response2'] = get_gpt4_response(openai_client, entry['text2'])
        entry['response3'] = get_gpt4_response(openai_client, entry['text3'])
        time.sleep(1)

# Save the result to a new JSON file
with open('final_response.json', 'w') as f:
    json.dump(data, f, indent=4)

