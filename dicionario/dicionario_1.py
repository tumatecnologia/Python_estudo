import itertools

def transformar_palavras(lista):
    """Gera variações de maiúsculas/minúsculas para cada palavra."""
    variacoes = set()
    for p in lista:
        if p.isalpha(): # Só transforma se for texto
            variacoes.add(p.lower())
            variacoes.add(p.upper())
            variacoes.add(p.capitalize())
        else:
            variacoes.add(p)
    return list(variacoes)

def gerar_sequencias_numericas():
    """Gera sequências numéricas que as pessoas mais usam."""
    return ["123", "1234", "123456", "00", "12345678", "102030", "112233"]

def gerador_mestre(nomes, datas, simbolos, arquivo_saida):
    total_gerado = 0
    
    # 1. Expandir nomes (Maiúsculas/Minúsculas)
    nomes_expandidos = transformar_palavras(nomes)
    
    # 2. Obter sequências numéricas automáticas
    sequencias_num = gerar_sequencias_numericas()
    
    # 3. Criar sequências numéricas COM símbolos (ex: 123@, 123456!)
    num_com_simbolos = []
    for n in sequencias_num:
        for s in simbolos:
            num_com_simbolos.append(f"{n}{s}")
    
    # Unificamos todas as opções de "finalização" ou "complemento"
    complementos = list(set(datas + sequencias_num + num_com_simbolos))
    
    with open(arquivo_saida, 'w') as f:
        # Focaremos em duas estruturas principais para não criar um arquivo infinito:
        # Estrutura A: Nome + Complemento (ex: Casa123@)
        # Estrutura B: Complemento + Nome (ex: 123@Casa)
        
        for n in nomes_expandidos:
            for c in complementos:
                # Escreve Nome + Complemento
                f.write(f"{n}{c}\n")
                # Escreve Complemento + Nome
                f.write(f"{c}{n}\n")
                total_gerado += 2
                
                # Opcional: Adicionar apenas o símbolo no meio (ex: Casa@123)
                for s in simbolos:
                    f.write(f"{n}{s}{c}\n")
                    total_gerado += 1

    print(f"--- Dicionário Mestre Gerado ---")
    print(f"Total de combinações: {total_gerado}")
    print(f"Arquivo: {arquivo_saida}")

# --- CONFIGURAÇÃO ---
meus_nomes = ["wifi", "net", "admin", "casa"]
minhas_datas = ["2023", "2024", "2025"]
meus_simbolos = ["@", "!", "#", "$"]

# Execução
gerador_mestre(meus_nomes, minhas_datas, meus_simbolos, "dicionario_kali.txt")