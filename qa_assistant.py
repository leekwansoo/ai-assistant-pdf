from openai import OpenAI
import time
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()
 
def upload_file(pdf_path):
    print(pdf_path)
    file_id = client.files.create(
        file = open(pdf_path, "rb"),
        purpose='assistants'
    )
    return file_id

def get_vectorStorelist():
    files = list(client.beta.vector_stores.files.list(vector_store_id=any))  
    return files

def get_filelist():
    files = list(client.beta.vector_stores.files.list(file_id=any))  
    return files
    
def create_assistant(instruction):
    print("request for assistant_id")
    assistant = client.beta.assistants.create(
        name="PDF Assistant",
        instructions=instruction,
        model="gpt-3.5-turbo",
        description="A chatbot that answers questions based on the uploaded file.",    
    )
    assistant_id = assistant.id
    print(assistant_id)
    return assistant_id

def create_thread():
    thread = client.beta.threads.create()
    thread_id = thread.id
    print(thread_id)
    return thread_id

def ask_question(prompt):
    return prompt

def run_assistant(prompt, thread_id, assistant_id, file_id):
    print(prompt, thread_id, assistant_id, file_id)
    client.beta.threads.messages.create(
        thread_id= thread_id,
        role="user",
        content=prompt,
        attachments = [ { "file_id": file_id, "tools": [{"type": "file_search"}] } ],
    )
    

    run = client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)

    run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
    while run_status.status != "completed":
        time.sleep(2)
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)

    messages = client.beta.threads.messages.list(thread_id=thread_id)
    print(run.id)
    run_id = run.id
    return (messages, run_id)

    
"""      
pdf_path = "data/sample.pdf"     
if pdf_path:
    qa_assistant = QAAssistant(pdf_path)
    qa_assistant.run_assistant()
"""