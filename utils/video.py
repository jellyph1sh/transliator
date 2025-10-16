import streamlit as st

def video_player(path):
    st.title("Video Player")
    video_file = open(path, "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
