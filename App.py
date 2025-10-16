import streamlit as st
import segment_to_subtitles as sts
from components.video_uploader import video_uploader

st.title('TranslIAtor')
video_uploader(st)