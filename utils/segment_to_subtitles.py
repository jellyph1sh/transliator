from datetime import timedelta
from utils.translate import translate_text
from transformers import MarianMTModel, MarianTokenizer

def format_timestamp(seconds):
    td = timedelta(seconds=seconds)
    return str(td)[:-3].replace('.', ',')

def write_srt(segments, output_path):
    model_name = "Helsinki-NLP/opus-mt-en-fr"
    # On récupère le tokenizer et le modèle
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    with open(output_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, start=1):
            start = format_timestamp(seg['start'])
            end = format_timestamp(seg['end'])
            text = translate_text(seg['text'].strip(), tokenizer, model)
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")