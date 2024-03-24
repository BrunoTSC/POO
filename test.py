import pandas as pd

tabela = pd.read_excel("DataFramePOO.xlsx")

class dataframe: #É uma classe que possui métodos para extrair os dados do arquivo Excel e realizar a análise inicial.
    def __init__(self, file_path): #O método inicializador da classe que carrega o arquivo Excel na memória.
        self.data = pd.read_excel(file_path)
    
    def extract(self): #Método que extrai os dados do arquivo Excel.
        return self.data
    
    def analise(self): #Método que realiza a análise inicial dos dados.
        print("1. Quantidade de elementos:")
        print(len(self.data))
        print("\n2. Nome das colunas:")
        print(self.data.columns.tolist())
        print("\n3. Tipo de dado das colunas:")
        print(self.data.dtypes)
        print("\n4. Análise estatística dos dados:")
        print(self.data.describe()) #describe: descreve a função definida pelo usuário (UDF) ou função externa especificada, incluindo a assinatura (isto é, argumentos), valor de retorno, linguagem e corpo (isto é, definição).

if __name__ == "__main__": #É uma condição que verifica se o script está sendo executado como o programa principal. Isso é útil para importar classes ou funções de um script em outros scripts sem que o código dentro do if seja executado.
    file_path = "DataFramePOO.xlsx"  # Coloque o caminho do seu arquivo Excel aqui
    processo = dataframe(file_path)
    extracted_data = processo.extract()
    processo.analise()

#file_path: O caminho para o arquivo Excel que será processado.
#extracted_data: Os dados extraídos do arquivo Excel.
#STD = DESVIO PADRÃO, O QUANTO OS MEUS VALORES DESVIAM DA MÉDIA
#VAR = VARIANCIA
#MEAN = MÉDIA 
#MEDIAN = MEDIANA
#QUANTILE = QUANTIL
    #