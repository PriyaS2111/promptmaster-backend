from fastapi import FastAPI
from app.routes import evaluate, compare, progress, prompt

app = FastAPI(title="PromptMaster AI")

app.include_router(evaluate.router)
app.include_router(compare.router)
app.include_router(progress.router)
app.include_router(prompt.router)

@app.get("/")
def home():
    return {"message": "PromptMaster AI Backend Running 🚀"}