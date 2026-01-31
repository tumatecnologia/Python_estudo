import itertools

def transformar_palavras(lista):
    """Gera variações de maiúsculas/minúsculas para cada palavra."""
    variacoes = set()
    for p in lista:
        variacoes.add(p.lower())      # casa
        variacoes.add(p.upper())      # CASA
        variacoes.add(p.capitalize()) # Casa
    return list(variacoes)

def gerador_avancado(nomes, datas, simbolos, arquivo_saida):
    total_gerado = 0
    
    # Aplicando as variações de letras nos nomes
    nomes_expandidos = transformar_palavras(nomes)
    
    with open(arquivo_saida, 'w') as f:
        # Definimos os blocos que serão combinados
        componentes = [nomes_expandidos, datas, simbolos]
        
        # itertools.permutations define a ordem dos blocos (ex: Nome+Data+Simbolo)
        for ordem in itertools.permutations(componentes):
            # itertools.product faz a mistura dos itens dentro dos blocos
            for combinacao in itertools.product(*ordem):
                senha = "".join(combinacao)
                f.write(senha + "\n")
                total_gerado += 1
                
    print(f"--- Concluído ---")
    print(f"Total de combinações geradas: {total_gerado}")
    print(f"Arquivo salvo como: {arquivo_saida}")

# --- CONFIGURAÇÃO DAS SUAS PALAVRAS-CHAVE ---
lista_nomes = ["wifi", "conexao", "familia"] 
lista_datas = ["2023", "2024", "2025", "1020"]
lista_simbolos = ["@", "!", "#", "$", "*"]

# Execução
gerador_avancado(lista_nomes, lista_datas, lista_simbolos, "wordlist_v2.txt")