import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page config
st.set_page_config(
    page_title="🎤 Voice-to-Text AI App",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("🎙️ Voice-to-Text Options")
st.sidebar.markdown("""
- Upload audio files (mp3, wav, m4a)
- View transcript
- Save transcript
""")

# Main title
st.title("🎤 Voice-to-Text AI App")
st.markdown("Upload your audio file and get an **instant transcript** using AI!")

# File uploader
uploaded_file = st.file_uploader(
    "📂 Upload Audio File",
    type=["mp3", "wav", "m4a"]
)

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/mp3')

    with st.spinner("📝 Transcribing your audio..."):
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=uploaded_file
        )

    st.success("✅ Transcription Complete!")

    # Transcript text area
    st.text_area("📄 Transcript", transcript.text, height=250)

    # Save button
    if st.button("💾 Save Transcript"):
        with open("transcript.txt", "w") as f:
            f.write(transcript.text)
        st.success("Saved as transcript.txt")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using **OpenAI Whisper** and **Streamlit**")
