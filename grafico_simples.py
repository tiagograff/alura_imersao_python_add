import pandas as pd
import plotly.express as px
import main as main

df_principal_saldo_reset = main.df_principal_saldo_reset

fig1 = px.bar(df_principal_saldo_reset, x='resultado', y='variacao_rs',
              text='variacao_rs', title='variação em reais por resultado')
fig1.show()
