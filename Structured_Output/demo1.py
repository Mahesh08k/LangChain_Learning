from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

#schema

class review(TypedDict):
    summary: str
    sentiment: str
    positive: str
    negative: str

structured_model = model.with_structured_output(review)

result = structured_model.invoke("""The hardware is grate but the software is bad , display is good but camera modules are are not that good as compared to price of the phone""")


print(result)
print(result['summary'])