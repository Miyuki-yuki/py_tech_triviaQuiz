import sys

class Question:
    def __init__(self, prompt, answer, correct_answer_text, options, id):
        self.prompt = prompt
        self.answer = answer
        self.correct_answer_text = correct_answer_text
        self.options = options
        self.id = id


# Initialize questions with all required attributes
questions = [
    Question(
        prompt="Which country first started using emojis in their digital communications?",
        answer="b",
        correct_answer_text="Japan",
        options=["United States", "Japan", "South Korea", "China"],
        id="fun_question1"
    ),
    Question(
        prompt="What was Google's original name?",
        answer="b",
        correct_answer_text="Backrub",
        options=["Googol", "Backrub", "WebSearch", "ByteDance"],
        id="fun_question2"
    ),
    Question(
        prompt="Which was the first commercially successful video game?",
        answer="a",
        correct_answer_text="Pong",
        options=["Pong", "Pac-Man", "Space Invaders", "Super Mario Bros"],
        id="fun_question3"
    ),
    Question(
        prompt="What is the name of the first ever artificial satellite launched into space?",
        answer="b",
        correct_answer_text="Sputnik",
        options=["Voyager", "Sputnik", "Apollo", "Hubble"],
        id="fun_question4"
    ),
    Question(
        prompt="In the movie 'The Matrix', what color is the pill Neo takes?",
        answer="a",
        correct_answer_text="Red",
        options=["Red", "Blue", "Green", "Yellow"],
        id="fun_question5"
    ),
    Question(
        prompt="Who was the first person to reach 1 million Twitter followers?",
        answer="c",
        correct_answer_text="Ashton Kutcher",
        options=["Barack Obama", "Justin Bieber", "Ashton Kutcher", "Lady Gaga"],
        id="fun_question6"
    ),
    Question(
        prompt="The Apple logo is a tribute to which historical figure?",
        answer="a",
        correct_answer_text="Isaac Newton",
        options=["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Thomas Edison"],
        id="fun_question7"
    ),
    Question(
        prompt="What does 'IoT' stand for in the world of technology?",
        answer="a",
        correct_answer_text="Internet of Things",
        options=["Internet of Things", "Integration of Technology", "Internal Online Transfer", "International Operational Tech"],
        id="fun_question8"
    ),
    Question(
        prompt="What was the first smartphone to use the Android operating system?",
        answer="a",
        correct_answer_text="HTC Dream",
        options=["HTC Dream", "Samsung Galaxy", "Motorola Droid", "Sony Xperia"],
        id="fun_question9"
    ),
    Question(
        prompt="Who is considered a pioneer in Virtual Reality technology?",
        answer="c",
        correct_answer_text="Palmer Luckey",
        options=["Mark Zuckerberg", "Steve Jobs", "Palmer Luckey", "Elon Musk"],
        id="fun_question10"
    ),
    Question(
        prompt="What was the first product ever sold on Amazon?",
        answer="a",
        correct_answer_text="A book",
        options=["A book", "A CD", "A VHS tape", "A computer mouse"],
        id="fun_question11"
    ),
    Question(
        prompt="Who is known as the 'Mother of Computing'?",
        answer="a",
        correct_answer_text="Ada Lovelace",
        options=["Ada Lovelace", "Grace Hopper", "Joan Clarke", "Hedy Lamarr"],
        id="fun_question12"
    ),
    Question(
        prompt="In computing, what does 'USB' stand for?",
        answer="a",
        correct_answer_text="Universal Serial Bus",
        options=["Universal Serial Bus", "United System Box", "Universal System Backup", "Unified Serial Bridge"],
        id="fun_question13"
    ),
    Question(
        prompt="What was the first image ever posted on the Internet?",
        answer="b",
        correct_answer_text="A band's promotional photo",
        options=["A cat", "A band's promotional photo", "A science experiment", "A world map"],
        id="fun_question14"
    ),
    Question(
        prompt="Which year was Wi-Fi invented?",
        answer="c",
        correct_answer_text="1997",
        options=["1985", "1991", "1997", "2003"],
        id="fun_question15"
    ),
]

def run_quiz(questions, num_questions):
    score = 0
    for question in questions[:num_questions]:
        print(question.prompt)
        for i, option in enumerate(question.options, start=1):
            print(f"({chr(96 + i)}) {option}")
        answer = input("Your answer: ")
        if answer.lower() == chr(96 + question.options.index(question.correct_answer_text) + 1):
            print("**Correct!**")
            score += 1
        else:
            print(f"**Incorrect. The correct answer is: {question.correct_answer_text}**")
    print(f"You got {score}/{num_questions} correct")

if __name__ == "__main__":
    num_questions = 15  # default number of questions
    if len(sys.argv) > 1:
        num_questions = int(sys.argv[1])
    run_quiz(questions, num_questions)
