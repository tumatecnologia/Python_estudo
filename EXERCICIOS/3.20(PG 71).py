 #CALCULO DE BONUS POR TEMPO DE SERVIÇO#
 
class Funcionario:
     def __init__(self,anos,valor_por_ano):  
         self.anos = anos
         self.valor_por_ano = valor_por_ano
        
     def bonus(anos, valor_por_ano):
        bonus_final = anos * valor_por_ano
        print(f"O valor do bônus é: R$ {bonus_final:.2f}")
 
 
 
 
anos = float(input("Tempo de serviço:"))
valor = float(input("Valor por ano:"))
Funcionario.bonus(anos,valor)