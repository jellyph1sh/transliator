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

def write_srt(segments, src_language, output_path, target_language="fr"):

    texts_to_translate = [seg['text'].strip() for seg in segments]
    
    batch_size = 32
    translated_texts = []

    if src_language == target_language:
        translated_texts = texts_to_translate
    else:
        print("Traduction des segments en batch...")
        model_name = f"Helsinki-NLP/opus-mt-{src_language}-{target_language}"
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        for i in range(0, len(texts_to_translate), batch_size):
            batch = texts_to_translate[i:i+batch_size]
            inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=512)
            translated = model.generate(**inputs)
            batch_translations = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
            translated_texts.extend(batch_translations)
    
    print(f"Traduction terminée: {len(translated_texts)} segments")

    with open(output_path, "w", encoding="utf-8") as f:
        for i, (seg, translated_text) in enumerate(zip(segments, translated_texts), start=1):
            start = format_timestamp(seg['start'])
            end = format_timestamp(seg['end'])
            f.write(f"{i}\n{start} --> {end}\n{translated_text}\n\n")
            
            print(f"Segment {i}: [{start} --> {end}] {translated_text[:50]}...")