
def translate_text(text, tokenizer, model):
    # On génère le nom du modèle en fonction des langues source et cible
    # On traduit le texte
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)