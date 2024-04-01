import pandas as pd
import matplotlib.pyplot as plt
import main as main
import mplfinance as mpf
import yfinance as yf
import matplotlib.dates as mdates
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# baixando dados de uma API
dados = yf.download('PETR4.SA', start='2023-01-01', end='2023-12-31')
# renomenado tudo
dados.columns = ['abertura', 'maximo', 'minimo',
                 'fechamento', ' fecha_ajust', 'volume']

dados.rename_axis('data', inplace=True)
# criando dados
dados['fechamento'].plot(figsize=(10, 6))
plt.title('variação do preço por data', fontsize=16)
plt.legend(['fechamento'])
plt.show()

##

df = dados.head(60).copy()
# convertentdo o índice em uma celula de data
df['data'] = df.index
# convertendo as datas para o formato numérico de maplotlib
# isso é necesssário para que o matplolib possa plotar as datas corrretamente no gráfico
df['data'] = df['data'].apply(mdates.date2num)
