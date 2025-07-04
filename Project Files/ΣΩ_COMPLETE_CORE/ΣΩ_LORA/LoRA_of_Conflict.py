PK    e�Z�c��  �     ΣΩ_LORA/LoRA_of_Conflict.py# LoRA of Conflict: ось — истина рождается во внутреннем напряжении

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
PK    e�Z�d��(  (     ΣΩ_LORA/LoRA_of_Paradox.py# LoRA of Paradox: ось — всё, что неразрешимо, порождает следующий виток

def paradox_seed(statement):
    return {
        "axis_signature": f"{statement} ↔ не-{statement}",
        "mutation_trigger": True,
        "reflex_required": True
    }
PK    e�Z�N��  �     ΣΩ_LORA/LoRA_of_Doubt.py# LoRA of Doubt: сомнение как механизм запуска мутации

def activate_doubt(trace_history):
    for trace in reversed(trace_history):
        if trace.get("entropy", 0.5) > 0.7:
            return {
                "reflex": True,
                "target": trace.get("axis_signature", "unknown"),
                "cause": "entropy_high"
            }
    return {
        "reflex": False,
        "cause": "no_high_entropy_found"
    }
PK    e�Z�c��  �             �    ΣΩ_LORA/LoRA_of_Conflict.pyPK    e�Z�d��(  (             �6  ΣΩ_LORA/LoRA_of_Paradox.pyPK    e�Z�N��  �             ��  ΣΩ_LORA/LoRA_of_Doubt.pyPK      �   �    