import json

# Load the data
with open('removed_answer_mcq_data.json', 'r') as f:
    data = json.load(f)

# Function to convert each entry to a complete question text
def convert_to_text(entry):
    question_text = f"Answer the following multiple choices question.\nQuestion: {entry['question']}\nChoices:\n"
    for i, choice in enumerate(entry['choices']):
        question_text += f"{i}: {choice}\n"
    return question_text

# Apply the function to each entry
for entry in data:
    entry['text'] = convert_to_text(entry)
    del entry['question']
    del entry['choices']

# Save the result to a new JSON file
with open('textual_mcq_data.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Data has been saved to textual_mcq_data.json")
