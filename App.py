import streamlit as st
import tempfile
from components.download_video import download_video
from utils.converter_audio import convert_video_to_mp3
from utils.transcribe_module import transcribe_audio
from utils.segment_to_subtitles import write_srt


def main():
    st.header('Welcome to Transliator !')

    st.sidebar.image('ressources\logo.png')

    uploaded_file = st.file_uploader(label="Choose your video", type="mp4", accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")

    if uploaded_file is not None:
        with st.spinner("We prepare the video...", show_time=True):
            temp_audio_path = convert_video_to_mp3(uploaded_file.getvalue())
            result = transcribe_audio(temp_audio_path)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as srt_file:
                srt_file_path = srt_file.name
                write_srt(result["text"], srt_file_path)
                st.video(uploaded_file, format="video/mp4", start_time=0, subtitles={"French": srt_file_path}, end_time=None, loop=False, autoplay=False, muted=False, width="stretch")
            download_video(st, uploaded_file)
main()