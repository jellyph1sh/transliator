@echo off

python -m venv .venv

call .venv\Scripts\activate.bat

REM install dependencies

echo Verification et installation des dependances...

pip show streamlit >nul 2>&1 || pip install streamlit

pip show openai-whisper >nul 2>&1 || pip install openai-whisper

pip show transformers >nul 2>&1 || pip install transformers

pip show sentencepiece >nul 2>&1 || pip install sentencepiece

pip show torch >nul 2>&1 || pip install torch

pip show sacremoses >nul 2>&1 || pip install sacremoses

pip show ffmpeg-python >nul 2>&1 || pip install ffmpeg-python

echo Toutes les dependances sont installees!

python -m streamlit run App.py
