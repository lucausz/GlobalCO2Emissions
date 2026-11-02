# The Global Carbon Project's fossil CO2 emissions

## Description

Ce projet est développé dans le cadre du Laboratoire 3. Élaboration d'un projet de science ouverte reproductible. Il vise à analyser les émissions carbones.

Les données utilisées proviennent de "The Global Carbon Project's fossil CO2 emissions dataset" et sont hébergées sur le dépôt Borealis.

## Structure du projet

├── 📂 **data** # Données brutes et nettoyées (ignorées par Git)
├── 📂 **results** # Graphiques générés par l'analyse (ignorées par Git)
├── 📂 **scripts** # scripts pythons
├── .gitignore # Fichiers et dossiers à ne pas versionner
├── CONTRIBUTING.md # Guide de contribution au projet
├── README.md # Documentation principale
├── LICENSE # license
└── requirements.txt # Dépendances python

## Prérequis

Pour exécuter ce projet, vous aurez besoin de :

- **Python 3.8+**

## 🚀 Installation et Configuration

**1. Cloner le dépôt**

**2. Créer et activer l'environnement virtuel**

Sous macOS / Linux :

```Bash
python3 -m venv .venv
source .venv/bin/activate
```

Sous Windows :

```DOS
python -m venv .venv
.venv\Scripts\activate
```

**3. Installer les dépendances**
L'ensemble des bibliothèques nécessaires et leurs versions exactes sont figées pour garantir la reproductibilité.

Dans l'environnement virtuel :

```Bash
pip install -r requirements.txt
```

## ⚙️ Exécution du Pipeline de Données

Les scripts doivent être exécutés dans l'ordre suivant :

**Étape 1 : Téléchargement des données**
Ce script se connecte à l'API Borealis pour télécharger les données brutes. Il est à excecuter en premier

```Bash
python download_data.py
```

Données sauvegardées dans : `data/raw/dataset.csv`

**Étape 2 : Prétraitement**
Ce script nettoie les données brutes (gestion des valeurs manquantes, formatage des colonnes, filtrage des données depuis 1950, suppression des données non attribuées à des pays précis).

```Bash
python preprocess_data.py
```

Données sauvegardées dans : `data/processed/dataset_cleaned.csv`

**Étape 3 : Analyse et Visualisation**
Ce script génère des indicateurs de synthèse (moyennes, corrélations) et produit des graphiques pour répondre aux questions de recherche.

```Bash
python analyze_data.py
```

Résultats sauvegardés dans le dossier `results/`

## 🤝 Contribution

Si vous souhaitez contribuer à ce projet (par exemple, pour ajouter de nouveaux indicateurs ou optimiser le nettoyage), veuillez consulter notre guide de contribution.

Toute contribution doit passer par une Pull Request vers la branche main, qui est protégée.
