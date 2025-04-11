from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.llm import LLMChain

def get_summary_chain(llm):
    return LLMChain(
        llm=llm,
        prompt=ChatPromptTemplate.from_template("""
            Summarize this document concisely:
            {text}
            Summary:""")
    )

def get_qa_chain(llm):
    return create_stuff_documents_chain(
        llm,
        ChatPromptTemplate.from_template("""
            Answer the question based only on the provided context:
            <context>{context}</context>
            Question: {input}
            Answer:""")
    )