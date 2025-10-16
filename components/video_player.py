def video_player(st, data):
    st.video(data, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False, width="stretch")