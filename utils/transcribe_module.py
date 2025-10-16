import whisper
from pathlib import Path

def transcribe_audio(file_path: str) -> str:
    model = whisper.load_model("medium", device="cpu")
    result = model.transcribe(file_path)
    text = result["segments"]
    language = result.get("language", "unknown")

    return {"lang": language, "text": text}
