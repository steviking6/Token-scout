# test_compteur.py
import tiktoken
from scouter import estimer_cout, compter_tokens

enc = tiktoken.get_encoding("o200k_base")

def test_estimer_cout_zero():
    assert estimer_cout(0) == 0

def test_estimer_cout_un_million():
    assert estimer_cout(1000000) == 2.50

def test_compter_tokens_vide():
    assert compter_tokens("", enc) == 0