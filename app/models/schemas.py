from pydantic import BaseModel

class PromptRequest(BaseModel):
    user_id: str
    prompt: str

class CompareRequest(BaseModel):
    old_prompt: str
    new_prompt: str