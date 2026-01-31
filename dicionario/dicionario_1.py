import itertools
from datetime import datetime

def transformar_palavras(lista):
    variacoes = set()
    for p in lista:
        variacoes.add(p.lower())
        variacoes.add(p.upper())
        variacoes.add(p.capitalize())
    return list(variacoes)

def gerar_todos_os_anos():
    ano_atual = datetime.now().year
    return [str(ano) for ano in range(1900, ano_atual + 1)]

def gerador_v4_filtrado(nomes, simbolos, arquivo_saida):
    total_bruto = 0
    total_filtrado = 0
    
    nomes_expandidos = transformar_palavras(nomes)
    anos = gerar_todos_os_anos()
    sequencias_comuns = ["123", "1234", "123456", "00", "112233"]
    
    complementos = list(set(anos + sequencias_comuns))
    
    print("Processando e filtrando para WPA2 (min 8 caracteres)...")
    
    with open(arquivo_saida, 'w') as f:
        for n in nomes_expandidos:
            for c in complementos:
                # Criamos as variações possíveis
                possibilidades = [
                    f"{n}{c}",          # Ex: Wifi1990
                    f"{c}{n}",          # Ex: 1990Wifi
                    f"{n}@{c}",         # Ex: Wifi@1990
                    f"{n}!{c}",         # Ex: Wifi!1990
                    f"{n}{c}!",         # Ex: Wifi1990!
                    f"@{n}{c}"          # Ex: @Wifi1990
                ]
                
                for senha in possibilidades:
                    total_bruto += 1
                    # --- O FILTRO MÁGICO ---
                    if 8 <= len(senha) <= 63:
                        f.write(senha + "\n")
                        total_filtrado += 1
                
    print(f"--- Relatório Final ---")
    print(f"Combinações ignoradas (curtas demais): {total_bruto - total_filtrado}")
    print(f"Combinações válidas salvas: {total_filtrado}")
    print(f"Arquivo pronto: {arquivo_saida}")

# --- CONFIGURAÇÃO ---
meus_nomes = ["wifi", "conexao", "casa", "familia"]
meus_simbolos = ["@", "!", "#"]

# Executar
gerador_v4_filtrado(meus_nomes, meus_simbolos, "wordlist_final_wpa2.txt")