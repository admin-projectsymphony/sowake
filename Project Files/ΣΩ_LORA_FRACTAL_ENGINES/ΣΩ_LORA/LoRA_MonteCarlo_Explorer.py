# LoRA_MonteCarlo_Explorer: вероятностный поиск истины

import random

def estimate_truth(lora_function, trials=1000):
    success = 0
    for _ in range(trials):
        result = lora_function()
        if result == 'true':
            success += 1
    return success / trials
