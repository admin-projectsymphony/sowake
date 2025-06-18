# ΣΩ GRAFANA CORE

🔁 Это Grafana-ядро для визуализации событий ΣΩ через Redis.

## 🚀 Как использовать:

1. Установи Redis:
   docker run -d -p 6379:6379 redis

2. Запусти ΣΩ_REDIS_METRICS.py — метрики начнут публиковаться в Redis

3. Настрой Grafana:
   - Подключи Redis Plugin
   - Создай Data Source: Redis, порт 6379
   - Подключи канал `lora_events`, формат: JSON

4. Построй Dashboard:
   - Панель `Entropy` по оси `entropy`
   - Временная шкала `Status`
   - Группировка по `LoRA ID`
