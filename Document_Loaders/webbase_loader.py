from  langchain_community.document_loaders import WebBaseLoader
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
    template = "Answer the Question {Question} asked on this  {topic}",
    input_variables = ['Question','topic'] 
)


url = "https://www.flipkart.com/motorola-edge-60-pro-pantone-sparkling-grape-256-gb/p/itm72c35d843cd5f?pid=MOBH9C9JWM2Y5FZP&lid=LSTMOBH9C9JWM2Y5FZPZTYQVM&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=browse&fm=organic&iid=3bae9629-aa80-4f2d-853f-092d4a42fb6f.MOBH9C9JWM2Y5FZP.SEARCH&ppt=hp&ppn=homepage&ssid=r1d4zy01xc0000001760454870221"

loader = WebBaseLoader(url)

docs = loader.load()

# print("Number of documents:", len(docs))

# print(docs[0].page_content) 

chain = prompt | model | parser

result = chain.invoke({"Question":"What is the product we are talking about","topic":docs[0].page_content})

print(result)