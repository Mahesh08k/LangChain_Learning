from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

template1 = PromptTemplate(
    template = "give me detailed info on {topic}",
    input_variables = ["topic"]
)

template2 = PromptTemplate(
    template = "write 5 line summary on following text. /n {text}",
    input_variables = ["text"]
)

chain = template1 | model | parser | template2 |model | parser

result = chain.invoke({'topic':'black hole'})

print(result)