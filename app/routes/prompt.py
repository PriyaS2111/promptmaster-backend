from fastapi import APIRouter
from app.db.supabase import supabase
from app.models.schemas import PromptRequest

router = APIRouter()

@router.post("/save-prompt")
async def save_prompt(data: PromptRequest):

    response = supabase.table("prompts").insert({
        "user_id": data.user_id,
        "prompt": data.prompt
    }).execute()

    return {"status": "saved", "data": response.data}