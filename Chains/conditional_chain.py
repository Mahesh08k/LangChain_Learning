from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel , RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative', 'neutral'] = Field(..., description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following feedback text into positive, negative, or neutral: {feedback} \n {format_instructions}",
    input_variables = ['feedback'],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({"feedback":"This is teriable smartphone."})

# print(result)

prompt2 = PromptTemplate(
    template = "write an appropriate response to the following positive feedback based :\n {feedback}",
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = "write an appropriate response to the following negative feedback: \n {feedback} ",
    input_variables = ['feedback']
)

prompt4 = PromptTemplate(
    template = "write an appropriate response to the following neutral feedback: \n {feedback} ",
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    (lambda x:x.sentiment == 'neutral', prompt4 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment")  # default case
)

chain = classifier_chain | branch_chain | parser

final_result = chain.invoke({"feedback":"I liked this toy car , it is very good"})

print(final_result)

chain.get_graph().print_ascii()



