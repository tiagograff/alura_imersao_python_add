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
