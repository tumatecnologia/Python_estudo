import itertools
from datetime import datetime

def transformar_palavras(lista):
    """Gera variações de maiúsculas, minúsculas e Leet Speak avançado."""
    variacoes = set()
    leet_map = {
        'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7', 'b': '8'
    }

    for p in lista:
        p = p.strip().lower()
        if not p: continue
        
        # Formatações padrão
        variacoes.add(p)
        variacoes.add(p.upper())
        variacoes.add(p.capitalize())
        
        # Leet Speak total
        p_leet = "".join(leet_map.get(c, c) for c in p)
        variacoes.add(p_leet)
        variacoes.add(p_leet.upper())
        variacoes.add(p_leet.capitalize())
        
    return list(variacoes)

def gerar_anos():
    """Anos completos e curtos."""
    anos = []
    ano_atual = datetime.now().year
    for ano in range(1970, ano_atual + 2):
        s = str(ano)
        anos.extend([s, s[-2:]])
    return list(set(anos))

def gerador_v3(alvos, sufixos, simbolos, arquivo_saida):
    total = 0
    bases = transformar_palavras(alvos)
    anos = gerar_anos()
    sequencias = ["123", "1234", "123456", "102030", "00", "11"]
    
    complementos = list(set(anos + sequencias + sufixos))
    senhas_unicas = set()
    
    print(f"[*] Criando super dicionário...")

    for base in bases:
        # Palavra pura (se tiver o tamanho mínimo do WPA2)
        if 8 <= len(base) <= 63: senhas_unicas.add(base)
        
        for comp in complementos:
            # Estruturas mais comuns em redes brasileiras
            templates = [
                f"{base}{comp}",       # familia2024
                f"{base}@{comp}",      # familia@24
                f"{base}{comp}!",      # familia24!
                f"{comp}{base}",       # 2024familia
                f"{base}_{comp}",      # familia_2024
                f"{base}.{comp}",      # familia.24
                f"{base}{comp}{base}"  # 123familia123
            ]
            
            for s in templates:
                if 8 <= len(s) <= 63:
                    senhas_unicas.add(s)

    with open(arquivo_saida, 'w') as f:
        # Ordenar ajuda o aircrack a ser mais eficiente no cache
        for s in sorted(senhas_unicas):
            f.write(s + "\n")
            total += 1
                        
    print(f"[+] Finalizado! {total} senhas geradas em {arquivo_saida}")

# --- ADICIONE MAIS PALAVRAS DO DICIONÁRIO AQUI ---
palavras_base = [
    "familia", "filhos", "mesh", "internet", "casa", "senha", 
    "wifi", "deus", "amor", "brasil", "conexao", "rede",
    "beto", "rex", "marcos", "lucas", "maria", "ana" # Adicione nomes prováveis
]

sufixos = ["777", "1010", "2024", "2025"]
simbolos = ["@", "!", "#", "$"]

gerador_v3(palavras_base, sufixos, simbolos, "wordlist_v3_final.txt")