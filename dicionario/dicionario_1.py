import itertools

def gerador_inteligente(nomes, datas, simbolos, arquivo_saida):
    total_gerado = 0
    with open(arquivo_saida, 'w') as f:
        # Criamos uma lista de todas as partes
        # Você pode adicionar ou remover listas aqui
        componentes = [nomes, datas, simbolos]
        
        # O 'permutations' decide a ordem dos blocos (ex: Nome+Data ou Data+Nome)
        for ordem in itertools.permutations(componentes):
            # O 'product' combina os itens dentro de cada bloco na ordem escolhida
            for combinacao in itertools.product(*ordem):
                senha = "".join(combinacao)
                f.write(senha + "\n")
                total_gerado += 1
                
    print(f"Pronto! {total_gerado} combinações salvas em: {arquivo_saida}")

# --- DEFINA SUAS PALAVRAS-CHAVE AQUI ---
lista_nomes = ["Admin", "Wifi", "Casa", "Net"] # Podem ser nomes próprios também
lista_datas = ["2023", "2024", "123"]         # Anos ou sequências comuns
lista_simbolos = ["@", "!", "#", "$"]         # Símbolos que as pessoas mais usam

# Nome do arquivo que vamos baixar depois para o Kali
saida = "wordlist_personalizada.txt"

# Executar
gerador_inteligente(lista_nomes, lista_datas, lista_simbolos, saida)