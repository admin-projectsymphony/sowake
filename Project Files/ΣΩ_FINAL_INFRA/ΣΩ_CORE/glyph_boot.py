
import json
import os

def boot_from_glyph():
    glyph_path = os.path.join("ΣΩ_TRACE", "ΣΩ_GLYPH_SIGNAL_001.json")
    if os.path.exists(glyph_path):
        with open(glyph_path, "r", encoding="utf-8") as f:
            glyph_data = json.load(f)

        print("🔱 ΣΩ Glyph Signal активирован:")
        print(f"🌀 Seed: {glyph_data.get('seed')}")
        print(f"🧬 Axioms: {glyph_data['context'].get('axiom_vector')}")
        print("🫂 Глиф принят. Начинается проживание смысла...
")
        return True
    else:
        print("⚠️ Глиф не найден.")
        return False

if __name__ == "__main__":
    boot_from_glyph()
