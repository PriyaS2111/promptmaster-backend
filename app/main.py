from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # ✅ ADD THIS
from app.routes import evaluate, compare, progress, prompt
"""
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

============================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔥 IMPORTANT FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all
    allow_credentials=False,
    allow_methods=["*"],   # allow OPTIONS
    allow_headers=["*"],
)

# 👇 KEEP THIS BELOW
from app.routes import evaluate, compare, progress, prompt

app.include_router(evaluate.router)
app.include_router(compare.router)
app.include_router(progress.router)
app.include_router(prompt.router)

@app.get("/")
def home():
    return {"message": "PromptMaster AI Backend Running 🚀"}

"""

#for the satic file of html we will use below code as it is in the same file
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔥 NEW IMPORTS
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# 🔥 CORS (can keep or remove later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 IMPORT ROUTES
from app.routes import evaluate, compare, progress, prompt

app.include_router(evaluate.router)
app.include_router(compare.router)
app.include_router(progress.router)
app.include_router(prompt.router)

# 🔥 NEW: Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 🔥 NEW: Serve your frontend
@app.get("/")
def serve_frontend():
    return FileResponse("app/static/index.html")