import pandas as pd
from datasets import load_dataset
import json

# List of tasks
# tasks = ['abstract_algebra', 'anatomy', 'astronomy', 'business_ethics', 'clinical_knowledge', 
#          'college_biology', 'college_chemistry', 'college_computer_science', 'college_mathematics', 
#          'college_medicine', 'college_physics', 'computer_security', 'conceptual_physics', 
#          'econometrics', 'electrical_engineering', 'elementary_mathematics', 'formal_logic', 
#          'global_facts', 'high_school_biology', 'high_school_chemistry', 'high_school_computer_science', 
#          'high_school_european_history', 'high_school_geography', 'high_school_government_and_politics', 
#          'high_school_macroeconomics', 'high_school_mathematics', 'high_school_microeconomics', 
#          'high_school_physics', 'high_school_psychology', 'high_school_statistics', 'high_school_us_history', 
#          'high_school_world_history', 'human_aging', 'human_sexuality', 'international_law', 'jurisprudence', 
#          'logical_fallacies', 'machine_learning', 'management', 'marketing', 'medical_genetics', 
#          'miscellaneous', 'moral_disputes', 'moral_scenarios', 'nutrition', 'philosophy', 'prehistory', 
#          'professional_accounting', 'professional_law', 'professional_medicine', 'professional_psychology', 
#          'public_relations', 'security_studies', 'sociology', 'us_foreign_policy', 'virology', 'world_religions']

# some scientific tasks
tasks = ['anatomy', 'astronomy','college_biology', 'college_chemistry', 'college_computer_science', 'college_mathematics', 
          'college_medicine', 'college_physics', 'computer_security', 'econometrics', 'electrical_engineering', 'machine_learning'
          , 'medical_genetics', 'nutrition', 'virology']

# Initialize an empty list to store all data
all_data = []

# Extract and save data from 'test', 'validation', and 'dev' splits for each task
for task in tasks:
    dataset = load_dataset('Stevross/mmlu', task)
    task_index = 0
    for split in ['test', 'validation', 'dev']:
        if split in dataset:
            for i, row in enumerate(dataset[split]):
                row_data = {
                    'index': len(all_data) + 1,
                    'question': row['question'],
                    'choices': row['choices'],
                    'answer': row['answer'],
                    'discipline': task,
                    'no': task_index + 1
                }
                all_data.append(row_data)
                task_index += 1

# Save the combined data to 'mcq_data.json'
with open('mcq_data.json', 'w') as f:
    json.dump(all_data, f, indent=4)

print("All data has been saved to mcq_data.json")
