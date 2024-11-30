from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import os 
from dotenv import load_dotenv
load_dotenv()


# Without Persistance storage
def simple():
    os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
    docs = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(docs)
    engine = index.as_query_engine()
    answer = engine.query("Explain me what is this?")
    print("answer", answer)


# With Persistance storage
def createEmbedding():
    os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
    docs = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(docs)
    index.storage_context.persist()

def loadEmbedding():
    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context)
    return index.as_query_engine()

def fireQuery(index, query):
    return index.query(query)


if __name__ =="__main__":
    '''
    if you enamble simple() 
    commnet rest of the methods
    if  simple() is commented the first create emabedding using  "createEmbedding()" then
    "loadEmbedding()" and "fireQuery(index,query)
    '''
    # simple()
    # createEmbedding()
    index = loadEmbedding()
    answer = fireQuery(index, "Who is host?")
    print(answer)
