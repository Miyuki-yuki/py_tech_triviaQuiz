# filename: tech_trivia_quiz.py
import sys

class Question:
    def __init__(self, prompt, answer, correct_answer_text):
        self.prompt = prompt
        self.answer = answer
        self.correct_answer_text = correct_answer_text

questions_prompts = [
    "What does CPU stand for?\n(a) Central Process Unit\n(b) Central Processor Unit\n(c) Central Processing Unit\n(d) Central Processed Unit\n",
    "In web design, what does CSS stand for?\n(a) Cascading Style Sheet\n(b) Computer Style Sheet\n(c) Cascading Style Script\n(d) Computer Style Script\n",
    "What language is a standard for relational database management systems?\n(a) Ruby\n(b) Python\n(c) SQL\n(d) Java\n",
    "What does the 'MP' stand for in MP3?\n(a) Moving Picture\n(b) Music Player\n(c) Multi Pass\n(d) Micro Point\n",
    "Which language is used for web apps?\n(a) PHP\n(b) Python\n(c) Java\n(d) All\n",
    "What is the primary purpose of an operating system?\n(a) Manage Hardware\n(b) Run Applications\n(c) Security\n(d) All of the above\n",
    "What is the extension for Python files?\n(a) .py\n(b) .pt\n(c) .pn\n(d) .pm\n",
    "What does HTTP stand for?\n(a) HyperText Transfer Protocol\n(b) Hyper Transfer Text Protocol\n(c) High-Level Text Transfer Protocol\n(d) HyperText Technical Protocol\n",
    "What is the main function of the ALU (Arithmetic Logic Unit)?\n(a) Perform arithmetic and logical operations\n(b) Manage memory and storage\n(c) Control input and output devices\n(d) Fetch instructions from memory\n",
    "What is a common use for Python?\n(a) Web Development\n(b) Data Analysis\n(c) Artificial Intelligence\n(d) All of the above\n",
    "What does GPU stand for?\n(a) General Processing Unit\n(b) Graphical Processing Unit\n(c) Graphical Performance Unit\n(d) General Purpose Unit\n",
    "What is the primary purpose of a database?\n(a) Store data\n(b) Retrieve data\n(c) Manage data\n(d) All of the above\n",
    "What does the acronym 'RAM' stand for?\n(a) Random Access Memory\n(b) Read Access Memory\n(c) Randomly Allocated Memory\n(d) Read Allocated Memory\n",
    "What language is primarily used for handling the back-end of web applications?\n(a) JavaScript\n(b) HTML\n(c) SQL\n(d) PHP\n",
    "What is a key characteristic of Object-Oriented Programming (OOP)?\n(a) Encapsulation\n(b) Inheritance\n(c) Polymorphism\n(d) All of the above\n",

]

questions = [
    Question(questions_prompts[0], "c", "Central Processing Unit"),
    Question(questions_prompts[1], "a", "Cascading Style Sheet"),
    Question(questions_prompts[2], "c", "SQL"),
    Question(questions_prompts[3], "a", "Moving Picture"),
    Question(questions_prompts[4], "d", "All"),
    Question(questions_prompts[5], "d", "All of the above"),
    Question(questions_prompts[6], "a", ".py"),
    Question(questions_prompts[7], "a", "HyperText Transfer Protocol"),
    Question(questions_prompts[8], "a", "Perform arithmetic and logical operations"),
    Question(questions_prompts[9], "d", "All of the above"),
    Question(questions_prompts[10], "b", "Graphical Processing Unit"),
    Question(questions_prompts[11], "d", "All of the above"),
    Question(questions_prompts[12], "a", "Random Access Memory"),
    Question(questions_prompts[13], "d", "PHP"),
    Question(questions_prompts[14], "d", "All of the above"),

]

def run_quiz(questions, num_questions):
    score = 0
    for question in questions[:num_questions]:
        answer = input(question.prompt)
        if answer == question.answer:
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
