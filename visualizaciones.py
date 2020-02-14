# -- ------------------------------------------------------------------------------------ -- #
# -- Proyecto: Describir brevemente el proyecto en general                                -- #
# -- Codigo: RepasoPython.py - describir brevemente el codigo                             -- #
# -- Repositorio: https://github.com/                                                     -- #
# -- Autor: Nombre de autor                                                               -- #
# -- ------------------------------------------------------------------------------------ -- #

import plotly.graph_objects as go
import plotly.io as pio  # renderizador para visualizar imagenes
pio.renderers.default = "browser"  # render de imagenes para correr en script


# -- --------------------------------------------------------- GRÁFICA: velas OHLC Simple -- #
# -- ------------------------------------------------------------------------------------ -- #
# -- --- Velas tipo candlestick utilizando precios tipo OHLC

def g_velas(p0_de, ticker):
    """
    Parameters
    ----------
    p0_de : pd.DataFrame : Precios OHLC como datos de entrada

    Returns
    -------
    fig : plotly figure : Grafica final

    Debugging
    ---------
    datos_dd = pd.DataFrame({'timestamp': [], 'open': [], 'high': [], 'low': [], 'close': []},
                              index=[])

    """

    p0_de.columns = [list(p0_de.columns)[i].lower() for i in range(0, len(p0_de.columns))]

    fig = go.Figure(data=[go.Candlestick(x=p0_de['timestamp'],
                                         open=p0_de['open'], high=p0_de['high'],
                                         low=p0_de['low'], close=p0_de['close'])])

    fig.update_layout(margin=go.layout.Margin(l=50, r=50, b=20, t=50, pad=0),
                      title=dict(x=0.5, y=1, text='Precios Historicos OHLC'),
                      xaxis=dict(title_text='Hora del dia', rangeslider=dict(visible=False)),
                      yaxis=dict(title_text=str('Precio del '+ ticker)))
    fig.add_trace(go.Scatter(x=p0_de['timestamp'], y=p0_de['ma'], name="SMA (Close)"))
    fig.add_trace(go.Scatter(x=p0_de['timestamp'], y=p0_de['bb_upper'], name="UPPER (Close)"))
    fig.add_trace(go.Scatter(x=p0_de['timestamp'], y=p0_de['bb_lower'], name="LOWER (Close)"))

    fig.layout.autosize = False
    fig.layout.width = 840
    fig.layout.height = 520

    return fig