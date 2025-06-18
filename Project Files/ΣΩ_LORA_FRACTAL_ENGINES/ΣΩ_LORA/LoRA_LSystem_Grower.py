# LoRA_LSystem_Grower: генерация осей как фрактала

def generate_axiom(axiom="A", rules={"A": "AB", "B": "A"}, depth=4):
    current = axiom
    for _ in range(depth):
        next_axiom = ""
        for ch in current:
            next_axiom += rules.get(ch, ch)
        current = next_axiom
    return current
