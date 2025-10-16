from components.video_player import video_player

def video_uploader(st):
    uploaded_file = st.file_uploader(label="Choose your video", type="mp4", accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")

    if uploaded_file is not None:
        with st.spinner("We prepare the video...", show_time=True):
            video_player(st, uploaded_file)
        # Déclencher transformation en format audio
    
    return None