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

#Seleção das colunas
df_final = df[['Nomes', 'MédiaF']].copy() # O .copy() evita avisos do Pandas

# DICA DE SEGURANÇA: Converte a coluna para números, forçando erro se houver texto
df_final['MédiaF'] = pd.to_numeric(df_final['MédiaF'], errors='coerce')

#Criando a lista das notas
lista_de_notas = df_final.values.tolist()

#Mostra se o aluno foi reprovado ou aprovado
print("\n=== Lista de Alunos ===")
for aluno in lista_de_notas:
    nome = aluno[0]
    nota = aluno[1]
   # Formatando para mostrar bonitinho
    print(f"Aluno: {nome:<40} | Média: {nota:.1f}", end=' | ')
    if(nota >= 7):
        print("Aluno Aprovado")
    else:
        print("Aluno Reprovado")
    
# Mostra o resultado dos 10 primeiros alunos
#print(df_final.head(10))

# Lista completa, use:
# print(df_final)