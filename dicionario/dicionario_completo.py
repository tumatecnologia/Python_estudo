import itertools
from datetime import datetime

def transformar_palavras(lista):
    variacoes = set()
    leet_map = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    for p in lista:
        p = p.strip().lower()
        if not p: continue
        variacoes.update([p, p.upper(), p.capitalize()])
        p_leet = "".join(leet_map.get(c, c) for c in p)
        variacoes.update([p_leet, p_leet.upper(), p_leet.capitalize()])
    return list(variacoes)

def gerador_bruto_v5(alvos, arquivo_saida):
    print(f"[*] Iniciando geração massiva. Isso pode levar um tempo...")
    
    # Usamos o arquivo direto para não estourar a memória RAM
    with open(arquivo_saida, 'w') as f:
        
        # 1. TODAS AS COMBINAÇÕES NUMÉRICAS DE 8 DÍGITOS (00000000 a 99999999)
        # Isso sozinho gera 100 milhões de senhas. É o "padrão ouro" para redes brasileiras.
        print("[>] Gerando 100 milhões de combinações numéricas (8 dígitos)...")
        for i in range(100000000):
            f.write(f"{i:08d}\n")
        
        # 2. VARIAÇÕES DAS PALAVRAS-ALVO COM SUFIXOS
        print("[>] Gerando variações das palavras-base...")
        bases = transformar_palavras(alvos)
        anos = [str(ano) for ano in range(1950, 2027)] + [str(ano)[-2:] for ano in range(1950, 2027)]
        simbolos = ["", "@", "!", "#", "$", "*", "_", "."]
        sequencias = ["123", "1234", "123456", "102030"]

        for base in bases:
            for s in simbolos:
                for comp in (anos + sequencias):
                    senha1 = f"{base}{s}{comp}"
                    senha2 = f"{comp}{s}{base}"
                    if 8 <= len(senha1) <= 63: f.write(senha1 + "\n")
                    if 8 <= len(senha2) <= 63: f.write(senha2 + "\n")

        # 3. O "ABECEDÁRIO" (Combinações de 3 letras + números)
        # Tentar todas as letras do alfabeto de 8 chars é impossível, 
        # então focamos em prefixos de letras com sufixos numéricos.
        print("[>] Gerando combinações de iniciais + números...")
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        # Gera combinações como abc12345, aaa12345, etc.
        for combo in itertools.product(alfabeto, repeat=3):
            prefixo = "".join(combo)
            for suf in ["123", "1234", "2024", "2025"]:
                f.write(f"{prefixo}{suf}\n")

    print(f"[+] Sucesso! O arquivo {arquivo_saida} está pronto para o combate.")

# --- CONFIGURAÇÃO ---
palavras_base = ["familia", "filhos", "mesh", "beto", "rex", "casa", "wifi"]
gerador_bruto_v5(palavras_base, "wordlist_mega_brute.txt")