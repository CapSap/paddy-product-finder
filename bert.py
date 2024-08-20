from transformers import BertTokenizer, BertModel
import torch
import numpy as np

# Load pre-trained model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


def encode_text(text):
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


from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(text1, text2):
    # Encode both texts
    embedding1 = encode_text(text1)
    embedding2 = encode_text(text2)
    # Compute cosine similarity
    similarity = cosine_similarity([embedding1], [embedding2])
    return similarity[0][0]

# Example texts
text1 = "ICE 560 ELEMENTAL LS ZIP JKT W"
text2 = "Womens Merino 560 RealFleece Elemental II LS Zip"

similarity_score = compute_similarity(text1, text2)
print(f"Similarity score: {similarity_score}")