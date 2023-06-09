# -*- coding: utf-8 -*-
"""streamliMito.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P-6IZ-K1CF8Uk3kHAdIByrhq_rJ6ShPP
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt    
import seaborn as sns              
import datetime

import pandas as pd

# Supongamos que tienes un DataFrame llamado 'df.csv' con las columnas 'fecha_local' y 'hora_local'

'''
******************CARGA DATOS
'''

#df = pd.read_json('datos_chile_etl.json')

df = pd.read_csv('chiledif_time_1.csv')
print(df.columns)

# Convertir la columna 'fecha_local' a tipo datetime
df.csv['fecha_local'] = pd.to_datetime(df.csv['fecha_local'])

# Convertir la columna 'hora_local' a tipo datetime y formatearla a horas y minutos
df.csv['hora_local'] = pd.to_datetime(df.csv['hora_local']).dt.strftime('%H:%M')

# Crear la columna 'fechaHora' concatenando las columnas 'fecha_local' y 'hora_local'
df.csv['fechaHora'] = df.csv['fecha_local'].astype(str) + ' ' + df.csv['hora_local']

# Verificar el resultado
print(df.csv['fechaHora'])

import pandas as pd

df['fechaHora'] = pd.to_datetime(df['fechaHora'])
# Ordenar el DataFrame por la columna 'fecha_hora'
df = df.sort_values('fechaHora')

# Calcular la diferencia de tiempo entre filas consecutivas
df['diferencia_tiempo'] = df['fechaHora'].diff()

# Mostrar el DataFrame resultante
df

df_dif = df.csv.copy()
filtered_df = df_dif[(df_dif['magnitud'] > 6) & (df_dif['profundidad'] < 70)]
filtered_df['dif_tiempo'] = filtered_df['fechaHora'].diff()
filtered_df

'''
***************FIN CARGA DATOS
'''


"""Graficamos """

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
x = df['magnitud']
y = df['dif_tiempo'].dt.days
plt.xlabel('Magnitud')
plt.ylabel('Días desde el último sismo')
plt.title('Relación entre Magnitud y Días desde el último sismo')
plt.xlim(0, 8.5)
plt.ylim(0, 20)
plt.scatter(x, y)
plt.show()

'''
********IMPRESION GRAFICO DISPERSION
'''

# Mostrar el gráfico
plt.show()

import matplotlib.pyplot as plt

# Configurar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Definir los valores de los ejes x e y
x = filtered_df['magnitud']
y = filtered_df['dif_tiempo'].dt.days

# Configurar los ejes y etiquetas
plt.xlabel('Magnitud')
plt.ylabel('Días desde el último sismo')
plt.title('Relación entre Magnitud y Días desde el último sismo')

# Configurar los límites de los ejes
plt.xlim(0, 8.5)
plt.ylim(0, 20)

# Graficar las barras
plt.bar(x, y)

'''
**********IMPRESION DE BARRAS
'''

# Mostrar el gráfico
plt.show()