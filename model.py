# model.py
from transformers import pipeline
from googletrans import Translator

translator = Translator()
# Initialize the question-answering model
oracle = pipeline(model="deepset/roberta-base-squad2")

# Dummy translation function (replace this with your actual code)
def translate(tamil_text):
    translated = str(translator.translate(tamil_text,dest  = 'en').text)
    return translated

# Function to get an answer based on the question and context
def get_answer(question, context):
    return oracle(question=question, context=context)['answer']
