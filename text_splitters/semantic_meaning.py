from langchain_experimental.text_splitters import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text_splitter = SemanticChunker(
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount = 1
)


text = """
        Farming has been the backbone of human civilization for thousands of years, providing sustenance and economic stability to communities worldwide. Modern agricultural practices have evolved to include precision farming techniques, utilizing advanced technology and data analytics. The integration of sustainable methods and organic farming has become increasingly important in addressing environmental concerns and food security challenges.

The Indian Premier League (IPL) has revolutionized cricket since its inception in 2008, becoming one of the most-watched sporting events globally. Teams compete fiercely for the coveted trophy, with matches often featuring nail-biting finishes and spectacular performances. The tournament has created numerous opportunities for young cricketers to showcase their talents alongside international stars. The economic impact of IPL has been tremendous, generating billions in revenue through broadcasting rights, sponsorships, and ticket sales. Meanwhile, the evolution of air navigation systems has dramatically enhanced aviation safety and efficiency. Modern aircraft rely on sophisticated satellite-based navigation systems and automated flight management computers. The integration of artificial intelligence and machine learning has improved weather prediction and route optimization. Ground-based radar systems work in conjunction with onboard equipment to maintain safe separation between aircraft. The continuous advancement of these technologies has made air travel one of the safest forms of transportation.


"""

chunks = text_splitter.create_document([text])
print(len(chunks))
print(chunks)