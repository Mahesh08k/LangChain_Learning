from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Mahesh_Kulkarni.pdf")

docs = loader.load()

print(docs)

print(len(docs))