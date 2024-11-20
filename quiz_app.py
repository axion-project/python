# Quiz App: Test Your Programming Knowledge
# By Michael Morales

def show_banner():
    """
    Displays the welcome banner for the quiz app.
    """
    print("""
    ***********************************************
    *         Programming Languages Quiz          *
    *    Test your coding knowledge and have fun! *
    ***********************************************
    """)

def load_questions():
    """
    Returns a list of quiz questions, options, and answers.
    """
    return [
        {
            "question": "Which language is primarily used for web development?",
            "options": ["1. Python", "2. Java", "3. JavaScript", "4. C++"],
            "answer": 3
        },
        {
            "question": "Which programming language is known as the language of AI?",
            "options": ["1. Ruby", "2. Python", "3. C", "4. PHP"],
            "answer": 2
        },
        {
            "question": "Which language is used to style web pages?",
            "options": ["1. HTML", "2. CSS", "3. JavaScript", "4. SQL"],
            "answer": 2
        },
        {
            "question": "Which of the following is a low-level programming language?",
            "options": ["1. Python", "2. Assembly", "3. Ruby", "4. Swift"],
            "answer": 2
        },
        {
            "question": "Which language is known for its 'write once, run anywhere' capability?",
            "options": ["1. C#", "2. Java", "3. Kotlin", "4. Perl"],
            "answer": 2
        }
    ]

def ask_question(question_data, question_number):
    """
    Asks a single question, displays options, and gets the user's answer.
    """
    print(f"\nQuestion {question_number}: {question_data['question']}")
    for option in question_data["options"]:
        print(option)
    
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if 1 <= answer <= len(question_data["options"]):
                return answer == question_data["answer"]
            else:
                print("Please enter a valid option number!")
        except ValueError:
            print("Invalid input! Please enter a number.")

def quiz_app():
    """
    Main function to run the quiz app.
    """
    show_banner()
    questions = load_questions()
    score = 0

    print("\nWelcome to the Programming Languages Quiz!")
    print("Answer the following questions to the best of your ability.\n")

    for i, question_data in enumerate(questions, start=1):
        correct = ask_question(question_data, i)
        if correct:
            print("✅ Correct! Great job!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was option {question_data['answer']}.")

    print("\n🎉 Quiz Complete! 🎉")
    print(f"Your final score is: {score}/{len(questions)}")
    if score == len(questions):
        print("🥳 Excellent! You're a programming expert!")
    elif score > len(questions) // 2:
        print("😊 Good job! Keep improving your knowledge!")
    else:
        print("😅 Keep practicing! You'll get there!")

if __name__ == "__main__":
    quiz_app()
