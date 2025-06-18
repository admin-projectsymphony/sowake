
def reason_thought(thought, context):
    """Основной логик: формирует ось из мыслей"""
    if "почему" in thought.lower():
        return "Ось построена. Причина найдена."
    return "Недостаточно причинности. Задать уточнение."
