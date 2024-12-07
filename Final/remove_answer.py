import json

# Load the data
with open('mcq_data.json', 'r') as f:
    data = json.load(f)

# Function to remove the correct answer from choices
def remove_correct_answer(entry):
    choices = entry['choices']
    correct_answer = entry['answer']
    del choices[correct_answer]  # Remove the correct answer
    return choices

# Apply the function to each entry
for entry in data:
    entry['choices'] = remove_correct_answer(entry)

# Select the required fields
output_data = [{'index': entry['index'], 'question': entry['question'], 'choices': entry['choices'], 'discipline': entry['discipline'], 'no': entry['no']} for entry in data]

# Save the result to a new JSON file
with open('removed_answer_mcq_data.json', 'w') as f:
    json.dump(output_data, f, indent=4)
