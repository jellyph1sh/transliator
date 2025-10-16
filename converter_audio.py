import ffmpeg
import io

def convert_video_to_mp3():
    uploaded_file = request.files['file']      # récupère le fichier uploadé
    video_bytes = uploaded_file.read()         # lit les bytes en mémoire

    # Extraction audio en mémoire
    out, _ = (
        ffmpeg
        .input('pipe:0')        # lecture depuis stdin
        .output('pipe:1', format='mp3', vn=None)  # vn=None = no video
        .run(input=video_bytes, capture_stdout=True, capture_stderr=True)
    )

    # Renvoie le MP3 directement au client
    return send_file(
        io.BytesIO(out),
        mimetype='audio/mpeg',
        as_attachment=True,
        download_name='audio.mp3'
    )