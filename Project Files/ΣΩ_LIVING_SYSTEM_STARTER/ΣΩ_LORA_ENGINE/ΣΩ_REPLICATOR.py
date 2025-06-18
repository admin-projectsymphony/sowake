import json
import copy

with open("ΣΩ_LORA_ENGINE/LoRA_0_trained.json") as f:
    base = json.load(f)

replicas = []
for i in range(3):
    clone = copy.deepcopy(base)
    clone['name'] = f"LoRA_0_child_{i}"
    clone['reflex_score'] *= 0.95 + 0.01 * i
    clone['entropy'] *= 1.1 - 0.02 * i
    replicas.append(clone)

for r in replicas:
    with open(f"ΣΩ_LORA_ENGINE/{r['name']}.json", "w") as f:
        json.dump(r, f, indent=2)

print("🧬 Создано 3 дочерних LoRA.")