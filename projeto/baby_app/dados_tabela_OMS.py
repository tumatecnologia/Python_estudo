# oms.py
class TabelaOMS:
    def __init__(self):
        # Dados de exemplo baseados nas tabelas da OMS
        self.tabela_imc = {
            # Idade: (limite_baixo_peso, limite_normal, limite_sobrepeso)
            2: (14.0, 18.0, 19.0),
            3: (14.5, 17.5, 18.5),
            4: (15.0, 17.0, 18.0),
            5: (15.5, 19.0, 20.0),
            
        }
    
    def get_classificacao(self, idade, imc, sexo='M'):
        # Arredonda a idade para baixo
        idade_chave = min([k for k in self.tabela_imc.keys() if k <= idade], key=lambda x: abs(x - idade))
        
        baixo, normal, sobrepeso = self.tabela_imc[idade_chave]
        
        if imc < baixo:
            return "Baixo peso"
        elif imc < normal:
            return "Peso adequado"
        elif imc < sobrepeso:
            return "Sobrepeso"
        else:
            return "Obesidade"