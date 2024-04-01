import pandas as pd
# lendo arquivo ações
arquivo_acoes = './alura/alura_imersao_python_add/dados/acoes.csv'
df_acoes = pd.read_csv(arquivo_acoes)
# lendo arquivo principal
arquivo_principal = './alura/alura_imersao_python_add/dados/principal.csv'
df_principal = pd.read_csv(arquivo_principal)
# selecionando colunas
df_principal = df_principal[['ativo', 'data',
                             'último (R$)', 'var. dia (%)']].copy()
# reenomenado colunas
df_principal = df_principal.rename(
    columns={'último (R$)': 'valor_final', 'var. dia (%)': 'var_dia_pct'}).copy()
# mudando da , para o ponto e mudando tipo dos valores
df_principal['valor_final'] = df_principal['valor_final'].str.replace(
    ',', '.').astype(float).copy()
df_principal['var_dia_pct'] = df_principal['var_dia_pct'].str.replace(
    ',', '.').astype(float).copy()
# lendo arquivo sobre
arquivo_sobre = './alura/alura_imersao_python_add/dados/sobre.csv'
df_sobre = pd.read_csv(arquivo_sobre)
# lendo arquivo ticker
arquivo_ticker = './alura/alura_imersao_python_add/dados/ticker.csv'
df_ticker = pd.read_csv(arquivo_ticker)

# criando coluna variação do dia em porcentagem
df_principal['var_pct'] = df_principal['var_dia_pct'] / 100

# criando coluna de valor principal
df_principal['valor_inicial'] = df_principal['valor_final'] / \
    (df_principal['var_pct'] + 1)

# criando coluna de quantidade de ações
df_principal = df_principal.merge(
    df_acoes, left_on='ativo', right_on='Código', how='left')
# excluir coluna
df_principal = df_principal.drop(columns=['Código'])
# renomeando coluna
df_principal = df_principal.rename(
    columns={'Qtde. Teórica': 'qtde_teorica'}).copy()
# mudando valor
df_principal['qtde_teorica'] = df_principal['qtde_teorica'].str.replace(
    '.', '').astype(float)

# criando coluna variação
df_principal['variacao_rs'] = (df_principal['valor_final'] -
                               df_principal['valor_inicial']) * df_principal['qtde_teorica']

# tirando a notacao cientifica
pd.options.display.float_format = '{:.2f}'.format

# trocando novamente
df_principal['qtde_teorica'] = df_principal['qtde_teorica'].astype(int)

# criando coluna resultado
# apply: uma função para chamar outra função. lambda: para cada linha
df_principal['resultado'] = df_principal['variacao_rs'].apply(
    lambda x: 'subiu' if x > 0 else ('desceu' if x < 0 else 'estavel'))

# criando a coluna nome da empresa
df_principal = df_principal.merge(
    df_ticker, left_on='ativo', right_on='Ticker', how='left')
# excluir coluna
df_principal = df_principal.drop(columns=['Ticker'])
# renomeando coluna
df_principal = df_principal.rename(
    columns={'Nome': 'nome_empresa'}).copy()

# criando coluna
# criando a coluna nome da empresa
df_principal = df_principal.merge(
    df_sobre, left_on='nome_empresa', right_on='nome', how='left')
# excluir coluna
df_principal = df_principal.drop(columns=['nome'])

# criando coluna categoria de idade
df_principal['cat_idade'] = df_principal['idade'].apply(
    lambda x: 'mais de 100' if x > 100 else ('menos de 50' if x < 50 else 'entre 50 e 100'))


## analises ##

# valor máximo
maior = df_principal['variacao_rs'].max().round(2)
# valor minímo
menor = df_principal['variacao_rs'].min().round(2)
# média entre valores
media = df_principal['variacao_rs'].mean().round(2)
# média de quem subiu
md_subiu = df_principal[df_principal['resultado']
                        == 'subiu']['variacao_rs'].mean()
md_subiu = round(md_subiu, 2)
# média de quem desceu
md_desceu = df_principal[df_principal['resultado']
                         == 'desceu']['variacao_rs'].mean()
md_desceu = round(md_desceu, 2)

# criando df dos apenas que subiram
df_principal_subiu = df_principal[df_principal['resultado'] == 'subiu']

# criando df analise segmento
df_principal_segmento = df_principal_subiu.groupby(
    'segmento')['variacao_rs'].sum().reset_index
df_principal_segmento_reset = df_principal_segmento().reset_index()

# criando df analise saldo
df_principal_saldo = df_principal.groupby(
    'resultado')['variacao_rs'].sum().reset_index
df_principal_saldo_reset = df_principal_saldo().reset_index()


# # alguns comandos de teste
# print(df_principal_subiu.head(10))
# print(maior)
# print(menor)
# print(media)
# print(md_subiu)
# print(md_desceu)
# print(df_principal_segmento)
# print(df_principal_saldo_reset)
