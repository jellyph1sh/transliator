import streamlit as st
from components.download_video import download_video


def main():
    st.header('Welcome to Transliator !')

    st.sidebar.image('ressources\logo.png')

    uploaded_file = st.file_uploader(label="Choose your video", type="mp4", accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")

    if uploaded_file is not None:
        with st.spinner("We prepare the video...", show_time=True):
            # Déclencher transformation en format audio
            st.video(uploaded_file, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False, width="stretch")
            download_video(st, uploaded_file)
main()