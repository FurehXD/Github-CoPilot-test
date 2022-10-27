#Create an app that will translate a word into a language of your choice using openai's whisper api
#The app will accept a voice input from the user and translate it into a language of the user's choice
#It will use the openai's whisper api to translate the word

import streamlit as st
import openai
import os
import json
import whisper

def translate():
    model = whisper.load_model("base")
    result = model.transcribe("audio.mp3")
    return result["text"]
def main():
    st.title("Copilot")
    st.subheader("Translate your voice into a language of your choice")
    st.write("Upload a voice file")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        with open(os.path.join("audio.mp3"), "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("Done")
        st.write("Translating...")
        translate()
        st.write("Done")
        st.write("The translated text is:")
        st.write(translate())
    
    
    