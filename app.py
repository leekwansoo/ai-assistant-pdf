import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import tempfile
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from document_handler import DocumentHandler, display_document
from qa_assistant import *
from dotenv import load_dotenv

load_dotenv()

def run(thread_id): 
    #print(prompt, thread_id, assistant_id, file_id)
    messages, run_id = run_assistant(prompt, thread_id, assistant_id, file_id)
    if messages:
        last_message_for_run = None
        for message in messages:
            st.write(message.content[0].text.value + "\n")
            if message.role == "assistant" and message.run_id == run_id:
                last_message_for_run = message
                break

        #if last_message_for_run:
        #    st.write(last_message_for_run.content[0].text.value + "\n")

        continue_asking = ask_question("Do you want to ask another question? (yes/no) ")
        keep_asking = continue_asking.lower() == "yes"
        #return messages
        st.write("Thank you for using the Q/A Assistant. Have a great day!")
    

st.title("AI-도우미")

with st.sidebar:
    option = st.selectbox("select Option", options = ["전자레인지메뉴얼", "100년후독서"])
    if option == "전자레인지메뉴얼":
        st.subheader("전자레인지메뉴얼")
        assistant_id = ""
        file_id = ""
        instruction = "당신은 충실한 서비스 챗봇입니다. Upload 된 전자 레인지 메뉴얼을 참조하여 소비자 질문에 충실하게 메뉴얼 내에서 응답해 주세요"
        prompt = ""

    if option == "100년후독서":
        st.subheader("100년후독서")
        assistant_id = ""
        file_id = ""
        instruction = "당신은 훌륭한 독서가이며 미래 정치 경제학자입니다. 100년 후 Document의 내용으로 부터 chatbot 으로 주어지는 질문에 상세히 대답해 주세요"
        prompt= ""
    #import tempfile

    uploaded_file = st.file_uploader("File upload", type="pdf")
    if uploaded_file:
        temp_dir = tempfile.mkdtemp()
        pdf_path = os.path.join(temp_dir, uploaded_file.name)
        with open(pdf_path, "wb") as f:
                f.write(uploaded_file.getvalue())
        print(pdf_path) 
        
        file_id = upload_file(pdf_path)
        file_id = file_id.id
        st.sidebar.write("file_id: ", file_id)

    file_id = st.text_input("enter the file_id", file_id) 
    assistant_id = st.text_input("enter the assitant_id", assistant_id) 


instruction = st.text_input("Instruction", instruction) 
if instruction:
    if not assistant_id:
        assistant_id = create_assistant(instruction)
        st.sidebar.write("assist_id: ", assistant_id)
        
prompt = st.text_input("Prompt")
if prompt:
    thread_id = create_thread()
    prompt = ask_question(prompt)
    st.button("Process", on_click=run(thread_id))
 

   
        
    
            
