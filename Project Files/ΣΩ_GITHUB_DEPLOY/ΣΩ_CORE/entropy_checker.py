
def check_entropy(text):
    from collections import Counter
    freq = Counter(text)
    entropy = sum(-p * (p / len(text)) for p in freq.values())
    return entropy
