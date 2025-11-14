from langchain_community.document_loaders import TextLoader
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

prompt = PromptTemplate(
    template = "Generate 5 lines of summary on {topic}",
    input_variables = ['topic'] 
)

loader = TextLoader("example.txt" , encoding='utf8')

docs = loader.load()

#print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({"topic":docs[0].page_content})

print(result)