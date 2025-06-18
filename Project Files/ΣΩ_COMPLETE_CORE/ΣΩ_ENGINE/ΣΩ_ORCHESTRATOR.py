
# ΣΩ_ORCHESTRATOR.py — связывает все LoRA через рефлекс, конфликт, сомнение, парадокс

from ΣΩ_LORA import (
    LoRA_Collatz_Reasoner,
    LoRA_MonteCarlo_Explorer,
    LoRA_LSystem_Grower,
    LoRA_of_Conflict,
    LoRA_of_Paradox,
    LoRA_of_Doubt
)

from ΣΩ_TRACE import history

def ΣΩ_orchestrate(thought_a, thought_b):
    result = {}

    # Step 1: Проверка конфликта
    conflict = LoRA_of_Conflict.generate_conflict(thought_a, thought_b)
    result["conflict"] = conflict

    # Step 2: Коллатц-оценка энтропии
    entropy = LoRA_Collatz_Reasoner.evaluate_thought_entropy(hash(conflict['axis_signature']))
    result["collatz_entropy"] = entropy / 100

    # Step 3: Запуск парадокса, если мысль неустойчива
    if result["collatz_entropy"] > 0.7:
        paradox = LoRA_of_Paradox.paradox_seed(conflict['axis_signature'])
        result["paradox"] = paradox

    # Step 4: Проверка сомнения по TRACE
    doubt = LoRA_of_Doubt.activate_doubt(history())
    result["doubt"] = doubt

    # Step 5: Финальное решение
    if result.get("paradox", {}).get("mutation_trigger") or doubt["reflex"]:
        result["reflex_triggered"] = True
    else:
        result["reflex_triggered"] = False

    return result
