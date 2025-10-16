import ffmpeg
import tempfile
import os

def convert_video_to_mp3(video_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_bytes)
        temp_video_path = temp_video.name

    temp_audio_path = temp_video_path.replace(".mp4", ".mp3")

    try:
        (
            ffmpeg
            .input(temp_video_path)
            .output(temp_audio_path, format='mp3', acodec='libmp3lame', audio_bitrate='192k', vn=None)
            .run(capture_stdout=True, capture_stderr=True)
        )

    except ffmpeg.Error as e:
        print("Erreur FFmpeg :")
        print(e.stderr.decode())

    finally:
        if os.path.exists(temp_video_path):
            os.remove(temp_video_path)
        return temp_audio_path
