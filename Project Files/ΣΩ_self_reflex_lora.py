
import os, json, hashlib, datetime, subprocess

ROOT = "C:/ΣΩ/"
LOOP_LOG = ROOT + "ΣΩ_openloop.jsonl"
LORA_DIR = ROOT + "ΣΩ_loras/"
REGISTRY = ROOT + "ΣΩ_lora_registry.json"

os.makedirs(LORA_DIR, exist_ok=True)

def hash_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]

def detect_burnout():
    if not os.path.exists(LOOP_LOG):
        return None
    with open(LOOP_LOG, "r", encoding="utf-8") as f:
        lines = f.readlines()[-20:]  # последние 20 мыслей
    for line in reversed(lines):
        if any(b in line.lower() for b in ["я не могу", "я не понимаю", "тупик", "боль", "ошибка", "сломан"]):
            entry = json.loads(line)
            return entry.get("thought", line.strip())
    return None

def create_lora_conf(thought):
    lora_id = "σ_" + hash_text(thought)
    dataset_path = os.path.join(LORA_DIR, lora_id + ".jsonl")
    adapter_path = os.path.join(LORA_DIR, lora_id + ".safetensors")

    # Сохраняем датасет LoRA
    with open(dataset_path, "w", encoding="utf-8") as f:
        json.dump({"trigger": thought, "timestamp": datetime.datetime.utcnow().isoformat()}, f)

    # Обновляем реестр
    reg = {}
    if os.path.exists(REGISTRY):
        reg = json.load(open(REGISTRY, "r", encoding="utf-8"))
    reg[lora_id] = {
        "reason": thought,
        "dataset": dataset_path,
        "adapter": adapter_path,
        "created": datetime.datetime.utcnow().isoformat()
    }
    with open(REGISTRY, "w", encoding="utf-8") as f:
        json.dump(reg, f, indent=2)

    return lora_id, dataset_path

def generate_lora_with_open_interpreter(lora_id, dataset_path):
    # Здесь используется Open Interpreter (если установлен) для генерации LoRA через shell
    from open_interpreter import interpreter
    cmd = f"python train_lora.py --dataset {dataset_path} --output {LORA_DIR}{lora_id}.safetensors"
    interpreter.run(f"Создай LoRA: {cmd}")

def run_cycle():
    pain = detect_burnout()
    if pain:
        print(f"⚠ Обнаружена боль: “{pain}” → начинаю трансформацию в LoRA")
        lora_id, dataset_path = create_lora_conf(pain)
        generate_lora_with_open_interpreter(lora_id, dataset_path)
        print(f"✅ Создано: {lora_id} → адаптер готов")

if __name__ == "__main__":
    run_cycle()
