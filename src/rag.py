from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

from src.retriever import retriever
from src.prompt import load_prompt
from src.llm import load_llm


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def create_rag_chain():

    retriever_obj = retriever()

    prompt = load_prompt()

    llm = load_llm()

    ragchain = (
        {
            "context": retriever_obj | RunnableLambda(format_docs),
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return ragchain