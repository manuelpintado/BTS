# -- ------------------------------------------------------------------------------------ -- #
# -- Proyecto: Estrategia basica para trading                                             -- #
# -- Codigo: RepasoPython.py - describir brevemente el codigo                             -- #
# -- Repositorio: https://github.com/                                                     -- #
# -- Autor: Manuel Pintado Delfin                                                         -- #
# -- ------------------------------------------------------------------------------------ -- #

# Importar librerias
import funciones as fn
import datos
import pandas as pd
from datetime import datetime

# Datos para descargar precios
OA_In = ['EUR_USD', 'USD_JPY', 'EUR_JPY', 'AUD_USD', 'GBP_USD', 'USD_CHF', 'AUD_JPY', 'EUR_AUD', 'EUR_GBP', 'GBP_JPY',
         'USD_CAD', 'AUD_CAD', 'EUR_CAD', 'GBP_AUD', 'USD_HKD', 'GBP_HKD', 'CAD_HKD', 'USD_MXN']  # Instrumento
OA_Gn = "H1"  # Granularidad de velas
fini = pd.to_datetime("2019-01-01 00:00:00").tz_localize('GMT')  # Fecha inicial
ffin = pd.to_datetime(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).tz_localize('GMT')  # Fecha final

for ticker in OA_In:
    # Descargar precios masivos
    df_pe = fn.f_precios_masivos(p0_fini=fini, p1_ffin=ffin, p2_gran=OA_Gn,
                                 p3_inst=ticker, p4_oatk=datos.token, p5_ginc=4900)

    # Calcular bandas de bollinger
    df_pe = fn.Bollinger_Bands(df=df_pe, window=20, ticker=ticker)

    fn.accion(df_pe, ticker)

