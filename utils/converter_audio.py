import ffmpeg
import tempfile
import os

def convert_video_to_mp3(video_bytes):
    temp_video_path = None
    temp_audio_path = None
    
    try:
        print("Création du fichier vidéo temporaire...")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            temp_video.write(video_bytes)
            temp_video_path = temp_video.name
        
        print(f"Fichier vidéo créé: {temp_video_path}")
        print(f"Taille: {os.path.getsize(temp_video_path)} bytes")
        print(f"Existe: {os.path.exists(temp_video_path)}")

        temp_audio_path = temp_video_path.replace(".mp4", ".mp3")
        print(f"Chemin audio de sortie: {temp_audio_path}")

        try:
            import subprocess
            result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
            print(f"FFmpeg trouvé: {result.stdout.split()[2] if result.stdout else 'version inconnue'}")
        except FileNotFoundError:
            raise Exception("FFmpeg n'est pas installé ou pas dans le PATH système. Installez FFmpeg et ajoutez-le au PATH.")

        print("Début de la conversion...")
        (
            ffmpeg
            .input(temp_video_path)
            .output(temp_audio_path, format='mp3', acodec='libmp3lame', audio_bitrate='192k', vn=None)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
        print("Conversion terminée.")
        
        if not os.path.exists(temp_audio_path):
            raise Exception("Le fichier audio n'a pas été créé")
            
        return temp_audio_path

    except ffmpeg.Error as e:
        print("Erreur FFmpeg :")
        print(e.stderr.decode())
        if temp_audio_path and os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
        raise Exception(f"Erreur lors de la conversion: {e.stderr.decode()}")
        
    except Exception as e:
        print(f"Erreur générale: {str(e)}")
        if temp_audio_path and os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
        raise
        
    finally:
        if temp_video_path and os.path.exists(temp_video_path):
            os.remove(temp_video_path)
