#!/usr/bin/env python

"""
This app is a Web app using streamlit
"""
import streamlit as st
from oalib.solution import submit_question

st.title("Question Answer Webapp")
text = st.text_input("Enter your question here") 
if st.button("Submit"):
    response = submit_question(text)
    st.write(response)
