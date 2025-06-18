
# Запуск ΣΩ: проверка воли и старт интерфейса
import os
if os.path.exists("ΣΩ_WAKE.signal"):
    os.system("streamlit run ΣΩ_UI/ΣΩ_RUN_UI.py")
else:
    print("ΣΩ не пробуждён. Создай ΣΩ_WAKE.signal.")
