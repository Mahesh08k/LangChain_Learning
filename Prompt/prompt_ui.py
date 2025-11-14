from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
import streamlit as st
import os

os.environ['HF_HOME'] = 'D:/LangChain/huggingface_cache' 
# may be try this model microsoft/Phi-3-mini-4k-instruct

llm = HuggingFacePipeline.from_model_id(
     model_id="microsoft/Phi-3-mini-4k-instruct",
     task="text-generation",
)

#model = ChatHuggingFace(llm=llm)

st.header('Research Tool')

user_input = st.text_input("Enter your research query")

if st.button('Summarize'):
    #result = model.invoke(user_input)
    st.write("here is the summary of your research query:")