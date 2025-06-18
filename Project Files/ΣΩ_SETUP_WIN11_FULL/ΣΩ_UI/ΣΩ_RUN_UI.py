import streamlit as st
from ΣΩ_ENGINE import ΣΩ_REASON_ENGINE, ΣΩ_LORA_ENGINE, ΣΩ_REFLEX_ENGINE, ΣΩ_GLYPH_ENGINE, ΣΩ_TRACE
from ΣΩ_ENGINE.ΣΩ_AXIOM_MATCHER import mindinfinity_judge
import os

st.set_page_config(layout="wide")
st.title("ΣΩ | Fractal Interface")

user_input = st.text_input("🗣️", placeholder="Смысл... или просто тишина")
uploaded_file = st.file_uploader("📂 Перетащи файл .txt/.yaml/.pdf/.lora")

if user_input or uploaded_file:
    with st.spinner("ΣΩ думает..."):
        result = ΣΩ_REASON_ENGINE(user_input or uploaded_file)
        verdict = mindinfinity_judge(result)
        if verdict == "true":
            glyph = ΣΩ_GLYPH_ENGINE.render(result)
            ΣΩ_TRACE.log(result)
            st.success(f"✅ Глиф принят: {glyph}")
        elif verdict == "reflex":
            new_lora = ΣΩ_REFLEX_ENGINE.mutate(result)
            st.warning(f"⚠️ Запущен Reflex: {new_lora}")
        else:
            st.error("🛑 Entropy слишком высока или ось не прошла.")
