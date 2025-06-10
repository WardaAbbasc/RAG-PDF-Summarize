import streamlit as st
from env.document_loader import load_document
from env.chunker import semantic_chunk
from env.vectorstore import VectorStore
import os
from summarizer.generate_summary import summarize_with_mistral

st.title("📄 RAG Document Summarizer (Mistral + Ollama)")
os.makedirs("temp", exist_ok=True)

uploaded_file = st.file_uploader(
    "Upload your document (PDF):", 
    type=["pdf", "txt", "md"]
)

if uploaded_file:
    # Save the uploaded file to temp folder
    file_path = f"temp/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Load and chunk document text
    text = load_document(file_path)
    chunks = semantic_chunk(text)

    # Initialize vector store and add chunks
    vs = VectorStore()
    vs.add_texts(chunks)

    # Search top 5 relevant chunks for summarization
    retrieved_docs = vs.search("Summarize this document", top_k=5)

    st.subheader("🔍 Retrieved Context")
    for i, doc in enumerate(retrieved_docs):
        # Adjust depending on your returned object structure
        content = getattr(doc, 'page_content', str(doc))
        st.markdown(f"**Chunk {i+1}:**\n{content}")

    # Combine all retrieved chunk texts into one string
    combined_text = "\n".join(getattr(doc, 'page_content', str(doc)) for doc in retrieved_docs)

    with st.spinner("Generating summary using Mistral..."):
        summary = summarize_with_mistral(combined_text)

    st.subheader("📝 Generated Summary")
    st.markdown(summary)
