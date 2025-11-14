from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/LangChain/huggingface_cache'  # Set the cache directory for Hugging Face models

llm = HuggingFacePipeline.from_model_id(
     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
     task="text-generation",
     pipeline_kwargs={"max_length": 2048, "temperature": 0.01},
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is captial of USA")

print(result.content)