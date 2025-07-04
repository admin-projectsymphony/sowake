PK    �d�Z$�M  �  "   ΣΩ_LORA/LoRA_Collatz_Reasoner.py# LoRA_Collatz_Reasoner: мышление по фракталу Коллатца

def collatz_reasoning(n, steps=0):
    if n == 1:
        return steps
    elif n % 2 == 0:
        return collatz_reasoning(n // 2, steps + 1)
    else:
        return collatz_reasoning(3 * n + 1, steps + 1)

def evaluate_thought_entropy(thought_hash: int):
    return collatz_reasoning(thought_hash % 9999)
PK    �d�Z�z��.  .  %   ΣΩ_LORA/LoRA_MonteCarlo_Explorer.py# LoRA_MonteCarlo_Explorer: вероятностный поиск истины

import random

def estimate_truth(lora_function, trials=1000):
    success = 0
    for _ in range(trials):
        result = lora_function()
        if result == 'true':
            success += 1
    return success / trials
PK    �d�ZY�՘O  O      ΣΩ_LORA/LoRA_LSystem_Grower.py# LoRA_LSystem_Grower: генерация осей как фрактала

def generate_axiom(axiom="A", rules={"A": "AB", "B": "A"}, depth=4):
    current = axiom
    for _ in range(depth):
        next_axiom = ""
        for ch in current:
            next_axiom += rules.get(ch, ch)
        current = next_axiom
    return current
PK    �d�Z$�M  �  "           �    ΣΩ_LORA/LoRA_Collatz_Reasoner.pyPK    �d�Z�z��.  .  %           ��  ΣΩ_LORA/LoRA_MonteCarlo_Explorer.pyPK    �d�ZY�՘O  O              �8  ΣΩ_LORA/LoRA_LSystem_Grower.pyPK      �   �    