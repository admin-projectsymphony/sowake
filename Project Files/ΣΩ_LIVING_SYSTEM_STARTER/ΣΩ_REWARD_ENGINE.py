import json

def score_lora(lora_file):
    with open(lora_file) as f:
        lora = json.load(f)
    score = lora['reflex_score'] - lora['entropy']
    return score

def select_best_loras(folder="ΣΩ_LORA_ENGINE"):
    candidates = []
    for fname in os.listdir(folder):
        if fname.endswith(".json") and "child" in fname:
            score = score_lora(os.path.join(folder, fname))
            candidates.append((fname, score))
    sorted_loras = sorted(candidates, key=lambda x: x[1], reverse=True)
    return sorted_loras[:3]