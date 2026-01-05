import pandas as pd

caminho_arquivo = 'notas4B.xlsx'

# Lê o arquivo
df = pd.read_excel(caminho_arquivo, header=4)

# Mostra a lista exata de colunas (copie e cole o resultado aqui se der erro)
print("--- LISTA DE COLUNAS ENCONTRADAS ---")
print(df.columns.tolist())
print("------------------------------------")