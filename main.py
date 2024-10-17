from data_handler import load_questions

# Specify the JSON filename
filename = 'questions.json'

# Load questions from the JSON file
questions = load_questions(filename)

# Display the loaded questions
for question in questions:
    print(f"Q: {question['question']}")
    for option in question['options']:
        print(f"   - {option}")
    print(f"Answer: {question['answer']}\n")
