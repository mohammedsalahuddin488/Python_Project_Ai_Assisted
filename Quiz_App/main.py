def run_quiz():
    questions = [
        {           "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Ernest Hemingway"],
            "answer": "A"
        }
    ]
    score = 0
    for index, q in enumerate(questions): # enumerate 
        print(f"Question {index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
        print()

run_quiz()
