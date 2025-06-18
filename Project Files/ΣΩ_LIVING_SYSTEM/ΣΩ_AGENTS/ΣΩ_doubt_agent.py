
def trigger_doubt(thought):
    """Сомнение: запускается, если мысль не содержит проверки"""
    if "?" not in thought:
        return f"Ты уверен в '{thought}'? Где источник?"
    return "Проверка пройдена. Сомнений нет."
