import streamlit as st 
import tempfile
from qa_assistant import *
import axios
from openai import OpenAI
import time
import os
import requests
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()

"""
def get_vectorStorelist():
    files = list(client.beta.vector_stores.files.list(vector_store_id=any))  
    return files

def get_filelist():
    files = list(client.beta.vector_stores.files.list(vector_store_id=any))  
    return files

def get_messages(thread_id):
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    print(messages)

"""
st.title("Handling URL")

url =  "https://api.openai.com/v1/files"   # return list of files

#api_key = "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"
res = requests.get(url, headers = {
              "Authorization": "Bearer " + api_key})

print(res[0])

#all_files = list(client.beta.vector_stores.files.list(vector_store_id= any))

#print(all_files)