from dotenv import load_dotenv
load_dotenv()  # load all the environment variables from .env

import streamlit as st
import os
from PIL import Image

import google.generativeai as genai

genai.configure(api_key="AIzaSyB3M2UJgUIcsY2-tSCeHxSkDQI-CCpW96I")
model = genai.GenerativeModel('gemini-pro-vision')  # Load Gemini pro vision model


def get_gemini_response(input, images, user_prompt):
    responses = []
    for idx, image in enumerate(images):
        response = model.generate_content([input, image[0], user_prompt.format(idx + 1)])
        responses.append(response.text)
    return responses


def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()  # Read the file into bytes
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts

    else:
        raise FileNotFoundError("No file uploaded")
    
st.header("AI Invoices Tracker")

import re


    
    
vv=0
col1,col2=st.columns([5,5])
with col2:

        # initialize our streamlit app

    input_prompt = """
    You are an expert in understanding invoices. We will upload {} images as invoices,
    and you will have to answer any questions based on the uploaded invoice images.
    """

    input = st.text_input("AI Input Prompt: ", key="input")
    
    submit = st.button("Perform Operations on Invoices")
    uploaded_files = st.file_uploader("Choose images of the invoice...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)


    st.sidebar.image(uploaded_files)

    if uploaded_files is not None and len(uploaded_files) > 0:
        st.info("Selected {} images for processing.".format(len(uploaded_files)))

        input_prompt = input_prompt.format(len(uploaded_files))

        
        if submit:  # if submit button is clicked
            responses = get_gemini_response(input_prompt, [input_image_details(file) for file in uploaded_files], input)

            st.subheader("The Responses are")
            
            for idx, response in enumerate(responses):
                st.write("-"*50)
                st.write(response)
            
                
                    




with col1:

    dtt=st.button("Dates",key="aff")
    if dtt:
        if uploaded_files is not None and len(uploaded_files) > 0:
            st.info("Selected {} images for processing.".format(len(uploaded_files)))

            input_prompt = "you are expert in invoices and dates ,answer the given question"

            
            
            responses = get_gemini_response(input_prompt, [input_image_details(file) for file in uploaded_files], "give me the invoices date")

            st.subheader("The Responses are")
                
            for idx, response in enumerate(responses):                #st.write(f"Response for Invoice:")
                st.write("-"*50)
                st.write(response)



    inv=st.button("Invoice No",key="af")
    if inv:
        if uploaded_files is not None and len(uploaded_files) > 0:
            st.info("Selected {} images for processing.".format(len(uploaded_files)))

            input_prompt = "you are expert in invoices and dates ,answer the given question"

            
            
            responses = get_gemini_response(input_prompt, [input_image_details(file) for file in uploaded_files], "give me the Invoices no.")

            st.subheader("The Responses are")
                
            for idx, response in enumerate(responses):                #st.write(f"Response for Invoice:")
                st.write("-"*50)
                st.write(response)
