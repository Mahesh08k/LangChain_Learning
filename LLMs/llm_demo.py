from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)

result = llm.invoke("Tell me a joke about programming.")

print(result)