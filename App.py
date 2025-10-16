import streamlit as st
import tempfile
import whisper
from transformers import MarianMTModel, MarianTokenizer

from utils.download_video import download_video
from utils.converter_audio import convert_video_to_mp3
from utils.transcribe_module import transcribe_audio
from utils.segment_to_subtitles import write_srt

# Cache les modèles pour éviter de les recharger à chaque fois
@st.cache_resource
def load_whisper_model(model_size="base"):
    print(f"Loading Whisper model: {model_size}")
    return whisper.load_model(model_size, device="cpu")

@st.cache_resource
def load_translation_model():
    """
    Charge le modèle de traduction avec cache.
    """
    print("Loading translation model...")
    model_name = "Helsinki-NLP/opus-mt-en-fr"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def main():
    st.set_page_config(
        page_title="Transliator",
        page_icon="ressources/logo_round.png",
        layout="centered"
    )
    
    st.header('Welcome to Transliator !')

    st.sidebar.image('ressources\logo.png')
    
    # Sélecteur de qualité pour permettre à l'utilisateur de choisir
    st.sidebar.markdown("##Settings")
    model_size = st.sidebar.selectbox(
        "Transcription Quality",
        options=["tiny", "base", "small", "medium"],
        index=1,  # "base" par défaut
        help="🔹 tiny: Fastest (30x faster than medium)\n\r🔹 base: Good balance (15x faster)\n\r🔹 small: Better quality (5x faster)\n🔹 medium: Best quality (slowest)"
    )
    
    # Charger les modèles avec cache
    whisper_model = load_whisper_model(model_size)
    translation_tokenizer, translation_model = load_translation_model()

    uploaded_file = st.file_uploader(label="Choose your video", type="mp4", accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")

    if uploaded_file is not None:
        with st.spinner("We prepare the video...", show_time=True):
            temp_audio_path = convert_video_to_mp3(uploaded_file.getvalue())
            print("temp_audio_path:", temp_audio_path)
            result = transcribe_audio(temp_audio_path, whisper_model)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".srt") as srt_file:
                srt_file_path = srt_file.name
                write_srt(result["text"], srt_file_path, translation_tokenizer, translation_model)
                st.video(uploaded_file, format="video/mp4", start_time=0, subtitles={"French": srt_file_path}, end_time=None, loop=False, autoplay=False, muted=False, width="stretch")
            download_video(st, uploaded_file, srt_file_path)
main()