# filename: tech_trivia_quiz.py
import sys

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions_prompts = [
    "What does CPU stand for?\n(a) Central Process Unit\n(b) Central Processor Unit\n(c) Central Processing Unit\n(d) Central Processed Unit\n",
    "In web design, what does CSS stand for?\n(a) Cascading Style Sheet\n(b) Computer Style Sheet\n(c) Cascading Style Script\n(d) Computer Style Script\n",
    "What language is a standard for relational database management systems?\n(a) Ruby\n(b) Python\n(c) SQL\n(d) Java\n",
    "What does the 'MP' stand for in MP3?\n(a) Moving Picture\n(b) Music Player\n(c) Multi Pass\n(d) Micro Point\n",
    "Which language is used for web apps?\n(a) PHP\n(b) Python\n(c) Java\n(d) All\n",
]

questions = [
    Question(questions_prompts[0], "c"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "c"),
    Question(questions_prompts[3], "a"),
    Question(questions_prompts[4], "d"),
]

def run_quiz(questions, num_questions):
    score = 0
    for question in questions[:num_questions]:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{num_questions} correct")

if __name__ == "__main__":
    num_questions = 5  # default number of questions
    if len(sys.argv) > 1:
        num_questions = int(sys.argv[1])
    run_quiz(questions, num_questions)