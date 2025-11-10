from crianca import crianca  # Importa o objeto crianca já criado
from datetime import date

class Medicao:
    def __init__(self, peso, altura, crianca_obj):
        self.peso = peso
        self.altura = altura
        self.crianca = crianca_obj  # Recebe o objeto crianca
        self.imc = self._calcular_imc()
        self.data = date.today()
    
    def _calcular_imc(self):
        return self.peso / (self.altura * self.altura)
    
    def set_Peso(self, peso):
        self.peso = peso
        self.imc = self._calcular_imc()
    
    def set_Altura(self, altura):
        self.altura = altura
        self.imc = self._calcular_imc()
    
    def get_IMC(self):
        return self.imc
    
    def get_Classificacao(self):
        imc = self.imc
        idade = self.crianca.CalcularIdade()  # Chama o método da criança
        
        if idade < 2:
            if imc < 14:
                return "Baixo peso"
            elif imc < 18:
                return "Peso adequado"
            else:
                return "Sobrepeso"
        
        elif idade < 5:
            if imc < 15:
                return "Baixo peso"
            elif imc < 17:
                return "Peso adequado"
            elif imc < 19:
                return "Sobrepeso"
            else:
                return "Obesidade"
        
        elif idade < 10:
            if imc < 16:
                return "Baixo peso"
            elif imc < 20:
                return "Peso adequado"
            elif imc < 23:
                return "Sobrepeso"
            else:
                return "Obesidade"
        
        else:  # 10-19 anos
            if imc < 18.5:
                return "Baixo peso"
            elif imc < 25:
                return "Peso adequado"
            elif imc < 30:
                return "Sobrepeso"
            else:
                return "Obesidade"
            
    def exibir_dados_medicao(self):
        # Acessando os dados da criança através da medição
        print("==================================================")
        print("\n=== DADOS DA MEDIÇÃO ===")
        print(f"Criança: {medicao.crianca.nome}")
        print(f'Nome da Mãe: {medicao.crianca.nomeMae}')
        print(f'Nome do Pai: {medicao.crianca.nomePai}')
        print(f'Data de Nascimento: {medicao.crianca.data_nascimento}')
        print(f"Sexo: {medicao.crianca.sexo}")
        print(f"Idade: {medicao.crianca.CalcularIdade()} anos")
        print(f"IMC: {medicao.get_IMC():.2f}")
        print(f"Classificação:\033[91m {medicao.get_Classificacao()}\033[0m")
        print("==================================================")
    

# CRIANDO A MEDIÇÃO USANDO A CRIANCA JÁ EXISTENTE

peso = float(input("Digite o peso:"))
altura = float(input('Digite a Altura:'))
medicao = Medicao(peso,altura, crianca)  # Passa o objeto crianca
medicao.exibir_dados_medicao()

