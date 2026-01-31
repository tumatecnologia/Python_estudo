import itertools
from datetime import datetime

def transformar_palavras(lista):
    """Gera variações de maiúsculas, minúsculas e Leet Speak."""
    variacoes = set()
    
    # Tabela de substituição Leet Speak simples
    leet_map = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}

    for p in lista:
        p = p.strip().lower()
        if not p: continue
        
        # Básicas
        variacoes.add(p)
        variacoes.add(p.upper())
        variacoes.add(p.capitalize())
        
        # Leet Speak (Substituição total)
        p_leet = "".join(leet_map.get(c, c) for c in p)
        variacoes.add(p_leet)
        variacoes.add(p_leet.upper())
        variacoes.add(p_leet.capitalize())
        
    return list(variacoes)

def gerar_anos():
    """Gera anos completos (1980) e curtos (80)."""
    anos = []
    ano_atual = datetime.now().year
    for ano in range(1950, ano_atual + 1):
        ano_str = str(ano)
        anos.append(ano_str)          # 1982
        anos.append(ano_str[-2:])     # 82
    return list(set(anos))

def gerador_repositorio(alvos, sufixos, simbolos, arquivo_saida):
    total_filtrado = 0
    
    bases_expandidas = transformar_palavras(alvos)
    anos = gerar_anos()
    sequencias = ["123", "1234", "123456", "00", "112233", "777"]
    
    # Unificar complementos (anos, sequências e sufixos extras)
    complementos = list(set(anos + sequencias + sufixos))
    
    print(f"[*] Gerando dicionário inteligente em: {arquivo_saida}...")
    
    # Usamos um set para evitar duplicatas antes de escrever no arquivo
    senhas_unicas = set()
    
    for base in bases_expandidas:
        # Adiciona a base pura se tiver 8+ chars
        if 8 <= len(base) <= 63:
            senhas_unicas.add(base)
            
        for comp in complementos:
            for simb in simbolos:
                # Templates de estrutura solicitados
                templates = [
                    f"{base}{comp}",          # familia82
                    f"{base}{simb}{comp}",     # familia@82
                    f"{base}{comp}{simb}",     # familia82!
                    f"{comp}{base}",          # 82familia
                    f"{base}{comp}{base}",     # 123familia123
                    f"{base}{simb}",          # familia@
                    f"{simb}{base}{comp}"      # @familia123
                ]
                
                for senha in templates:
                    if 8 <= len(senha) <= 63:
                        senhas_unicas.add(senha)

    with open(arquivo_saida, 'w') as f:
        for s in sorted(senhas_unicas):
            f.write(s + "\n")
            total_filtrado += 1
                        
    print(f"[+] Sucesso! {total_filtrado} senhas únicas geradas.")

# --- CONFIGURAÇÃO ---
# Adicionei 'filhos' e 'mesh' por causa do nome da rede que você capturou
palavras_alvo = ["familia", "beto", "rex", "sp", "filhos", "mesh"] 
sufixos_extras = ["2024", "1010", "2025", "2026"]
meus_simbolos = ["@", "!", "#", "$", "_", "."]

# Executar
gerador_repositorio(palavras_alvo, sufixos_extras, meus_simbolos, "wordlist_final_v2.txt")