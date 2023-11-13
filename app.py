from flask import Flask, render_template, request, session
import tech_trivia_quiz
from random import shuffle

app = Flask(__name__)
app.secret_key = 'httt12345'  # Use a secure, secret key for production

@app.route('/')
def index():
    # Start with a fresh session each time the user reaches the home page
    session.clear()
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    feedback = None
    correct_answer_text = None

    # Initialize the quiz and shuffle the questions
    if 'current_question' not in session:
        session['current_question'] = 0
        session['score'] = 0
        # Shuffling the indices instead of the questions themselves
        question_indices = list(range(len(tech_trivia_quiz.questions)))
        shuffle(question_indices)
        session['question_order'] = question_indices

    if request.method == 'POST':
        # Retrieve the answer and the index of the current question
        submitted_answer = request.form['answer']
        current_index = session['question_order'][session['current_question']]
        question = tech_trivia_quiz.questions[current_index]
        correct_answer = question.answer
        correct_answer_text = question.correct_answer_text

        # Check if the submitted answer is correct
        if submitted_answer.lower() == correct_answer.lower():
            session['score'] += 1
            feedback = "Correct!"
        else:
            feedback = f"Incorrect! The correct answer was {correct_answer_text}."

        # Prepare for the next question
        session['current_question'] += 1

    # If all questions have been answered, show the results
    if session['current_question'] >= len(tech_trivia_quiz.questions):
        score = session.pop('score', None)
        session.clear()  # Clear the session for a fresh start
        return render_template('result.html', score=score, total=len(tech_trivia_quiz.questions))

    # Present the next question
    current_index = session['question_order'][session['current_question']]
    question = tech_trivia_quiz.questions[current_index]
    return render_template('quiz.html', question=question, feedback=feedback, correct_answer_text=correct_answer_text)

@app.route('/result')
def result():
    # Retrieve the final score and show the results
    score = session.get('score', 0)
    session.clear()
    return render_template('result.html', score=score, total=len(tech_trivia_quiz.questions))

if __name__ == '__main__':
    app.run(debug=True)
