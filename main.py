from fastapi import FastAPI, Query
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import openai
import uvicorn

app = FastAPI()

# Initialize FAISS search (Assuming docs are indexed)
embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embeddings)

@app.get("/query")
def answer_question(query: str = Query(..., min_length=5, max_length=500)):
    """
    Handles 'how-to' questions about Segment, mParticle, Lytics, Zeotap.
    Returns relevant documentation excerpts.
    """
    try:
        # Search FAISS for relevant documentation
        results = db.similarity_search(query, k=3)

        if not results:
            return {"response": "Sorry, I couldn't find relevant documentation for your query."}

        return {"response": results[0].page_content}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
