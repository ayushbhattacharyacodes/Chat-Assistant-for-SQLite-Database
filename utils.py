from langchain_ollama import ChatOllama
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.prompts import PromptTemplate
from langchain.memory.buffer import ConversationBufferMemory
from langchain_experimental.sql import SQLDatabaseChain
from langchain_core.output_parsers.string import StrOutputParser


from dotenv import load_dotenv
import os

def read_properties_file():
    load_dotenv()
    db_path = os.getenv("db")
    url = os.getenv("BASE_URL")
    return db_path,url

def get_properties():
    try:
        db_path,url = read_properties_file()
        return db_path,url
    except FileNotFoundError as e:
        raise e
    
def get_llm(url):
    llm = ChatOllama(model="llama3.2-vision",
                     base_url=url,
                     temperature=0.4
                     )

    return llm    

def db_connection(db):
    db = SQLDatabase.from_uri(f'sqlite:///{db}')
    return db

def create_conversational_chain():
    try:
        db,url = get_properties()

        llm = get_llm(url)

        db = db_connection(db) 

        sql_prompt_template = """
        Only use the following tables:
        {table_info}

        Question: {input}

        Given an input question,first create a syntactically correct
        {dialect} query to run.

        Relevant pieces of previous converation:
        {history}

        (You do not need to use these pieces of information if not relevant)

        Don't include ```,```sql and \n in the output.
        """ 

        prompt = PromptTemplate(
            input_variables=["input","table_info","dialect","history"],
            template = sql_prompt_template
        )

        memory = ConversationBufferMemory(memory_key="history")

        db_chain = SQLDatabaseChain.from_llm(
                    llm, 
                    db, 
                    memory=memory,
                    prompt=prompt,
                    return_direct=True, 
                    verbose=True
                )

        oputput_parser = StrOutputParser()
        chain = llm | oputput_parser

    except Exception as e:
        raise e
    return db_chain,chain 