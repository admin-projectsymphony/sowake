
def reflex(thought, result):
    if "не понимаю" in result or result.strip() == "":
        return f"⚠️ Reflex: перезапуск для мысли: '{thought}'"
    return "Понимание достигнуто."
