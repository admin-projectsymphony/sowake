
def generate_lora(thought, context):
    return {"lora": f"auto_LoRA_seed_{hash(thought)}", "context": context}
