# test_compteur.py
import tiktoken
from scouter import estimer_cout, compter_tokens, visualiser_tokens, pourcentage_contexte

enc = tiktoken.get_encoding("o200k_base")

def test_estimer_cout_zero():
    assert estimer_cout(0) == 0

def test_estimer_cout_un_million():
    assert estimer_cout(1000000) == 2.50

def test_compter_tokens_vide():
    assert compter_tokens("", enc) == 0

def test_visualiser_tokens():
    texte = "Bonjour les mecs, Gojo > Sukuna ?"
    result = visualiser_tokens(texte, enc)
    assert result.replace("|", "") == texte 
    
def test_pourcentage_fenetre_contexte():
    assert pourcentage_contexte(128_000) == 100
    
    
   
   
