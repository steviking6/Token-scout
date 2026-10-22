import tiktoken 
from pathlib import Path
import csv 

# Source : https://developers.openai.com/api/docs/models/gpt-4o
# Vérifié le 22/10/2026
PRIX_PAR_MILLION = 2.50 # en USD, tokens en entrée 
FENETRE_CONTEXTE = 128_000 # Tokens 

CHEMIN = Path(__file__).parent.parent 

def lire_texte(chemin : Path) -> str:
    return chemin.read_text(encoding="utf-8")

def compter_tokens(texte:str, enc) -> int:
    return len(enc.encode(texte))

def visualiser_tokens(texte:str, enc) -> str:
    tokens = enc.encode(texte)
    visuel = []
    for i in range(0, len(tokens)):
        token = enc.decode([tokens[i]])
        visuel.append(token)
    texte = "|".join(visuel)
    return texte 

def estimer_cout(nb_tokens:int)-> float:
    return (nb_tokens * PRIX_PAR_MILLION) / 1000000

def pourcentage_contexte(nb_tokens:int)->float:
    return nb_tokens/FENETRE_CONTEXTE

def analyser(chemin:Path, enc)->str:
    texte = lire_texte(chemin)
    nb_tokens = compter_tokens(texte, enc)
    return {
        "chemin" : chemin.name,
        "caractères" : len(texte),
        "tokens" : nb_tokens, 
        "chars/token" : round(len(texte)/nb_tokens, 2) if nb_tokens else 0,
        "cout" : estimer_cout(nb_tokens),
        "% contexte" : pourcentage_contexte(nb_tokens),
    }
        

def exporter_csv(lignes: list[dict], chemin: Path)->None:
    if not lignes:
        return 
    with open(chemin, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=lignes[0].keys)
        writer.writeheader()
        writer.writerows(lignes)

def main():
    dossier = CHEMIN
    enc = tiktoken.get_encoding("o200k_base")
    
    liste_fichiers = []
    for fichier in dossier.glob("*.txt"):
        liste_fichiers.append(fichier.name)
        
    #analyse de fichiers 
    resultats = []
    for fichier in liste_fichiers:
        resultats.append(analyser(dossier/fichier, enc))
    
    exporter_csv(resultats)
        
    
if __name__ == "__main__":
    '''encoding_name = str(input("choisissez le type d'encodage"))'''
    
    enc = tiktoken.get_encoding(encoding_name="o200k_base")