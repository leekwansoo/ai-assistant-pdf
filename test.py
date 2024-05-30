import streamlit as st 
import os
import logging
from pdf2image import convert_from_path
import matplotlib.pyplot as plt
import numpy as np
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

files = ["files/100years_later.pdf", "files/Declaration_of_independence.pdf", "files/The_Adventures_of_Tom_Sawyer.pdf", "files/전자레인지메뉴얼.pdf"]
images = ["data/output_1.png","data/output_2.png","data/output_3.png","data/output_4.png"]
def display_image(img):
        try:
            #pdf_path = os.path.join(output_dir, 'sample.pdf')
            st.size=(30, 30)
            st.image(img)
        except Exception as e:
            logger.error(f"Error displaying document: {e}")

selected = st.selectbox("Selct your choice", ("files/100years_later.pdf", "files/Declaration_of_independence.pdf", "files/The_Adventures_of_Tom_Sawyer.pdf", "files/전자레인지메뉴얼.pdf"))
st.write("selected file is:", selected)         
st.title("Plotting the Fig in the web page")
for img in images:
    display_image(img)
    
