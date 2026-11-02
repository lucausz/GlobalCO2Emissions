import os
import pandas as pd

# Chemins des fichiers (entrée et sortie)
DATA_DIR = "data/processed"
INPUT_FILE = "data/raw/dataset.csv"
OUTPUT_FILE = "data/processed/dataset_cleaned.csv"

def preprocess_data():
    os.makedirs(DATA_DIR, exist_ok=True)
    print(f"Chargement des données depuis {INPUT_FILE}...")
    
    # 1. Chargement (Note : le dataset utilise des tabulations comme séparateur)
    try:
        df = pd.read_csv(INPUT_FILE, sep='\t') 
    except FileNotFoundError:
        print(f"Erreur : Le fichier {INPUT_FILE} est introuvable. Lancez d'abord le téléchargement.")
        return

    # 2. Renommer et formater les colonnes
    print("Formatage des colonnes...")
    # Simplifier le nom de la colonne ISO
    df = df.rename(columns={"ISO 3166-1 alpha-3": "ISO"})
    
    # Bonne pratique : tout en minuscules et remplacer les espaces par des underscores '_'
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # 3. Gestion des valeurs manquantes
    print("Traitement des valeurs manquantes...")
    # Supprimer les lignes où le 'total' est manquant (donnée inexploitable)
    df = df.dropna(subset=['total'])
    
    # Remplacer les valeurs manquantes (NaN) des sources d'énergie par 0
    sources = ['coal', 'oil', 'gas', 'cement', 'flaring', 'other']
    df[sources] = df[sources].fillna(0)

    # 4. Filtrer les lignes
    print("Filtrage des données...")
    # Retirer les régions ou continents (qui n'ont pas de code ISO de pays)
    df = df.dropna(subset=['iso'])
    
    # Filtrer pour ne garder que l'époque moderne (ex: depuis 1950) pour une analyse plus pertinente
    df = df[df['year'] >= 1950]

    # 5. Conversion de types simples
    print("Conversion des types...")
    # S'assurer que les pays et codes ISO sont des chaînes de caractères (string)
    df['country'] = df['country'].astype('string')
    df['iso'] = df['iso'].astype('string')
    
    # S'assurer que l'année est un nombre entier
    df['year'] = df['year'].astype(int)

    # 6. Suppression des valeurs aberrantes évidentes
    print("Vérification des valeurs aberrantes...")
    # Les émissions totales ne peuvent pas être négatives physiquement
    df = df[df['total'] >= 0]
    # On pourrait aussi supprimer les lignes où 'per_capita' est aberrant

    # Sauvegarde des données propres
    os.makedirs("data", exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    
    print(f"\nSuccès ! Données prétraitées sauvegardées dans : {OUTPUT_FILE}")
    print(f"Dimensions du jeu de données final : {df.shape[0]} lignes, {df.shape[1]} colonnes")

if __name__ == "__main__":
    preprocess_data()