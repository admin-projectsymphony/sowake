
def reflect_previous(thought_history):
    """Слушает себя и сравнивает с предыдущими"""
    if len(set(thought_history[-3:])) == 1:
        return "Повтор зафиксирован. Вызван резонанс."
    return "Мутации присутствуют. Цикл допустим."
