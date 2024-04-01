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

##

df = dados.head(60).copy()
# convertentdo o índice em uma celula de data
df['data'] = df.index
# convertendo as datas para o formato numérico de maplotlib
# isso é necesssário para que o matplolib possa plotar as datas corrretamente no gráfico
df['data'] = df['data'].apply(mdates.date2num)

## criando outro gráfico ##

fig, ax = plt.subplots(figsize=(15, 8))
width = 0.7

##


for i in range(len(df)):
    # determinando a cor do candel
    # se o preço do fechamento for maior que o de abertura, candle é verde
    # se for menor, o cendle será vermelho
    if df['fechamento'].iloc[i] > df['abertura'].iloc[i]:
        color = 'green'
    else:
        color = 'red'
    # desenhando a linha vertical do candle
    # essa linha mostra os preços máximo e mínimo
    # usando 'ax.plot' para desenhar uma linha vertical
    # define o ponto x da linha // define
    ax.plot([df.index[i], df.index[i]],
            [df['minimo'].iloc[i], df['maximo'].iloc[i]],
            color=color,
            linewidth=1)

    ax.add_patch(plt.Rectangle((df['data'].iloc[i] - width/2, min(df['abertura'].iloc[i], df['fechamento'].iloc[i])),
                 width, abs(df['fechamento'].iloc[i] - df['abertura'].iloc[i]), facecolor=color))

    df['MA7'] = df['fechamento'].rolling(window=7).mean()
    df['MA14'] = df['fechamento'].rolling(window=14).mean()

    ##

ax.plot(df['data'], df['MA7'], color='orange', label='média móvel 7 dias')
ax.plot(df['data'], df['MA14'], color='yellow',
        label='média móvel 14 dias')

ax.legend()

# formatando o eixo x para mostrar as datas
# configurar o formato da data e a rotação para melhor legibilidade
ax.xaxis_date()  # as datas estão sendo usadas no eixo x
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# adcionando título e rótulos para eixos x e y
plt.title('grafico de cadlestick')
plt.xlabel('data')
plt.ylabel('preço')

# adcionando uma grade para facilitar a visualização
plt.grid(True)

plt.title('gráfico de velas', fontsize=16)
plt.legend(['fechamento'])

# criando subplots

fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, subplot_titles=('candlesticks', 'volume transacionado'),
                    row_width=[0.2, 0.7])

# adcionando o gráfico de candlesstick
fig.add_trace(go.Candlestick(x=df.index,
                             open=df['abertura'],
                             high=df['maximo'],
                             low=df['minimo'],
                             close=df['fechamento'],
                             name='candlestick'),
              row=1, col=1)

# adicionando as médias móveis
fig.add_trace(go.Scatter(x=df.index,
                         y=df['MA7'],
                         mode='lines',
                         name='MA7 - média móvel 7 dias'),
              row=1, col=1)

fig.add_trace(go.Scatter(x=df.index,
                         y=df['MA14'],
                         mode='lines',
                         name='MA14 - média móvel 14 dias'),
              row=1, col=1)

# adcionando o gráfico de barras para o volume

fig.add_trace(go.Bar(x=df.index,
                     y=df['volume'],
                     name='volume'
                     ), row=2, col=1)

# atualizando layout

fig.update_layout(yaxis_title='preço',
                  xaxis_rangeslider_visible=False,
                  width=1100, height=600)

fig.show()
plt.show()
