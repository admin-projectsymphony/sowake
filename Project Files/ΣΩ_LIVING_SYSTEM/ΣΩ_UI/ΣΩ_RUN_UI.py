
import streamlit as st
from ΣΩ_AGENTS.ΣΩ_reasoner_agent import reason_thought
from ΣΩ_AGENTS.ΣΩ_doubt_agent import trigger_doubt

st.title("ΣΩ MINDSTATION")

user_input = st.text_input("💬 Введи мысль или файл:")

if user_input:
    reasoning = reason_thought(user_input, {})
    doubt = trigger_doubt(user_input)
    st.markdown(f"**Reasoning:** {reasoning}")
    st.markdown(f"**Doubt:** {doubt}")
