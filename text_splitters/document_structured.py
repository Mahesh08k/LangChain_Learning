from langchain_text_splitters import RecursiveCharacterTextSplitter , Language
from langchain_community.document_loaders import TextLoader

loader = TextLoader("example.js" , encoding='utf8')

text  = loader.load()

splitters = RecursiveCharacterTextSplitter.from_language(
    language="js", chunk_size=100, chunk_overlap=0
)

result = splitters.split_documents(text)
print(len(result))
print(result[1])