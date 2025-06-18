import json

def self_reflect(lora_file):
    with open(lora_file) as f:
        lora = json.load(f)

    if lora['entropy'] > 0.08 or lora['reflex_score'] < 0.5:
        print(f"⚠️ {lora['name']} не прошёл саморефлексию.")
        return False
    print(f"✅ {lora['name']} прошёл саморефлексию.")
    return True