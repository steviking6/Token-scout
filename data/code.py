from pathlib import Path
import tiktoken

CHEMIN = Path("data")

def analyser(fichier, enc):
    # encoding="utf-8" = la clé qui évite le bug sur les .py
    texte = fichier.read_text(encoding="utf-8")
    nb_chars = len(texte)
    nb_tokens = len(enc.encode(texte))
    return {
        "chemin": fichier.name,
        "caractères": nb_chars,
        "tokens": nb_tokens,
    }

def main():
    enc = tiktoken.get_encoding("cl100k_base")

    # on ramasse .txt ET .py
    extensions = ("*.txt", "*.py")
    fichiers = [f for ext in extensions for f in CHEMIN.glob(ext)]

    for f in fichiers:
        res = analyser(f, enc)
        print(res)

if __name__ == "__main__":
    main()