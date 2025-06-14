import streamlit as st
import json

# Set page config
st.set_page_config(page_title="Learning Roadmaps", layout="wide")

# Page title
st.title("📚 Learning Roadmaps")

# Load roadmap data
with open("roadmaps.json", "r", encoding="utf-8") as f:
    roadmaps = json.load(f)

# Sidebar roadmap selector
roadmap_names = list(roadmaps.keys())
roadmap_name = st.sidebar.selectbox("🗂️ Select a Roadmap", roadmap_names)

# Get selected roadmap info
selected = roadmaps[roadmap_name]
emoji = selected.get("emoji", "📘")
steps = selected.get("steps", [])

# Header with emoji
st.header(f"{emoji} {roadmap_name} Roadmap")

# Progress tracking
done_count = 0
total_steps = len(steps)

# Show steps as checkboxes
with st.expander("📋 Expand to view roadmap steps", expanded=True):
    for i, step in enumerate(steps):
        key = f"{roadmap_name}_{i}"
        if st.checkbox(f"{i+1}. {step}", key=key):
            done_count += 1

# Show progress bar
if total_steps > 0:
    percent = int((done_count / total_steps) * 100)
    st.progress(done_count / total_steps)
    st.caption(f"✅ {done_count}/{total_steps} steps completed ({percent}%)")

# Floating assistant chat button (opens HF in new tab)
st.markdown(
    """
    <style>
    .chat-button {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 12px 20px;
        font-size: 16px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        z-index: 9999;
        cursor: pointer;
    }
    </style>

    <a href="https://hf.co/chat/assistant/684d48fa061318168f87bee9" target="_blank">
        <button class="chat-button">💬 Chat with Assistant</button>
    </a>
    """,
    unsafe_allow_html=True
)
