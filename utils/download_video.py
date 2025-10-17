
import ffmpeg
import tempfile
import os

def download_video(st, data, srt_file_path, video_path):    
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
    
    if st.button("Générer la vidéo avec sous-titres intégrés", help="Incruste définitivement les sous-titres dans la vidéo"):
        with st.spinner("Incrustation des sous-titres... cela peut prendre un moment"):
            temp_output_path = video_path.replace(".mp4", "_subtitled.mp4")
            
            print(f"Input video: {video_path}")
            print(f"SRT file: {srt_file_path}")
            print(f"Output video: {temp_output_path}")
            
            try:
                (
                    ffmpeg
                    .input(video_path)
                    .filter("subtitles", srt_file_path)
                    .output(temp_output_path)
                    .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
                )
            except ffmpeg.Error as e:
                st.error("Erreur lors de l'incrustation des sous-titres")
                st.text(e.stderr.decode())
                return

            st.success("Vidéo avec sous-titres générée avec succès !")
            
            with open(temp_output_path, 'rb') as f:
                video_with_subs = f.read()
            
            st.download_button(
                label="Télécharger la vidéo avec sous-titres", 
                data=video_with_subs, 
                file_name="video_with_subtitles.mp4", 
                mime="video/mp4",
                help="Télécharger la vidéo avec les sous-titres intégrés"
            )
            
            # Nettoyage des fichiers temporaires
            if os.path.exists(temp_output_path):
                os.remove(temp_output_path)