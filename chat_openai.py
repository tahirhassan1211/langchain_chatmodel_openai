from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
chatmodel=ChatOpenAI(model_name='gpt-5-nano', temperature=0.7)
result=chatmodel.invoke("Current president of USA?")
print(result.content)



