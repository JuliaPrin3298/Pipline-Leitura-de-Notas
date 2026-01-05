import pandas as pd

# Caminho do arquivo
caminho_arquivo = 'notas4B.xlsx'

# Definição do inicio e cabeçalho
df = pd.read_excel(caminho_arquivo, header=4, sheet_name=0)

# Limpeza nos nomes das colunas
df.columns = df.columns.str.strip()

# Remove linhas onde não tem nome de aluno
df = df.dropna(subset=['Nomes'])

#Seleção das colunas
df_final = df[['Nomes', 'MédiaF']]

# Mostra o resultado
print(df_final.head(10))

# Lista completa, use:
# print(df_final)