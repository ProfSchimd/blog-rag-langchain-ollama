# RAG with LangChain and Ollama
Companion repository for the blog post "Retrieval-Augmented Generation (RAG) with LangChain and local Ollama"

See the blog post [Retrieval-Augmented Generation (RAG) with LangChain and local Ollama](https://skimmy.github.com/blog/rag-langchain/) for details on the repository.

 > [!WARNING]
 > To run properly, the code in this repository requires Ollama with the model indicate in `main.py`.

## Setting up an environment

```shell
 python -m venv .venv
 source .venv/bin/activate
 # Windows users
 # .venv\Scripts\activate.bat 
 pip install langchain langchain-community langchainhub langchain-ollama
 curl --output cat-facts.txt "https://huggingface.co/ngxson/demo_simple_rag_py/raw/main/cat-facts.txt"
 ```

 ## Running the code

 ```shell
 python main.py
 ```

 > [!NOTE]
 > You may see several warnings appearing while running, the program should complete correctly anyway outputting an answer similar to

 ```
 Yes, the French cat Felicette, also known as "Astrocat," was sent to space in 1963. In contrast, cats are typically fed a diet consisting of around five mice per meal on average. The first recorded cat show took place in London in 1871.
 ```