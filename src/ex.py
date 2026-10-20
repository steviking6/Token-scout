import tiktoken 

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(string)
    liste_tokens = []
    for i in range(0, len(tokens)):
        token = encoding.decode([tokens[i]])
        liste_tokens.append(token)
    texte = "|".join(liste_tokens)
    return texte

num_tok = num_tokens_from_string("Bonjour, moi c'est Stevi.", "o200k_base")
print(f"nombre de tokens : {num_tok}")

#decodage = encoding.decode([83, 8251, 2488, 382, 2212, 0])

def decode_txt(etxte:str, enc)->str:
    ...