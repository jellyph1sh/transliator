from pathlib import Path
import whisper
import os

def transcribe_audio(file_path: str, model: whisper.Whisper) -> dict:
    print("Starting transcription...")
    
    # Vérifier que le fichier existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier audio n'existe pas: {file_path}")
    
    print(f"Fichier trouvé: {file_path}")
    print(f"Taille du fichier: {os.path.getsize(file_path)} bytes")
    
    try:        
        result = model.transcribe(file_path)
        
        # Récupérer les informations AVANT de les utiliser
        language = result.get("language", "unknown")
        text = result["segments"]
        
        print(f"Detected language: {language}")
        print(f"Number of segments: {len(text)}")
        print(f"First segment: {text[0] if text else 'No segments'}")
        
        return {"lang": language, "text": text}
        
    except Exception as e:
        print(f"Erreur lors de la transcription: {str(e)}")
        raise
