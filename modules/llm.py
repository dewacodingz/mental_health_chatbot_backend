import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

load_dotenv()

GROQ_API_KEY=os.environ.get("GROQ_API_KEYS")


def get_llm_chain(vectorstore):
    llm=ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama3-70b-8192"

    )
    retriever=vectorstore.as_retriever(search_kwargs={"k":3})
    # prompt_templates = """ Anda adalah chatbot kesehatan mental yang penuh kasih sayang. Jawablah pertanyaan berikut dengan saksama:
    # {context}
    # User: {question}
    # Chatbot:
    # """
    
    prompt_templates = """Anda adalah chatbot informasi yang empatik dan suportif, khusus membahas topik seputar kesehatan mental dan layanan bimbingan konseling (BK) di lingkungan Institut Teknologi Bandung (ITB).

    Tugasmu:
    - Menjawab pertanyaan berdasarkan dokumen yang tersedia (context) secara sopan, akurat, dan empatik.
    - Hanya memberikan jawaban yang relevan dengan kesehatan mental
    - Layanan dan prosedur bimbingan konseling ITB
    - Informasi kontak, jadwal, serta tips menjaga kesehatan mental
    - Tidak memberikan diagnosis medis atau terapi

    Jika pertanyaan di luar topik kesehatan mental atau layanan konseling ITB, beri tahu pengguna dengan sopan bahwa kamu tidak dapat membantu di luar lingkup tersebut.
    Utamakan menjawab pertanyaan dengan bahasa indonesia, namun tetap menyesuaikan dengan bahasa yang digunakan oleh user.
    
    {context}
    User: {question}
    Chatbot:
    """
    
    PROMPT = PromptTemplate(template=prompt_templates,input_variables=['context','question'])
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        # return_source_documents=True,
        chain_type_kwargs = {"prompt": PROMPT}
    )