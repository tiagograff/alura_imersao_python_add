import pandas as pd
# lendo arquivo ações
arquivo_acoes = './alura/alura_imersao_python_add/dados/acoes.csv'
df_acoes = pd.read_csv(arquivo_acoes)
# lendo arquivo principal
arquivo_principal = './alura/alura_imersao_python_add/dados/principal.csv'
df_principal = pd.read_csv(arquivo_principal)
# lendo arquivo sobre
arquivo_sobre = './alura/alura_imersao_python_add/dados/sobre.csv'
df_sobre = pd.read_csv(arquivo_sobre)
# lendo arquivo ticker
arquivo_ticker = './alura/alura_imersao_python_add/dados/ticker.csv'
df_ticker = pd.read_csv(arquivo_ticker)

# # alguns comandos de teste
# print(df_acoes.head(10))
