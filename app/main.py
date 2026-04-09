from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # ✅ ADD THIS
from app.routes import evaluate, compare, progress, prompt

app = FastAPI(title="PromptMaster AI")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    #allow_origins=["*"],   # allow all (for now)
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(evaluate.router)
app.include_router(compare.router)
app.include_router(progress.router)
app.include_router(prompt.router)

@app.get("/")
def home():
    return {"message": "PromptMaster AI Backend Running 🚀"}