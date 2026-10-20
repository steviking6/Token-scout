import tiktoken 
from pathlib import Path


CHEMIN = Path(__file__).parent.parent 

def lire_texte(chemin : Path) -> str:
    with open(chemin, "r", encoding="utf-8") as file:
        file.read()

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
    

if __name__ == "__main__":
    '''encoding_name = str(input("choisissez le type d'encodage"))'''
    
    enc = tiktoken.get_encoding(encoding_name="o200k_base")