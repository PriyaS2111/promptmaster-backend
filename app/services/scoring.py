import json
import re

def extract_json(text):
    try:
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except:
        pass

    return None


def fallback_parse(text):
    try:
        score_match = re.search(r"Score[:\s]*([0-9]+)", text)
        clarity_match = re.search(r"Clarity[:\s]*(.*)", text)
        improvement_match = re.search(r"Improvement.*?:\s*(.*)", text)

        return {
            "score": int(score_match.group(1)) if score_match else 5,
            "clarity": clarity_match.group(1).strip() if clarity_match else "Not clear",
            "improvement": improvement_match.group(1).strip() if improvement_match else "Improve prompt"
        }
    except:
        return None


def combine_scores(rule_result, llm_result):

    llm_data = extract_json(llm_result)

    if not llm_data:
        llm_data = fallback_parse(llm_result)

    if not llm_data:
        llm_data = {
            "score": 5,
            "clarity": "Parsing error",
            "improvement": "Try again"
        }

    final_score = (
        rule_result["rule_score"] +
        llm_data["score"]
    ) / 2

    return {
        "final_score": round(final_score, 2),
        "llm": llm_data,
        "rule": rule_result
    }