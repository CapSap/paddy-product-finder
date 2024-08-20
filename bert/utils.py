# utils.py
import torch
import numpy as np

def encode_text(tokenizer, model, text):
    # Tokenize text
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    # Get BERT embeddings
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the embeddings from the last hidden layer
    last_hidden_state = outputs.last_hidden_state
    # Mean pooling to get a single vector representation
    attention_mask = inputs['attention_mask']
    pooled_output = torch.sum(last_hidden_state * attention_mask.unsqueeze(-1), 1) / torch.sum(attention_mask, 1, keepdim=True)
    return pooled_output.squeeze().numpy()
