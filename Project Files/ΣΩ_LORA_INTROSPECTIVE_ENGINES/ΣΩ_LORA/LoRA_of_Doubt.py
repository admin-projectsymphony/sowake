# LoRA of Doubt: сомнение как механизм запуска мутации

def activate_doubt(trace_history):
    for trace in reversed(trace_history):
        if trace.get("entropy", 0.5) > 0.7:
            return {
                "reflex": True,
                "target": trace.get("axis_signature", "unknown"),
                "cause": "entropy_high"
            }
    return {
        "reflex": False,
        "cause": "no_high_entropy_found"
    }
