'''CRIANDO A CLASSE CRIANCA'''
from datetime import datetime, date

class Crianca:
    '''ABAIXO TENHO O METODO CONSTRUTOR'''
    def __init__(self, nome, data_nasc, sex, mae="", pai=""):
       self.nome = nome
       self.nomePai = pai
       self.nomeMae = mae
       self.data_nascimento = data_nasc
       self.sexo = sex
       self.foto_entregue = False    
    '''==========================================='''
    '''ABAIXO TENHO OS ATRIBUTOS DA CLASSE CRIANCA'''    
    def set_nomePai(self, nomePai):
        self.nomePai = nomePai  
         
    def set_nomeMae(self, nomeMae):
        self.nomeMae = nomeMae
    
    def set_foto_entregue(self, status):
        self.foto_entregue = status  
        
    def set_Sexo(self):
        self.sexo = sex      
    
    def get_nome(self):
       return self.nome
   
    def get_Status_foto(self):
        if self.foto_entregue:
            return "Foto Entregue"
        else:
            return "Foto Pendente"
        
    '''======================================================='''
    '''ABAIXO TENHO O MÉTODO CALCULAR IDADE'''
   
    def CalcularIdade(self):
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year
        
        # Ajuste para aniversário que ainda não aconteceu este ano
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1
            
        return idade
    '''=========================================================='''
    '''ABAIXO TENHO A ENTRADA DE crianca PELO TECLADO'''

# CORREÇÃO NA ENTRADA DE crianca
nome = input("Digite o nome da criança: ").upper()
ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))
sex = input("Digite o sexo da criança: ").upper()
mae = input("Nome da mãe:").upper()
pai = input("nome do pai:").upper()
foto = input("A foto foi entregue?").upper()

'''======================================================'''
'''ABAIXO TENHO A CRIAÇÃO DO OBJETO crianca'''

# Criar objeto date corretamente
data_nasc = date(ano, mes, dia)
crianca = Crianca(nome, data_nasc, sex, mae, pai)

'''========================================================'''
'''ABAIXO ESTOU VERIFICANDO O STATUS DA ENTREGA DA FOTO'''
if foto == "S":
    crianca.set_foto_entregue(True)
else:
    crianca.set_foto_entregue(False)

'''=========================================================='''
'''ABAIXO ESTOU IMPRIMINDO OS crianca NA TELA'''
print("========RESULTADO==============")
print("===============================")
print(f"Nome da criança: {crianca.nome}")
print(f"Data de nascimento: {crianca.data_nascimento}")
print(f"Nome do pai: {crianca.nomePai}")
print(f"Nome da mãe: {crianca.nomeMae}")
print(f"Idade calculada: {crianca.CalcularIdade()} anos")
print(f"Status da foto: {crianca.get_Status_foto()}")
print("===============================")



   