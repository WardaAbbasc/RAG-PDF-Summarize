# 📄 RAG-based PDF Document Summarizer

This project is a **Retrieval-Augmented Generation (RAG)** pipeline that summarizes PDF documents using **semantic search** and a **local LLM**. It combines **FAISS** for embedding storage, **Mistral** as the summarizer via **Ollama**, and a simple **Streamlit UI** for interaction.

---

## 🧠 How It Works

1. **PDF Upload**: User uploads a PDF via the Streamlit interface.
2. **Document Parsing**: Extracted using **PyMuPDF (fitz)**.
3. **Chunking & Preprocessing**: Cleaned and chunked using **NLTK**.
4. **Embedding Generation**: Using **sentence-transformers**.
5. **Storage**: Embeddings are stored in **FAISS (CPU)**.
6. **Retrieval**: FAISS returns the most relevant chunks.
7. **Summarization**: Relevant context is passed to **Mistral LLM** via **Ollama**.
8. **Display**: Streamlit presents both the retrieved text and the final summary.

---

## 🧰 Tech Stack

| Component         | Tool/Library         |
|------------------|----------------------|
| PDF Parsing      | `PyMuPDF (fitz)`     |
| Text Processing  | `NLTK`, `NumPy`       |
| Embedding Model  | `sentence-transformers` |
| Vector DB        | `FAISS (CPU)`         |
| LLM              | `Mistral` via `Ollama` |
| UI               | `Streamlit`, `Markdown` |
| Others           | `pandas`, `os`, `uuid` |

---

