import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fichiers d'entrée et dossier de sortie
INPUT_FILE = "data/processed/dataset_cleaned.csv"
RESULTS_DIR = "results"

def analyze_data():
    # Création du dossier pour stocker les résultats et graphiques
    os.makedirs(RESULTS_DIR, exist_ok=True)
    
    print(f"Chargement des données nettoyées depuis {INPUT_FILE}...")
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print("Erreur : Fichier introuvable. Lancez d'abord preprocess_data.py.")
        return
    df_countries = df[df['iso'] != 'WLD'].copy()
    print("\n--- 1. CALCUL DES INDICATEURS ---")
    
    # Indicateur 1 : Statistiques groupées (Émissions mondiales totales par année)
    global_emissions_per_year = df_countries.groupby('year')['total'].sum()
    print(f"-> Indicateur 1 : Les émissions mondiales sont passées de {global_emissions_per_year.iloc[0]:.0f} en {global_emissions_per_year.index[0]} à {global_emissions_per_year.iloc[-1]:.0f} en {global_emissions_per_year.index[-1]}.")
    
    # Indicateur 2 : Moyenne (Les 5 pays les plus émetteurs en 2020)
    df_2020 = df_countries[df_countries['year'] == 2020]
    top_5_2020 = df_2020.nlargest(5, 'total')[['country', 'total']]
    print(f"-> Indicateur 2 : Top 5 des émetteurs en 2020 :\n{top_5_2020.to_string(index=False)}")
    
    # Indicateur 3 : Corrélation (Émissions totales vs par habitant en 2020)
    # On utilise numpy (np.corrcoef) ou pandas (.corr)
    corr_total_per_capita = df_2020['total'].corr(df_2020['per_capita'])
    print(f"-> Indicateur 3 : La corrélation entre les émissions totales et par habitant en 2020 est de {corr_total_per_capita:.2f} (Corrélation faible à modérée).")

    print("\n--- 2. GÉNÉRATION DES VISUALISATIONS ---")

    # Visualisation 1 : Évolution temporelle des sources d'émissions (Graphique en courbes)
    # On groupe par année et on somme les différentes sources
    sources_per_year = df_countries.groupby('year')[['coal', 'oil', 'gas']].sum()
    
    plt.figure(figsize=(10, 6))
    plt.plot(sources_per_year.index, sources_per_year['coal'], label='Charbon (Coal)', color='saddlebrown', linewidth=2)
    plt.plot(sources_per_year.index, sources_per_year['oil'], label='Pétrole (Oil)', color='black', linewidth=2)
    plt.plot(sources_per_year.index, sources_per_year['gas'], label='Gaz (Gas)', color='royalblue', linewidth=2)
    
    plt.title('Évolution des émissions mondiales de CO2 par source (1950 - 2020)')
    plt.xlabel('Année')
    plt.ylabel('Émissions de CO2 (Millions de tonnes)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plot1_path = os.path.join(RESULTS_DIR, "evolution_sources_co2.png")
    plt.savefig(plot1_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"-> Graphique 1 sauvegardé : {plot1_path}")

    # Visualisation 2 : Nuage de points (Dispersion) Total vs Per Capita (2020)
    plt.figure(figsize=(10, 6))
    
    # Pour éviter que les pays immenses (Chine, USA) écrasent le graphique, on utilise une échelle logarithmique pour l'axe X
    plt.scatter(df_2020['total'], df_2020['per_capita'], alpha=0.6, color='crimson', edgecolors='black')
    
    plt.title(f'Émissions de CO2 : Totales vs Par Habitant (2020)\nCorrélation : {corr_total_per_capita:.2f}')
    plt.xlabel('Émissions totales (Échelle logarithmique)')
    plt.ylabel('Émissions par habitant (Tonnes)')
    plt.xscale('log') # Indispensable pour bien voir tous les pays
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plot2_path = os.path.join(RESULTS_DIR, "dispersion_total_vs_habitant.png")
    plt.savefig(plot2_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"-> Graphique 2 sauvegardé : {plot2_path}")

    print("\nAnalyse terminée avec succès !")

if __name__ == "__main__":
    analyze_data()
