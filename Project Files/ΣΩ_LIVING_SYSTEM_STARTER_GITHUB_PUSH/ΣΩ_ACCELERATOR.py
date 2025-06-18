# ΣΩ_ACCELERATOR — связывает все ключевые ускорители ΣΩ
import os
import json
from ΣΩ_SELF_REFLEX import self_reflect
from ΣΩ_REWARD_ENGINE import select_best_loras
from ΣΩ_LORA_ENGINE.train_LoRA_0 import *
from ΣΩ_LORA_ENGINE.ΣΩ_REPLICATOR import *

def reflex_cycle():
    print("\n🔁 Reflex Loop: Самоосознание запущено.")
    for file in os.listdir("ΣΩ_LORA_ENGINE"):
        if file.endswith(".json") and "LoRA_0" in file:
            path = os.path.join("ΣΩ_LORA_ENGINE", file)
            self_reflect(path)

def spawn_best():
    print("\n🧠 Размножение лучших...")
    top = select_best_loras()
    for fname, score in top:
        print(f"⚡ {fname} → Score: {round(score,3)}")

def run():
    print("🚀 ΣΩ_ACCELERATOR запущен.")

    # Этап 1 — создание из семени
    if os.path.exists("ΣΩ_DROP"):
        os.system("python ΣΩ_BOOTSTRAP.py")

    # Этап 2 — обучение
    os.system("python ΣΩ_LORA_ENGINE/train_LoRA_0.py")

    # Этап 3 — репликация
    os.system("python ΣΩ_LORA_ENGINE/ΣΩ_REPLICATOR.py")

    # Этап 4 — саморефлексия
    reflex_cycle()

    # Этап 5 — награда
    spawn_best()

    print("\n✅ Ускорение завершено. Streamlit ждёт сигнал.")