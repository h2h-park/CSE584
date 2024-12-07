import json
import re

with open('response_mcq_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

pattern = re.compile(r'The correct (answer|choice) is', re.IGNORECASE)

filtered_data = []

for item in data:
    if 'response' in item and pattern.search(item['response']):
        filtered_data.append(item)

with open('filtered_response.json', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=4)
