from src.vectordb import create_vector_db
vector_store=create_vector_db()
def retriever():
    retriever=vector_store.as_retriever(
    search_kwargs={"k":5}
)
    return retriever