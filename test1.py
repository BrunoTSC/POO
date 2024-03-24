class ETL:
    def __init__(self, file_path):
        self.data = pd.read_excel(file_path)
        self.quant_ele = len(self.data)
        self.columns = list(self.data.columns)
        self.data_types = self.data.dtypes

    def extract(self):
        return self.data

    def analise_inicial(self):
        print("Quantidade de elementos", self.quant_ele)
        print("Tipo de dado das colunas:")
        print(self.data_types)

if __name__ == "__main__":
    file_path = "DataframePOO.xlsx"
    processor = ETL(file_path)
    extracted_data = processor.extract()
    processor.analise_inicial()