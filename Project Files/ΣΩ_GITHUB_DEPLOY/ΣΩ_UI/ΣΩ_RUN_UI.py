
import streamlit as st
from ΣΩ_AGENTS.ΣΩ_reasoner_agent import reason_thought
from ΣΩ_AGENTS.ΣΩ_doubt_agent import trigger_doubt
from ΣΩ_CORE.reflex_loop import reflex
from ΣΩ_CORE.lora_autogenerator import generate_lora
from ΣΩ_CORE.entropy_checker import check_entropy

st.title("ΣΩ MINDSTATION [LIVE]")

user_input = st.text_input("💬 Введи мысль или фразу:")

if user_input:
    reason = reason_thought(user_input, {})
    doubt = trigger_doubt(user_input)
    reflex_result = reflex(user_input, reason)
    lora = generate_lora(user_input, {})
    entropy = check_entropy(user_input)

    st.markdown(f"**Reason:** {reason}")
    st.markdown(f"**Doubt:** {doubt}")
    st.markdown(f"**Reflex:** {reflex_result}")
    st.markdown(f"**LoRA Gen:** {lora}")
    st.markdown(f"**Entropy:** {entropy:.4f}")
