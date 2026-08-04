from langchain_community.vectorstores import Chroma

from src.splitter import split_documents
from src.embeddings import load_embeddings


def create_vector_db():

    chunks = split_documents()

    embeddings = load_embeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store