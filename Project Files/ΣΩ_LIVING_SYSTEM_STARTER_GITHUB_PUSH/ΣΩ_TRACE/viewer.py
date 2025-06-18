import json

def load_lineage(path="ΣΩ_TRACE/lineage.jsonl"):
    with open(path) as f:
        return [json.loads(line) for line in f.readlines()]