import streamlit as st 
from document_handler import DocumentHandler
from qa_assistant import *
#import temp
import os

st.title("OPENAI Assistant with PDF Loader")

if "files" not in st.session_state:
    st.session_state.files = []
with st.sidebar:
    selected = st.selectbox("Selct your choice", ("files/100years_later.pdf", "files/Declaration_of_independence.pdf", "files/The_Adventures_of_Tom_Sawyer.pdf", "files/전자레인지메뉴얼.pdf"))
    st.write("selected file is:", selected)
    
    if st.button("Upload File"):
        file_id = upload_file(selected) # file_id in the OpenAI Vector #Vector Storage in AI Assistant
        file_id = file_id.id
        st.session_state.files.append(file_id)
        st.write("file_id:", file_id)
    
    if st.button("Get Stored file list"):
        files = get_filelist() 
        st.write("Files in vectore store", files)
        
    if st.button("Create Assistant"):
        file_id = "file-tlF8iQNV6GWi21XTExVPNvAr"
        st.write("file_id:", file_id)
        #assistant_id = create_assistant()
        #asisstant_id = assistant_id.id
        assistant_id = "asst_AHARJKfMOYS6PZNx7sQA1oB1"
        st.write("assistant_id:", assistant_id)
    

if st.button("Thread"):
    thread_id =create_thread()
    st.sidebar.write("thread_id:", thread_id)
    
    if thread_id:
        
        input_key = 0   
        input_key += 1
        user_question = st.text_input("What is your question?", key = input_key)
        if user_question:
            while True:
                prompt = ask_question(user_question)
                st.write("user_question:", prompt)
                [run_id, messages] = run_assistant(prompt, thread_id, assistant_id, file_id) 
                last_message_for_run = None
                for message in reversed(messages.data):
                    if message.role == "assistant" and message.run_id == run_id:
                        last_message_for_run = message
                        break

                if last_message_for_run:
                    st.write(f"{last_message_for_run.content[0].text.value} \n")
                    
                    st.stop()
            
                    
                
            