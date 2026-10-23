# Token-scout

## prédiction de la valuer du token en fonction de la langue 

Le fichier `cg_fr.txt` devrait contenir plus de tokens que le fichier `cg_en.txt`  (environ 20% de tokens en plus) parceque le français est une langue plus riche que l'anglais. Et en plus de celà, les modèles de language ont été entrainés sur plus de données en anglais qu'en français.

## Arborescence du projet

```text
Token-scout/
├── data/
│   ├── cg_en.txt
│   ├── cg_fr.txt
│   └── code.py
├── src/
│   └── scouter.py
├── tests/
│   └── test_scouter.py
├── pytest.ini
├── README.md
└── requiremets.txt
```
## Problème : pourquoi compter le nombre de tokens ?

Compter le nombre de tokens est important pour plusieurs raisons : 
- Il permet de comprendre la complexité d'un texte et de déterminer combien de ressources sont nécessaires pour le traiter.
- D'un point de vue économique, le coût de traitement d'un texte est souvent proportionnel au nombre de tokens qu'il contient. Ainsi, en connaissant le nombre de tokens, on peut estimer le coût associé à l'utilisation d'un modèle de langage pour traiter ce texte.
- Il ya aussi un enjeu de limite de contexte car les modèles de langage ont une limite sur le nombre de tokens qu'ils peuvent traiter à la fois. Si un texte dépasse cette limite, il peut être nécessaire de le diviser en plusieurs parties, ce qui peut compliquer le traitement et potentiellement affecter la qualité des résultats.

## Prediction vs resultats

Nous avons eu à prédire le nombre de tokens pour les fichiers `cg_en.txt` et `cg_fr.txt` en utilisant un modèle de langage (ici, GPT-4o). finalement, on a ~ 26% de tokens en plus pour le fichier `cg_fr.txt` par rapport au fichier `cg_en.txt`. Ce qui est cohérent avec nos attentes. 

## Conclusion dans le monde de l'assuarance

finalement, le nombre de tokens est un indicateur clé pour évaluer la complexité d'un texte et le coût associé à son traitement par un modèle de langage. Dans le contexte de l'assurance, où les documents peuvent être longs et complexes, comprendre le nombre de tokens peut aider à optimiser les processus de traitement automatique des documents, à estimer les coûts et à garantir que les modèles de langage utilisés sont adaptés à la taille et à la complexité des textes traités.
