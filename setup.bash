#!/bin/bash

python -m venv .venv

.venv/Scripts/activate.bat

# install dependencies

echo "Vérification et installation des dépendances..."

pip show streamlit > /dev/null 2>&1 || pip install streamlit

pip show openai-whisper > /dev/null 2>&1 || pip install openai-whisper

pip show transformers > /dev/null 2>&1 || pip install transformers

pip show sentencepiece > /dev/null 2>&1 || pip install sentencepiece

pip show torch > /dev/null 2>&1 || pip install torch

pip show sacremoses > /dev/null 2>&1 || pip install sacremoses

pip show ffmpeg-python > /dev/null 2>&1 || pip install ffmpeg-python

echo "Toutes les dépendances sont installées!"

python -m streamlit run App.py