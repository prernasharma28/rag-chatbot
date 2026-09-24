from fastapi import FastAPI

app = FastAPI(title="RAG Chatbot")


@app.get("/")
def home():
    return {"message": "RAG Chatbot is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}