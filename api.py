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

mpf.plot(dados.head(30), type='candle', figsize=(
    16, 8), volume=True, mav=(7, 14), style='yahoo')
