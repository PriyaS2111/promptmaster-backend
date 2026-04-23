from fastapi import APIRouter
from app.models.schemas import PromptRequest
from app.services.rule_engine import evaluate_rules
from app.services.llm_engine import evaluate_with_llm
from app.services.scoring import combine_scores

router = APIRouter()

@router.post("/evaluate-prompt")
async def evaluate_prompt(data: PromptRequest):

    rule_result = evaluate_rules(data.prompt)
    llm_result = evaluate_with_llm(data.prompt)

    final = combine_scores(rule_result, llm_result)

    return {
        "status": "success",
        "data": final
    }
