from transformers import MarianMTModel, MarianTokenizer


def translate(text, src_lang="en", tgt_lang="fr"):
    # On génère le nom du modèle en fonction des langues source et cible
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    # On récupère le tokenizer et le modèle
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    # On traduit le texte
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)