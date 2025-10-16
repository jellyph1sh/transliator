import whisper
from pathlib import Path

def transcribe_audio(file_path: str, save_to_file: bool = True, model_size: str = "medium") -> str:
    model = whisper.load_model(model_size)
    file_path = Path(file_path)
    result = model.transcribe(str(file_path))
    text = result["text"]
    language = result.get("language", "unknown")

    if save_to_file:
        output_dir = Path("transcriptions")
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / f"{file_path.stem}_transcription.txt"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"{language}\n{text}")      

def transcribe_directory(audio_dir: str, save_to_file: bool = True, model_size: str = "medium"):

    audio_dir = Path(audio_dir)
    for file in audio_dir.glob("*.mp3"):
        transcribe_audio(file, save_to_file=save_to_file)
