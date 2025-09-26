# faça um programa que solicite o preço de uma mercadoria e o percentual de desconto
# exiba o valor do desconto e o preço a pagar

class produto:
    def __init__(self,preco,desconto):
        self.preco = preco
        self.desconto = desconto
        
    def descontar(self):
        percentual = desconto / 100
        a_descontar = self. preco * percentual
        coloca = a_descontar * 100
        resta = self.preco - a_descontar 
        print(f'Valor do desconto => R${coloca:.2f}')
        print(f'O novo valor é => R${resta:.3f}')
        print("==================================")
        
        
        
        
        
        
        
        
        
        
        
preco = float(input("Digite o preço R$:"))
desconto = float(input("Digite o percentual de desconto(%):"))
valor = produto(preco,desconto)
valor.descontar()