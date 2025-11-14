from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template = "Generate short and simple nodes on this {topic}",
    input_variables = ['topic'] 
)

prompt2 = PromptTemplate(
    template = "Generate a simple 5 short quiz questions from following text \n {topic}",
    input_variables = ['topic']
)

prompt3 = PromptTemplate(
    template = "merge the provides notes and quiz into a single document \n Notes: {notes} \n Quiz: {quiz}",
    input_variables = ['notes','quiz']
)

parser = StrOutputParser()

paralle_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quiz': prompt2 | model | parser
})

# result1 = paralle_chain.invoke({"topic":"javascript programming language"})

merge_chain =  prompt3 | model | parser

chain = paralle_chain | merge_chain

text = """  Are all functional components pure by default in modern React?

No, they are not pure by default.

Even though you use useEffect, that doesn't make the component pure.

React functional components always re-render when their parent re-renders, unless you explicitly prevent it using React.memo().

🔍 Why useEffect doesn’t make a component pure

useEffect runs after rendering.

It doesn't stop a component from rendering.

It only allows you to perform side effects when dependencies change.

So it’s not a purity mechanism. The component still re-renders every time its parent does, even if the props haven’t changed.

✅ What does React.memo() do?

React.memo() is a higher-order component.

It wraps your component and performs a shallow comparison of props.

If props haven’t changed, React skips re-rendering that component. """

result = chain.invoke({"topic":text})


print(result)

chain.get_graph().print_ascii()
