from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
import pandas as pd
from ecommercebot.data_converter import dataconverter

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLCATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

def ingestdata(status):
    vstore = AstraDBVectorStore(
        embedding=embedding,
        collection_name="ChatBotEComm",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLCATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE,
    )

    storage = status

    if storage == None:
        docs = dataconverter()
        inserted_id = vstore.add_documents(docs)

    else:
        return vstore
    
    return vstore, inserted_id

if __name__ == "__main__":
    vstore, inserted_id = ingestdata(None)
    print(f"\nInserted {len(inserted_id)} documents")
    results = vstore.similarity_search("can you tell me the low budget sound basshead?")
    for res in results:
        print(f"* {res.page_content} [{res.metadata}]")