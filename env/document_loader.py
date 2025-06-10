import fitz  # PyMuPDF
import markdown

def load_document(file_path):
    if file_path.endswith(".pdf"):
        doc = fitz.open(file_path)
        return "\n".join([page.get_text() for page in doc])
    elif file_path.endswith(".txt"):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif file_path.endswith(".md"):
        with open(file_path, 'r', encoding='utf-8') as f:
            return markdown.markdown(f.read())
    else:
        raise ValueError("Unsupported file format")