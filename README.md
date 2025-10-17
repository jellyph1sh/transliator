## 🌐 Transliator

**Transliator** est une application Python conçue pour automatiser la traduction et la transformation de texte à partir d'une vidéo.  
Elle fournit une interface simple et portable permettant de traduire des fichiers ou des phrases directement depuis la ligne de commande ou via un conteneur Docker.

---

## 🧩 Technologie

Langage : Python  
Framework Web : Streamlit

Tout les membres du groupes connaisse python et streamlit est une solution rapide pour faire un application.

---

## 🧠 Présentation

Transliator vise à simplifier le processus de traduction automatique à travers :

- Une configuration rapide

- Une compatibilité multi-environnements

- Une interface intuitive (locale ou web)

- Une intégration Docker pour un déploiement instantané

Comme avantages il est :

- ⚡ Léger et rapide : conçu pour une utilisation immédiate

- ✅ Portable : fonctionne sur Windows, Linux et macOS

- 🐳 Dockerisable : lancement en un clic via un DOCKERFILE

  
---

## ⚙️ Fonctionnalités principales


L’utilisateur peut :
- "Drag and Drop" un fichier video sur l'interface ou juste l'importer

- Traduire du texte ou des fichiers (audio/texte)

- Choisir la langue de traduction

- Visualiser les résultats instantanément via Streamlit

- Exécuter l’application en local ou dans un conteneur Docker

- Gérer les dépendances automatiquement via les scripts setup.bat ou setup.bash

---

## 🏗️ Structure du projet

transliator/  
├── App.py # Fichier principal  
├── requirements.txt # Dépendances Python  
├── DOCKERFILE # Déploiement Docker  
├── utils # Utilitaires
├── ressources # images, etc
├── dockerise.bat # Script Windows pour build Docker  
├── setup.bash / setup.bat # Scripts d’installation  
├── .devcontainer/ # Configuration VS Code  
└── README.md # Documentation  


---

## 🛠️SETUP ##

Exécuter un des script setup.

Dans les script "Setup" on peut y retrouver les commandes suivantes: 

- python -m venv .venv

- call .venv\Scripts\activate.bat

- REM install dependencies

- echo Verification et installation des dependances...

- pip show streamlit >nul 2>&1 || pip install streamlit

- pip show openai-whisper >nul 2>&1 || pip install openai-whisper

- pip show transformers >nul 2>&1 || pip install transformers

- pip show sentencepiece >nul 2>&1 || pip install sentencepiece

- pip show torch >nul 2>&1 || pip install torch

- pip show sacremoses >nul 2>&1 || pip install sacremoses

- pip show ffmpeg-python >nul 2>&1 || pip install ffmpeg-python

- echo Toutes les dependances sont installees!

- python -m streamlit run App.py


# 🚀 Lancement


1. Executer le script ".\setup.bash" ou .\setup.bat sur le terminal puis cLiquer sur l'adresse de l'URL network


2. Executer dans le terminal ".venv/Scripts/activate.bat" puis "python -m streamlit run App.py"


# Docker 

L'image du projet peut être générée à l'aide du Dockerfile.




