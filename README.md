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
