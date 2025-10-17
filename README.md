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


## 🚀 Lancement


1. Executer le script ".\setup.bash" ou .\setup.bat sur le terminal puis cLiquer sur l'adresse de l'URL network


2. Executer dans le terminal ".venv/Scripts/activate.bat" puis "python -m streamlit run App.py"


## 🐳 Docker 

L'image du projet peut être générée à l'aide du Dockerfile.


# Analyse énergétique et éthique

## 1. Analyse énergétique et écologique

### 1.1. Consommation énergétique

**Navigateur web (Chrome)**

- **Page initiale :** mémoire ~180 Mo, CPU négligeable  
- **Upload + traitement vidéo :** mémoire ~320 Mo, CPU ~4% sur 16 cœurs (soit 0,64 W par cœur estimé à 10 W)  
- **Download vidéo traitée :** mémoire ~250 Mo, CPU ~3% sur 16 cœurs  

**Impact :** faible consommation énergétique. L’utilisation du navigateur est adaptée à des tâches légères et reste écologique pour des usages simples.  
**Consommation estimée (10 min) :** ~0,0011 kWh  

**Docker**

- **Initialisation :** mémoire ~760 Mo, CPU ~0,1% sur 16 cœurs  
- **Upload + traitement vidéo :** mémoire ~1,15 Go, CPU ~800% (soit 8 cœurs à 100% chacun, puissance ~10 W/cœur)  
- **Download vidéo traitée :** mémoire ~1 Go, CPU ~150% (soit 1,5 cœurs à 100%)  

**Impact :** traitement intensif très énergivore. L’utilisation de 8 cœurs simultanément entraîne une consommation électrique notable.  
**Consommation estimée (10 min) :**  
- Upload + traitement vidéo : 8 cœurs × 10 W × 0,1667 h ≈ 0,0133 kWh  
- Download vidéo : 1,5 cœurs × 10 W × 0,1667 h ≈ 0,0025 kWh  

---

### 1.2. Consommation estimée et comparaison

| Logiciel / Application | Mémoire | CPU utilisé | Nb de cœurs équivalents | Puissance estimée (W) | Consommation estimée (kWh / 10 min) | Impact écologique | Remarques |
|------------------------|----------|--------------|--------------------------|-----------------------|--------------------------------------|------------------|------------|
| **Chrome** | ~320 Mo | 4 % | 0,04 | 0,4 W | **0,00007 kWh** | Très faible | Activité légère, navigation ou upload simple. |
| **Docker** | ~1,15 Go | 800 % | 8 | 80 W | **0,0133 kWh** | Élevé | Traitement intensif, 8 cœurs sollicités simultanément. |
| Comparaison |
| **Adobe Photoshop** | ~1–2 Go | 400–600 % | 4–6 | 40–60 W | **0,0067–0,010 kWh** | Modéré à élevé | Calculs complexes (filtres, export). |
| **Discord** | ~400 Mo | 40–60 % | 0,4–0,6 | 4–6 W | **0,00067–0,0010 kWh** | Faible | Appel audio/vidéo, charge modérée. |
| **Microsoft Word** | ~200 Mo | 4–30 % | 0,04–0,3 | 0,4–3 W | **0,00007–0,0005 kWh** | Très faible | Activité bureautique simple. |

compréhensions : 0.01 kWh = 1 charge (10W) d'un smartphone pendant 1 heure ou allumer 1 ampoule 100 W pendant 6 minutes
                 
> ⚠ Les calculs sont basés sur :  
> - Puissance CPU estimée : 10 W par cœur en charge complète  
> - Durée : 10 minutes = 0,1667 h  
> - kWh = Puissance totale (kW) × durée (h)  

---

### 1.3. Implications écologiques et éthiques

#### Implications écologiques et éthiques

- La consommation énergétique explose **pendant le traitement vidéo**, ce qui peut avoir un impact carbone notable, surtout si plusieurs utilisateurs effectuent ces traitements.  
- Les logiciels optimisés (Photoshop) utilisent **moins de ressources pour un traitement intensif**, montrant qu’il est possible de réduire l’impact sans sacrifier la performance.  
- **Responsabilité des développeurs** : optimiser le code, exploiter le GPU, fractionner les traitements lourds.  
- **Sensibilisation des utilisateurs** : informer sur l’impact énergétique et proposer des alternatives moins lourdes pour les petites vidéos ou les tests.

#### Pour une solution durable

- Optimiser le code pour limiter l’utilisation CPU maximale pendant le traitement.  
- Exploiter le GPU pour soulager le CPU et réduire la consommation.  
- Fractionner ou différer les traitements lourds pour réduire la puissance simultanément utilisée.  
- Favoriser les serveurs/machines alimentés par des énergies renouvelables.  

**Conclusion** : L'application est performante mais **très énergivore pendant le traitement vidéo**. Comparée à des logiciels populaires comme Photoshop ou Discord, on voit clairement que **l’usage intensif est la vraie source de consommation**, et que des optimisations sont possibles pour réduire l’impact sans sacrifier la performance.


