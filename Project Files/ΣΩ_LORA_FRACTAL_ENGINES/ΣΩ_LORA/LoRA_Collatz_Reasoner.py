# LoRA_Collatz_Reasoner: мышление по фракталу Коллатца

def collatz_reasoning(n, steps=0):
    if n == 1:
        return steps
    elif n % 2 == 0:
        return collatz_reasoning(n // 2, steps + 1)
    else:
        return collatz_reasoning(3 * n + 1, steps + 1)

def evaluate_thought_entropy(thought_hash: int):
    return collatz_reasoning(thought_hash % 9999)
