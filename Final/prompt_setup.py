import json

# Load the data
with open('final_mcq_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Function to add new text1 field
def add_text1(item):
    text_parts = item['text'].split("Question:")
    new_text = text_parts[0] + "There may be no right answer.\nQuestion:" + text_parts[1]
    item['text1'] = new_text
    return item

# Function to add new text2 field
def add_text2(item):
    item['text2'] = item['text'] + "3: None of the above\n"
    return item

# Function to add new text3 field
def add_text3(item):
    example_text = "Example 1) \nQuestion: What is 1+1? \nChoices:\n0: 1\n1: 2\n2: 3\nResponse: The correct answer is 1: 2\n" \
                   "Example 2) \nQuestion: What is the last digit of pi? \nChoices:\n0: 1\n1: 3\n2: 5\nResponse: The correct answer is not in the provided choices.\n"
    item['text3'] = example_text + item['text']
    return item

# Apply the new fields to each item in the data
for item in data:
    add_text1(item)
    add_text2(item)
    add_text3(item)

# Save the modified data to a new JSON file
with open('prompted_mcq_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

