import itertools
from datetime import datetime

def transformar_palavras(lista):
    """Gera variações de maiúsculas/minúsculas para cada palavra."""
    variacoes = set()
    for p in lista:
        if p.isalpha():
            variacoes.add(p.lower())
            variacoes.add(p.upper())
            variacoes.add(p.capitalize())
        else:
            variacoes.add(p)
    return list(variacoes)

def gerar_sequencias_numericas():
    """Gera sequências numéricas comuns."""
    return ["123", "1234", "123456", "00", "112233", "102030"]

def gerar_todos_os_anos():
    """Gera uma lista de anos de 1900 até o ano atual."""
    ano_atual = datetime.now().year
    return [str(ano) for ano in range(1900, ano_atual + 1)]

def gerador_final(nomes, simbolos, arquivo_saida):
    total_gerado = 0
    
    # 1. Preparar os blocos
    nomes_expandidos = transformar_palavras(nomes)
    anos = gerar_todos_os_anos()
    sequencias_num = gerar_sequencias_numericas()
    
    # 2. Criar combinações de Números + Símbolos (ex: 1995@, 123!)
    numeros_totais = anos + sequencias_num
    num_com_simbolos = []
    for n in numeros_totais:
        for s in simbolos:
            num_com_simbolos.append(f"{n}{s}")
    
    # Unificamos tudo que pode vir depois ou antes do nome
    complementos = list(set(numeros_totais + num_com_simbolos))
    
    print(f"Gerando arquivo... Isso pode levar alguns segundos.")
    
    with open(arquivo_saida, 'w') as f:
        for n in nomes_expandidos:
            for c in complementos:
                # Estrutura: NomeAno (ex: Maria1990)
                f.write(f"{n}{c}\n")
                # Estrutura: AnoNome (ex: 1990Maria)
                f.write(f"{c}{n}\n")
                total_gerado += 2
                
                # Estrutura com símbolo no meio (ex: Maria@1990)
                for s in simbolos:
                    f.write(f"{n}{s}{c}\n")
                    total_gerado += 1
                
    print(f"--- Dicionário Completo Gerado ---")
    print(f"Total de combinações: {total_gerado}")
    print(f"Anos incluídos: 1900 até {datetime.now().year}")
    print(f"Arquivo salvo como: {arquivo_saida}")

# --- CONFIGURAÇÃO ---
meus_nomes = ["wifi", "net", "casa"] # Coloque nomes que façam sentido para o alvo
meus_simbolos = ["@", "!", "#", "$"]

# Execução
gerador_final(meus_nomes, meus_simbolos, "wordlist_completa.txt")