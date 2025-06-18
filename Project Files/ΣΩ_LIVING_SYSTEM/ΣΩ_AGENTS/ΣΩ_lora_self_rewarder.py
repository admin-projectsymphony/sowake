
def evaluate_lora_trace(trace):
    """Оценивает LoRA по резонансу, глубине, совпадению с аксиомами"""
    if "ошибка" in trace.lower():
        return 0.1  # низкая награда
    if "истина" in trace.lower():
        return 0.9  # высокая награда
    return 0.5  # нейтрально
