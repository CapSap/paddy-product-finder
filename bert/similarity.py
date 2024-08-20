# similarity.py
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(embedding1, embedding2):
    # Compute cosine similarity
    similarity = cosine_similarity([embedding1], [embedding2])
    return similarity[0][0]
