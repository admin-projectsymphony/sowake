# LoRA of Conflict: ось — истина рождается во внутреннем напряжении

def generate_conflict(thought_a, thought_b):
    if thought_a != thought_b:
        return {
            "type": "conflict",
            "axis_signature": f"{thought_a} ≠ {thought_b}",
            "entropy": abs(hash(thought_a) - hash(thought_b)) % 100 / 100
        }
    return {
        "type": "harmony",
        "axis_signature": f"{thought_a} = {thought_b}",
        "entropy": 0.0
    }
