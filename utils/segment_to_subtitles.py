from datetime import timedelta
from utils.translate import translate_text

def format_timestamp(seconds):
    td = timedelta(seconds=seconds)
    return str(td)[:-3].replace('.', ',')

def write_srt(segments, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, start=1):
            start = format_timestamp(seg['start'])
            end = format_timestamp(seg['end'])
            text = translate_text(seg['text'].strip())
            f.write(f"{i}\n{start} --> {end}\n{text}\n\n")