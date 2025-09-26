# escreva um programa que leia um valor em metros e o exiba convertido em milímetros

class Converter:
    def __init__(self,metros):
        self.metros = metros
        
    def milimetros(self):
        resultado = self. metros * 1000
        print(f"{self.metros} metros é igual a {resultado} milímetros")    
        


metros = float(input('Digite um valor em metros: '))
conversor = Converter(metros)
conversor.milimetros()