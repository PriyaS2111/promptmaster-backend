from fastapi import APIRouter
from app.db.supabase import supabase

router = APIRouter()

@router.get("/user-progress/{user_id}")
async def get_progress(user_id: str):

    response = supabase.table("progress").select("*").eq("user_id", user_id).execute()

    return {"data": response.data}