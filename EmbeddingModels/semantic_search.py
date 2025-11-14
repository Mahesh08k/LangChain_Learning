from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India"

document = [
    "Rohit sharma is the captain of Indian cricket team.",
    "sachin Tendulkar is the God of cricket.",
    "Jasprit Bumrah is a best fast bowler in Indian cricket team known for unorthodox action and yorkers.",
    "Buvneshwar Kumar is a good swing bowler.",
]

query = "Jasprit Bumrah famaous for?"

doc_embedding = embeddings.embed_documents(document)
query_embedding = embeddings.embed_query(query)

similarity = cosine_similarity([query_embedding], doc_embedding)

index, score = (sorted(list(enumerate(np.array(similarity[0]))), key=lambda x: x[1])[-1])

print(query)
print(document[index])
print("similarity score: " + str(score))
