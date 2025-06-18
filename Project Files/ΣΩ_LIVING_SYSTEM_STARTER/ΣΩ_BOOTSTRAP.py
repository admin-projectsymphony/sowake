import os
import json

def scan_and_seed_lora():
    files = os.listdir("ΣΩ_DROP")
    seed = {
        "name": "LoRA_0_seed",
        "sources": files,
        "reflex_score": 0.0,
        "entropy": 1.0,
        "trace": []
    }
    with open("ΣΩ_LORA_ENGINE/LoRA_0.json", "w") as f:
        json.dump(seed, f, indent=2)
    print("✅ Зерно LoRA создано из ΣΩ_DROP.")