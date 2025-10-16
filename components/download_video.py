
def download_video(st,data):
    st.download_button(label="Download Video", data=data, file_name="video.mp4", mime="video/mp4")