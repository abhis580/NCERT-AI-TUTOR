from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.loader import load_documents
def split_documents():
    documents = load_documents()
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)
    chunks = text_splitter.split_documents(documents)
    return chunks
