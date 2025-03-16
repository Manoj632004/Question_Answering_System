from flask import Flask, render_template, request
from model import translate, model  #Import functions from model.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    content = request.form['content'] 
    translated_text = translate(content) 
    return render_template('home.html', content=content, translated_text=translated_text)

@app.route('/answer', methods=['POST'])
def answer():
    question = request.form['question']  
    answer_text = model(question)  
    return render_template('home.html', content=request.form['content'], translated_text=request.form['translated_text'], answer=answer_text)

if __name__ == '__main__':
    app.run(debug=True)
