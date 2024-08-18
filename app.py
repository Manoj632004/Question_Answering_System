from flask import Flask, render_template, request
from model import translate, get_answer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    context = None
    question = None
    answer = None
    language_token = None

    if request.method == 'POST':
        if 'contextInput' in request.form:
            # First submission - Context input
            context = request.form.get('contextInput')
            language_token = request.form.get('languageToken')
            if language_token == "1":
                context = translate(context)
        elif 'questionInput' in request.form:
            # Second submission - Question input
            context = request.form.get('context')
            language_token = request.form.get('language_token')
            question = request.form.get('questionInput')
            answer = get_answer(question, context)

    return render_template('home.html', context=context, question=question, answer=answer, language_token=language_token)

if __name__ == '__main__':
    app.run(debug=True)
