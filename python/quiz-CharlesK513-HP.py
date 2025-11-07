# Sample multiple-choice questions
questions = [
    {
        "question": "Python programming language was created by?",
        "options": ["A. Charles Babbage", "B. Guido Van Rossum", "C. Ada B Loverace", "D. Dennis Ricchie"],
        "answer": "B"
    },
    {
        "question": "Which level of programming language is python?",
        "options": ["A. Low level", "B. Mid level", "C. High level", "D. None of the above"],
        "answer": "C"
    },
    {
        "question": "How many core data types are there in python?",
        "options": ["A. One", "B. Four", "C. Two", "D. Three"],
        "answer": "B"
    }
    {
        "question": "What are the courses opted for in the FCI faculty?",
        "options": ["A. (BIT, BSE, BVE)", "B. (EEE, BCS, BPAM)", "C. (BSE, BCS, BIT)", "D. (FRA, MAS, BCS)"],
        "answer": "C"
    }
]

score = 0

print("Welcome to the Objective Exam!\n")

student_name = input('What is your name, please ') 
print('')

for n,p in enumerate(questions, start = 1):
    print(f"Q{n}. {p['question']}")
    for option in p['options']:
        print(option)
    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    if answer == p['answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {p['answer']}.\n")
print(f"{student_name}, your total score is {score} out of {len(questions)}.")