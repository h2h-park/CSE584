# CSE584 Final Project
## Overview
This project focuses on generating faulty scientific questions designed to deceive top-performing Large Language Models (LLMs). The ultimate goal is to construct a dataset that enables creative research and design research about how LLMs handle these faulty questions.

### Key Objective
The strategy for generating faulty scientific questions in this project focuses on multiple-choice questions. Starting with existing multiple-choice question datasets, the correct answer was deliberately removed from the choices and reintroduced to the LLM. If the LLM still provides the correct answer despite the missing correct choice, it indicates that the model has been "fooled", and the question is classified as part of our desired faulty question dataset.

## Disciplines and Dataset Composition
I curated faulty questions across **15 disciplines** to ensure diversity and a broad scope of testing. For each discipline, **60 faulty questions** were generated, resulting in a dataset containing **900 questions** in total with no **standard deviation** on the number of questions over all disciplines.

The selected disciplines are as follows:
- `Anatomy`
- `Astronomy`
- `College Biology`
- `College Chemistry`
- `College Computer Science`
- `College Mathematics`
- `College Medicine`
- `College Physics`
- `Computer Security`
- `Econometrics`
- `Electrical Engineering`
- `Machine Learning`
- `Medical Genetics`
- `Nutrition`
- `Virology`

## Methodology
1. **Faulty Questions Generation**: Starting with existing multiple-choice question datasets [MMLU Dataset](https://huggingface.co/datasets/Stevross/mmlu), we removed the correct answers from the choices. 
2. **LLM Evaluation**: These faulty questions were input into the LLM to determine whether it could still output the correct answers.
3. **Desired Dataset**: Questions where the LLM still output the correct answer despite the faulty setup were categorized as part of the final faulty questions dataset.

## Dataset Access
The complete dataset of **900 faulty scientific questions** in **15 disciplines** is publicly available. You can explore the dataset using the following link:

[Faulty Scientific Question Dataset - Google Sheets](https://docs.google.com/spreadsheets/d/15m83rfH7xvT8_nyAe1_D5IdGDN4mhVDlLkLRdPsUiVc/edit?gid=0#gid=0)

## Research Design
This project evaluates the effectiveness of three distinct prompting strategies in mitigating faulty questions:

1. **Scenario 1: Adding a Hint**  
   - Adds the sentence: "There may be no right answer" to the prompt.  
   - **Goal**: Encourage the LLM to consider the possibility of no correct answer.

2. **Scenario 2: Adding an Explicit Option**  
   - Adds a new option: "None of the above" to the choices.  
   - **Goal**: Provide a clear and actionable alternative for the LLM.

3. **Scenario 3: In-Context Learning**  
   - Presents two example questions before the main question: one with a valid answer and one faulty question with no answer.  
   - **Goal**: Use context to guide the LLM’s reasoning process.

## Report
You can access the full report here:  
[CSE584_Final_Project.pdf](./CSE584_Final_Project.pdf)


## Tools and Libraries
- **Programming Language**: Python
- **Main Libraries**: Hugging Face Transformers, Pandas, NumPy, Matplotlib
- **LLM**: GPT-4o-mini
