from fastapi import APIRouter
from app.models.schemas import CompareRequest
from app.services.rule_engine import evaluate_rules

router = APIRouter()

@router.post("/compare-prompts")
async def compare_prompts(data: CompareRequest):

    old_score = evaluate_rules(data.old_prompt)["rule_score"]
    new_score = evaluate_rules(data.new_prompt)["rule_score"]

    improvement = new_score - old_score

    return {
        "old_score": old_score,
        "new_score": new_score,
        "improvement": improvement
    }