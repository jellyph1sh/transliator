import streamlit as st
import segment_to_subtitles as sts
import video as vp
import translate as tr

st.write("Hello world")

# vp.video_player("ressources\Lartiste_-_Chocolat_feat._Awa_Imani_Clip_Officiel.mp4")
print(tr.translate_file("ressources\subtiltles.srt"))