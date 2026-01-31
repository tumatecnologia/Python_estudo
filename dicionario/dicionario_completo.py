import itertools
from datetime import datetime

def transformar_palavras(lista):
    """Gera variações de maiúsculas, minúsculas e Leet Speak avançado."""
    variacoes = set()
    leet_map = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}

    for p in lista:
        p = p.strip().lower()
        if not p: continue
        
        variacoes.add(p)
        variacoes.add(p.upper())
        variacoes.add(p.capitalize())
        
        # Leet Speak
        p_leet = "".join(leet_map.get(c, c) for c in p)
        variacoes.add(p_leet)
        variacoes.add(p_leet.capitalize())
        
    return list(variacoes)

def gerar_anos():
    anos = []
    ano_atual = datetime.now().year
    for ano in range(1960, ano_atual + 2):
        s = str(ano)
        anos.extend([s, s[-2:]]) # 1995 e 95
    return list(set(anos))

def gerador_v4(alvos, sufixos, simbolos, arquivo_saida):
    total = 0
    senhas_unicas = set()
    
    bases = transformar_palavras(alvos)
    anos = gerar_anos()
    
    # 1. GERAR SEQUÊNCIAS DE 8 DÍGITOS (Muito comum: datas ou números seguidos)
    # Nota: Geramos apenas as mais prováveis para não inflar o arquivo demais
    sequencias_8 = [
        "12345678", "87654321", "00000000", "11111111", 
        "10203040", "12121212", "12312312"
    ]
    
    # 2. COMBINAÇÕES DE 3 LETRAS (O "abecedário" como prefixo/sufixo)
    # Ex: abc, aaa, wifi, net...
    letras_comuns = ["abc", "wifi", "net", "web", "sky"]
    
    complementos = list(set(anos + sufixos + sequencias_8 + letras_comuns))
    
    print(f"[*] Gerando dicionário v4 (Inteligente + Numérico)...")

    for base in bases:
        # Palavra pura
        if 8 <= len(base) <= 63: senhas_unicas.add(base)
        
        for comp in complementos:
            for simb in simbolos:
                templates = [
                    f"{base}{comp}",       # familia2024
                    f"{base}{simb}{comp}",    # familia@2024
                    f"{comp}{base}",       # 2024familia
                    f"{base}{comp}{simb}",    # familia2024!
                    f"{base}_{comp}",      # familia_2024
                    f"{base}{simb}"        # familia@
                ]
                for s in templates:
                    if 8 <= len(s) <= 63:
                        senhas_unicas.add(s)

    # 3. DATAS DDMMAAAA (As mais comuns dos últimos 40 anos)
    for ano in range(1970, 2025):
        senhas_unicas.add(f"0101{ano}") # Exemplo de feriado/data padrão

    with open(arquivo_saida, 'w') as f:
        for s in sorted(senhas_unicas):
            f.write(s + "\n")
            total += 1
                        
    print(f"[+] Finalizado! {total} senhas geradas em {arquivo_saida}")

# --- LISTA AMPLIADA ---
palavras_base = [
    "familia", "filhos", "mesh", "beto", "rex", "casa", 
    "deus", "amor", "senha", "admin", "conect", "wifi"
]
sufixos = ["123", "777", "1010", "2024", "2025", "2026"]
simbolos = ["@", "!", "#", "$", "*"]

gerador_v4(palavras_base, sufixos, simbolos, "wordlist_completo.txt")