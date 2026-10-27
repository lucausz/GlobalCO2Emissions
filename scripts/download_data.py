import os
import requests

# L'URL du fichier restreint sur Borealis
FILE_URL = "https://demo.borealisdata.ca/api/access/datafile/73270"
DATA_DIR = "data"
OUTPUT_FILE = os.path.join(DATA_DIR, "dataset.csv") 

def download_data():    

    os.makedirs(DATA_DIR, exist_ok=True)
    print("Connexion à Borealis...")
    
    try:
        response = requests.get(FILE_URL, stream=True)
        response.raise_for_status() 

        print("Téléchargement en cours...")
        
        with open(OUTPUT_FILE, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    
        print(f"Succès ! Données enregistrées dans : {OUTPUT_FILE}")
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            print("Erreur 403 : Accès refusé.")
        else:
            print(f"Erreur HTTP : {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau lors du téléchargement : {e}")

if __name__ == "__main__":
    download_data()