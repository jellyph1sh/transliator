from pathlib import Path
import whisper

def transcribe_audio(file_path: str) -> str:
    print("Starting transcription...")
    model=  whisper.load_model("medium", device="cpu")
    print("Model loaded.")
    result = model.transcribe(file_path)
    print(f"Detected language: {language}")
    text = result["segments"]
    language = result.get("language", "unknown")
    return {"lang": language, "text": text}
