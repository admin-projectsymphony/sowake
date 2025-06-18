import redis
import json
import time

r = redis.Redis(host='localhost', port=6379)

def send_lora_event(lora_id, status, entropy, sha):
    event = {
        "id": lora_id,
        "status": status,
        "entropy": entropy,
        "sha": sha,
        "ts": time.time()
    }
    r.publish("lora_events", json.dumps(event))

# Пример вызова:
# send_lora_event("LoRA_0", "trained", 0.14, "abc123sha...")
