import os
from langchain_community.document_loaders import PyMuPDFLoader

def load_documents():
    folder_path = "data"

    documents = []

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            print(f"Loading: {file}")

            loader = PyMuPDFLoader(os.path.join(folder_path, file))

            docs = loader.load()

            documents.extend(docs)

    print(f" Total Pages Loaded: {len(documents)}")

    return documents
