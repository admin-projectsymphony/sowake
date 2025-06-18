
@echo off
title ΣΩ_LAUNCHER
echo === ΣΩ Autostart Launcher ===
echo Starting ΣΩ_RUN_UI.py...
cd /d %~dp0ΣΩ_UI
start cmd /k "streamlit run ΣΩ_RUN_UI.py"

echo Starting Ollama (if installed)...
start cmd /k "ollama run llama3"

echo If using Godot, launch manually from ΣΩ_RENDER/mod_fractal_dream.tscn
pause
