from transformers import MarianMTModel, MarianTokenizer

def format_timestamp(seconds):
    """
    Convertit un nombre de secondes en format SRT (HH:MM:SS,mmm)
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"

def write_srt(segments, output_path, tokenizer=None, model=None):
    if tokenizer is None or model is None:
        model_name = "Helsinki-NLP/opus-mt-en-fr"
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)

    print(f"Écriture de {len(segments)} segments dans: {output_path}")

    texts_to_translate = [seg['text'].strip() for seg in segments]
    
    print("Traduction des segments en batch...")
    batch_size = 32
    translated_texts = []
    
    for i in range(0, len(texts_to_translate), batch_size):
        batch = texts_to_translate[i:i+batch_size]
        inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=512)
        translated = model.generate(**inputs)
        batch_translations = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
        translated_texts.extend(batch_translations)
        
        if i % 100 == 0:
            print(f"Traduit {i}/{len(texts_to_translate)} segments...")
    
    print(f"Traduction terminée: {len(translated_texts)} segments")

    with open(output_path, "w", encoding="utf-8") as f:
        for i, (seg, translated_text) in enumerate(zip(segments, translated_texts), start=1):
            start = format_timestamp(seg['start'])
            end = format_timestamp(seg['end'])
            f.write(f"{i}\n{start} --> {end}\n{translated_text}\n\n")
            
            print(f"Segment {i}: [{start} --> {end}] {translated_text[:50]}...")