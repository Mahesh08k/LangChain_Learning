from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Mahesh_Kulkarni.pdf")

docs = loader.load()

# print(docs[0].page_content)

# text = """In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available.
# """

text = docs[0].page_content

splitter = CharacterTextSplitter(
    chunk_size=50, chunk_overlap=0, separator=""
)

texts = splitter.split_text(text)
print(texts)