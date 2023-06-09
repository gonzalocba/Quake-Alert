# -*- coding: utf-8 -*-
"""streamlitTorta.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17miWkHQm9GjVbhs89cTbBp2i06lu8xbH
"""

import pandas as pd
import numpy as np
import requests                     
from datetime import datetime
import matplotlib.pyplot as plt    
import seaborn as sns              
import datetime

import pandas as pd

# Calcular la profundidad y magnitud media
profundidad_media = chile['profundidad'].mean()
magnitud_media = chile['magnitud'].mean()

# Mostrar los resultados
print("Profundidad media:", profundidad_media)
print("Magnitud media:", magnitud_media)

"""Graficamos

KPI en que estacion del año se generan mas sismos
"""

chile = pd.read_csv('/content/drive/MyDrive/PF_Sismos/chiledif_time.csv')

#cambio nombre de columnas para que coincidan con el original
chile.rename(columns={'fechaHora': 'fecha_hora'}, inplace=True)

chile['estacion'] = chile['fecha_hora'].dt.month.apply(lambda x: (x % 12 + 3) // 3)
frecuencia_estaciones = chile['estacion'].value_counts()
estacion_mas_frecuente = frecuencia_estaciones.idxmax()
print('La estación del año más frecuente es:', estacion_mas_frecuente)

chile_filtrado = chile[(chile['magnitud'] > 5) & (chile['profundidad'] < 70)]
chile_filtrado['fecha_hora'] = pd.to_datetime(chile_filtrado['fecha_hora'])
chile_filtrado['estacion'] = chile_filtrado['fecha_hora'].dt.month.apply(lambda x: (x % 12 + 3) // 3)
frecuencia_estaciones = chile_filtrado['estacion'].value_counts()
#est = frecuencia_estaciones.sort_values(ascending=False)
estacion_mas_frecuente = frecuencia_estaciones.idxmax()

# Mapeo de estaciones del año
estaciones_mapeadas = {1: 'Primavera', 2: 'Verano', 3: 'Otoño', 4: 'Invierno'}
estacion_mas_frecuente_mapeada = estaciones_mapeadas[estacion_mas_frecuente]

# Imprimir la estación del año más frecuente
print('La estación del año más frecuente para sismos con magnitud mayor a 5 y profundidad menor a 70 km es:', estacion_mas_frecuente_mapeada)

chile_filtrado = chile[(chile['magnitud'] > 5) & (chile['profundidad'] < 70)]
chile_filtrado['fecha_hora'] = pd.to_datetime(chile_filtrado['fecha_hora'])
chile_filtrado['estacion'] = chile_filtrado['fecha_hora'].dt.month.apply(lambda x: (x % 12 + 3) // 3)
frecuencia_estaciones = chile_filtrado['estacion'].value_counts()
etiquetas = ['Primavera', 'Verano', 'Otoño', 'Invierno']
valores = frecuencia_estaciones.reindex([1, 2, 3, 4])
etiquetas_filtradas = []
valores_filtrados = []
for etiqueta, valor in zip(etiquetas, valores):
    if valor > 0:
        etiquetas_filtradas.append(etiqueta)
        valores_filtrados.append(valor)
fig, ax = plt.subplots()
ax.pie(valores_filtrados, labels=etiquetas_filtradas, autopct='%1.1f%%', startangle=90, colors=[ '#e11e30', '#00BFFF', '#FFA500', '#8B4513'])