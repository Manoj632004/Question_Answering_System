import torch
from transformers import BertForQuestionAnswering, BertTokenizer

def model(context, question):
    model = BertForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
    tokenizer = BertTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
    
    # Encode Input
    encoding = tokenizer.encode_plus(text=question, text_pair=context, return_tensors="pt")
    
    inputs = encoding['input_ids']
    sentence_embedding = encoding['token_type_ids']
    
    start_scores, end_scores = model(input_ids=inputs, token_type_ids=sentence_embedding)
    
    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores)
    
    tokens = tokenizer.convert_ids_to_tokens(inputs[0])
    answer = ' '.join(tokens[start_index:end_index+1])
    
    corrected_answer = ''
    for word in answer.split():
        if word.startswith('##'):
            corrected_answer += word[2:]
        else:
            corrected_answer += ' ' + word
    
    return corrected_answer.strip()

