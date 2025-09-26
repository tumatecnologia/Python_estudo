# escreva um programa que leia a data de nascimento do usuario e mostre a quantidade de dias, horas, minutos e segundos de vida dele


class converter:
   def __init__(self, ano):
        self.ano = ano
        self.atual = None
        self.dias = None
        self. horas = None
        self.minutos = None
        self.segundos = None
        
        
   def idade(self):
        self.atual = 2025 - self.ano
        print(f'Você tem {self.atual} anos de vida')
         
   def dia(self): 
       self.dias = self.atual * 365
       print(f'Você tem {self.dias} dias de vida')
       
   def hora(self):
       self.horas = self.dias * 24
       print(f'Você tem {self.horas} horas de vida')  
       
   def minuto(self):
       self.minutos = self.horas * 60
       print(f'Você tem {self.minutos} minutos de vida')
       
   def segundo(self):
       self.segundos = self.minutos * 60
       print(f'Você tem o total de {self.segundos} de vida')    
        
        
ano= int(input("Digite o ano do seu nascimento:"))
conversao = converter(ano)     
conversao.idade() 
conversao.dia()
conversao.hora()
conversao.minuto()
conversao.segundo()
