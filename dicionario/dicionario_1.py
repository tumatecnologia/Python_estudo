import itertools
from datetime import datetime

def transformar_palavras(lista):
    """Gera variações de maiúsculas/minúsculas."""
    variacoes = set()
    for p in lista:
        p = p.strip()
        if p:
            variacoes.add(p.lower())
            variacoes.add(p.upper())
            variacoes.add(p.capitalize())
    return list(variacoes)

def gerar_anos():
    return [str(ano) for ano in range(1900, datetime.now().year + 1)]

def gerador_repositorio(alvos, sufixos, simbolos, arquivo_saida):
    total_filtrado = 0
    
    # Expandir todas as palavras-base (Nomes, Cidades, Pets)
    bases_expandidas = transformar_palavras(alvos)
    anos = gerar_anos()
    sequencias = ["123", "1234", "123456", "00", "112233"]
    
    # Unificar o que pode vir depois da palavra-base
    complementos = list(set(anos + sequencias + sufixos))
    
    print(f"[*] Gerando dicionário inteligente em: {arquivo_saida}...")
    
    with open(arquivo_saida, 'w') as f:
        for base in bases_expandidas:
            for comp in complementos:
                # Criar variações de estrutura
                templates = [
                    f"{base}{comp}",       # Ex: Mara1995
                    f"{base}@{comp}",      # Ex: Mara@1995
                    f"{base}{comp}!",      # Ex: Mara1995!
                    f"{comp}{base}",       # Ex: 1995Mara
                    f"{base}{comp}{base}"  # Ex: 123Mara123
                ]
                
                for senha in templates:
                    # Filtro obrigatório para WPA2 (8 a 63 caracteres)
                    if 8 <= len(senha) <= 63:
                        f.write(senha + "\n")
                        total_filtrado += 1
                        
    print(f"[+] Sucesso! {total_filtrado} senhas válidas geradas.")

# --- EDITE ESTAS LISTAS NO SEU VS CODE ---
palavras_alvo = ["familia", "beto", "rex", "sp"] # Nomes, pets, cidades
sufixos_extras = ["2024", "777", "1010"]          # Números da sorte, etc
meus_simbolos = ["@", "!", "#", "$"]

# Executar
gerador_repositorio(palavras_alvo, sufixos_extras, meus_simbolos, "wordlist_final.txt")