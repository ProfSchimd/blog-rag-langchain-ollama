# IMPORTS
from langchain import hub
from langchain.document_loaders.text import TextLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# INDEXING 

# Load document
file_path = "./cat-facts.txt"
loader = TextLoader(file_path)
docs = loader.load()

# Split doucment into smaller chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=0,
    length_function=len,
)
all_splits = text_splitter.split_documents(docs)

# Construct embeddings for the documents and store in memory
embeddings = OllamaEmbeddings(model="llama3.2:1b")  
vector_store = InMemoryVectorStore(embeddings)
vector_store.add_documents(documents=all_splits)

# RETRIEVAL

# Query the storer for documents similar to the query
query = "Were cats ever sent to space?"
retrieved_docs = vector_store.similarity_search(query)
docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

# GENERATION
# Create a prompt
prompt = hub.pull("rlm/rag-prompt")
prompt = prompt.invoke({"question": query, "context": docs_content})

# Create the chat and send the prompt
llm = ChatOllama(model="llama3.2:1b")
answer = llm.invoke(prompt)

print(answer.content)