import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)  # for MiniLM embeddings
        self.texts = []

    def add_texts(self, texts):
        embeddings = self.model.encode(texts)
        self.index.add(np.array(embeddings).astype('float32'))
        self.texts.extend(texts)

    def search(self, query, top_k=5):
        embedding = self.model.encode([query])
        D, I = self.index.search(np.array(embedding).astype('float32'), top_k)
        return [self.texts[i] for i in I[0]]
