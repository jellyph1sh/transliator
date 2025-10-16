
import ffmpeg
import tempfile
import os

def download_video(st, data, srt_file_path):    
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="Download Original Video", 
            data=data, 
            file_name="video.mp4", 
            mime="video/mp4",
            help="Download the original video without subtitles"
        )
    
    with col2:
        if os.path.exists(srt_file_path):
            with open(srt_file_path, 'rb') as f:
                srt_data = f.read()
            st.download_button(
                label="Download Subtitles (SRT)", 
                data=srt_data, 
                file_name="subtitles.srt", 
                mime="text/plain",
                help="Download the subtitle file"
            )
    
    st.markdown("---")
    
    if st.button("Generate Video with Burned Subtitles", help="This will embed subtitles permanently into the video"):
        with st.spinner("Burning subtitles into video... This may take a moment."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_input:
                temp_input.write(data.read() if hasattr(data, 'read') else data)
                temp_input_path = temp_input.name
            
            temp_output_path = temp_input_path.replace(".mp4", "_subtitled.mp4")
            
            srt_path_escaped = srt_file_path.replace('\\', '/').replace(':', '\\:')
            
            print(f"Input video: {temp_input_path}")
            print(f"SRT file: {srt_file_path}")
            print(f"Output video: {temp_output_path}")
            
            (
                ffmpeg
                .input(temp_input_path)
                .output(
                    temp_output_path,
                    vf=f"subtitles={srt_path_escaped}",
                    vcodec='libx264',
                    acodec='aac',
                    strict='experimental'
                )
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )
            
            print("Video with subtitles created successfully!")
            
            with open(temp_output_path, 'rb') as f:
                video_with_subs = f.read()
            
            st.success("Video with subtitles generated successfully!")
            st.download_button(
                label="Download Video with Subtitles", 
                data=video_with_subs, 
                file_name="video_with_subtitles.mp4", 
                mime="video/mp4",
                help="Download the video with burned-in subtitles"
            )
            
            if os.path.exists(temp_input_path):
                os.remove(temp_input_path)
            if os.path.exists(temp_output_path):
                os.remove(temp_output_path)