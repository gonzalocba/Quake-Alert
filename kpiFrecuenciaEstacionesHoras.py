# -*- coding: utf-8 -*-
"""KPI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V2EPs-4xt7xLZPRsXFC12LQw21f-V8jx

Chile esta dividida en 16 regiones:

1-Región de Arica y Parinacota

2- Región de Tarapacá

3- Región de Antofagasta

4-Región de Atacama

5-Región de Coquimbo

6-Región de Valparaíso

7-Región Metropolitana de Santiago

8-Región del Libertador General Bernardo O'Higgins

9-Región del Maule

10-Región de Ñuble

11-Región del Biobío

12-Región de La Araucanía

13-Región de Los Ríos

14-Región de Los Lagos

15-Región de Aysén del General Carlos Ibáñez del Campo

16-Región de Magallanes y de la Antártica Chilena

La Región de Tarapacá, en el norte de Chile, es conocida por tener una alta actividad sísmica. Esta región se encuentra en una zona de subducción donde convergen las placas tectónicas de Nazca y Sudamericana. Como resultado, experimenta frecuentes movimientos sísmicos, incluyendo terremotos de magnitud significativa.

Además de la Región de Tarapacá, otras regiones de Chile también son propensas a la actividad sísmica debido a su ubicación geográfica en la zona de subducción. Estas incluyen la Región de Antofagasta, la Región de Atacama, la Región de Coquimbo, la Región de Valparaíso, la Región Metropolitana de Santiago, la Región del Maule, la Región del Biobío y la Región de La Araucanía, entre otras.

Cabe destacar que Chile es uno de los países más sísmicamente activos del mundo debido a su posición en el Cinturón de Fuego del Pacífico, una zona de intensa actividad sísmica y volcánica. Por lo tanto, se recomienda a los residentes y visitantes de Chile estar preparados y seguir las medidas de seguridad adecuadas en caso de un evento sísmico.
El Cinturón de Fuego del Pacífico, también conocido como Anillo de Fuego del Pacífico, es una zona geográfica en forma de herradura que rodea el borde del Océano Pacífico. Es famoso por ser una de las regiones más sísmicamente activas y volcánicamente activas del mundo.

El Cinturón de Fuego del Pacífico abarca aproximadamente el 75% de los volcanes activos del mundo y es el escenario de la mayoría de los terremotos más fuertes del planeta. Se extiende desde la costa occidental de América del Sur, pasando por América Central y del Norte, hasta alcanzar el este de Asia, incluyendo Japón, Filipinas, Indonesia y Nueva Zelanda. Luego se curva hacia el sur, abarcando las Islas del Pacífico suroriental.

Esta región es el resultado de la interacción de varias placas tectónicas en los límites de las placas. Hay una combinación de subducción (donde una placa se sumerge bajo otra) y zonas de falla transformante (donde las placas se deslizan lateralmente una respecto a la otra). Estos procesos generan una intensa actividad sísmica y volcánica.

El Cinturón de Fuego del Pacífico es una zona de gran interés científico debido a la posibilidad de estudiar y comprender mejor los procesos tectónicos y volcánicos que ocurren en ella. Sin embargo, también representa un riesgo significativo en términos de terremotos, tsunamis y erupciones volcánicas para las poblaciones que viven en estas áreas.

En Chile existen rutas y caminos designados como "rutas de evacuación" que se utilizan durante situaciones de emergencia, incluyendo sismos y otros eventos naturales. Estas rutas de evacuación están planificadas y establecidas por las autoridades competentes, como la Oficina Nacional de Emergencia del Ministerio del Interior y Seguridad Pública (ONEMI).

Las rutas de evacuación están diseñadas estratégicamente para facilitar la salida segura de las personas de áreas afectadas por desastres. Por lo general, se identifican y señalizan con letreros especiales que indican que son rutas de evacuación. Estas rutas suelen ser vías principales, carreteras o caminos que conducen a zonas más seguras, como zonas elevadas o áreas alejadas del peligro.

caminos: https://emergenciaydesastres.mineduc.cl/mapa-de-riesgo/
"""

import pandas as pd
import numpy as np

import requests                     
from datetime import datetime
import matplotlib.pyplot as plt    
import seaborn as sns              
import datetime

#con este codigo se elige fechas a descargar, y columnas y de que pagina

# Define los parámetros de la consulta
params = {
    "format": "geojson",
    "starttime": "2023-01-01",
    "endtime": "2023-05-15",
    "minmagnitude": 2
    
}

# Hacer una solicitud HTTP a la API con los parámetros de consulta
response = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query", params=params)

# Obtener la respuesta en formato JSON
data = response.json()

# Crear un DataFrame con los datos relevantes
chile_j = pd.DataFrame(
    [
        [
            feature["properties"]["mag"],
            feature["geometry"]["coordinates"][0],
            feature["geometry"]["coordinates"][1],
            feature["geometry"]["coordinates"][2],
            pd.to_datetime(feature["properties"]["time"], unit="ms").date(),
            pd.to_datetime(feature["properties"]["time"], unit="ms").time()
        ]
        for feature in data["features"]
    ],
    columns=["magnitud", "longitud", "latitud", "profundidad", "fecha_local", "hora_local"]
)

chile_j.head()

#bajar en csv
chile_j.to_csv('chile.csv')

from google.colab import files
files.download('chile.csv')

chile = pd.read_csv('/content/drive/MyDrive/PF_Sismos/chile (1).csv')

chile.info()

chile.head()

df_tiempo = chile.copy()

df_tiempo['hora_local'] = pd.to_datetime(df_tiempo['hora_local'])

"""probar con unir fecha y hora"""

df_fh = chile.copy()

df_fh['fecha_hora'] = pd.to_datetime(df_fh['fecha_local'] + ' ' + df_fh['hora_local'])

df_fh

df_fh.info()

df_fh.sort_values(by='fecha_hora', ascending=True, inplace=True)

df_fh['diferencia_tiempo'] = df_fh['fecha_hora'].diff()

df_fh

# Filtrar los sismos con magnitud mayor a 4 y profundidad menor a 300 km

filtered_df = df_dif[(df_dif['magnitud'] > 6) & (df_dif['profundidad'] < 70)]
filtered_df['dif_tiempo'] = filtered_df['fecha_hora'].diff()

chile_filtrado['diferencia_tiempo'].describe()

"""Podemos observar que los sismos ocurren alrededor del mismo rango horario osea entre las 15hs y las 18hs, y no pasa mas de un día para los sismos de 4° y menos de 300km de profundidad.Desde comieno de año al 15 de mayo han habido 4867 sismos, en promedio todos los dias hay sismos de esa manitud. la menor cantidad de tiempo entre un sismo y otro fue de aproximadamente 20 segundos, y la mayor cantidad de tiempo fue de 1 hora y 51 minutos aproximadamente.



"""

df_dif = df_fh.copy()
filtered_df = df_dif[(df_dif['magnitud'] > 6) & (df_dif['profundidad'] < 70)]
filtered_df['dif_tiempo'] = filtered_df['fecha_hora'].diff()

#filtro['diferencia_tiempo'] = filtro['fecha_hora'].diff()
filtered_df

#aca borre columnas
filtered_df.drop(columns=['diferencia_tiempo'], inplace= True)
filtered_df.drop(columns=['fecha_local','hora_local'], inplace= True)

filtered_df.info()

filtered_df.describe()

"""Aca podemos concluir para los sismos de 6 grados en adelante y a menos de 70 km de profundidad que han ocurrido 22 desde comienzo de año 2023 hasta 15 de mayo del mismo año, el de mayor magnitud fue de 7.8 grados en escala de Richer y hacia mas de 18 días que no se producia un sismo de ese nivel de magnitud los cuales son considerados graves.

Graficamos
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from datetime import timedelta

# Crear una lista de colores rojos en un degradado
colormap = plt.cm.get_cmap('Reds')
normalize = mcolors.Normalize(vmin=6, vmax=8)  # Rango de magnitudes

# Configurar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Convertir la diferencia de tiempo a días
dif_tiempo_dias = filtered_df['dif_tiempo'] / timedelta(days=1)

# Generar el gráfico de dispersión
scatter = plt.scatter(dif_tiempo_dias, filtered_df['magnitud'], c=filtered_df['magnitud'], cmap=colormap, norm=normalize)

# Añadir una barra de colores
cbar = plt.colorbar(scatter)
cbar.set_label('Magnitud')

# Configurar los ejes y etiquetas
plt.xlabel('Diferencia de tiempo (días)')
plt.ylabel('Magnitud')
plt.title('Relación entre magnitud y diferencia de tiempo de sismos seleccionados')

# Mostrar el gráfico
plt.show()

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from datetime import timedelta

# Crear una lista de colores rojos en un degradado
colormap = plt.cm.get_cmap('Reds')
normalize = mcolors.Normalize(vmin=6, vmax=8)  # Rango de magnitudes

# Configurar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Convertir la diferencia de tiempo a días
dif_tiempo_dias = filtered_df['dif_tiempo'] / timedelta(days=1)

# Calcular las posiciones de las barras
x_pos = range(len(filtered_df))

# Graficar las barras de magnitud
plt.bar(x_pos, filtered_df['magnitud'], color=colormap(normalize(filtered_df['magnitud'])))

# Configurar los ejes y etiquetas
plt.xlabel('Diferencia de tiempo (días)')
plt.ylabel('Magnitud')
plt.title('Magnitud de sismos seleccionados')
plt.xticks(x_pos, dif_tiempo_dias, rotation=90)

# Añadir una barra de colores
cbar = plt.colorbar(label='Magnitud')

# Mostrar el gráfico
plt.show()

"""KPI en que estacion del año se generan mas sismos"""

# Define los parámetros de la consulta
params = {
    "format": "geojson",
    "starttime": "2022-01-01",
    "endtime": "2023-01-01",
    "minmagnitude": 6
    
}

# Hacer una solicitud HTTP a la API con los parámetros de consulta
response = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query", params=params)

# Obtener la respuesta en formato JSON
data = response.json()

# Crear un DataFrame con los datos relevantes
chile22_6 = pd.DataFrame(
    [
        [
            feature["properties"]["mag"],
            feature["geometry"]["coordinates"][0],
            feature["geometry"]["coordinates"][1],
            feature["geometry"]["coordinates"][2],
            pd.to_datetime(feature["properties"]["time"], unit="ms").date(),
            pd.to_datetime(feature["properties"]["time"], unit="ms").time()
        ]
        for feature in data["features"]
    ],
    columns=["magnitud", "longitud", "latitud", "profundidad", "fecha_local", "hora_local"]
)

chile22_6

chile22_6.head(3)

chile22_6.info()

sismos_por_estacion

import pandas as pd
import matplotlib.pyplot as plt
#chile22_6['fecha_local'] = pd.to_datetime(chile22_6['fecha_local'])

# Calcular la cantidad de sismos por estación del año
chile22_6['estacion'] = chile22_6['fecha_local'].dt.to_period('Q').dt.strftime('%b')

sismos_por_estacion = chile22_6['estacion'].value_counts()

# Ordenar las estaciones del año en orden cronológico
estaciones_ordenadas = ['Dec', 'Mar', 'Jun', 'Sep']

# Mapeo de colores por estación del año
colores = {'Dec': 'orange', 'Mar': 'yellow', 'Jun': 'blue', 'Sep': 'green'}

# Mapeo de etiquetas por estación del año
etiquetas = {'Dec': 'Verano', 'Mar': 'Otoño', 'Jun': 'Invierno', 'Sep': 'Primavera'}

# Crear un DataFrame con los datos de cantidad de sismos por estación del año
kpi_sismos_estaciones = pd.DataFrame({
    'Estacion': estaciones_ordenadas,
    'Cantidad de Sismos': [sismos_por_estacion[estacion] for estacion in estaciones_ordenadas]
})

# Configurar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Graficar las barras de cantidad de sismos por estación del año con colores personalizados
plt.bar(kpi_sismos_estaciones['Estacion'], kpi_sismos_estaciones['Cantidad de Sismos'],
        color=[colores[estacion] for estacion in kpi_sismos_estaciones['Estacion']])

# Configurar los ejes y etiquetas
plt.xlabel('Estación del Año')
plt.ylabel('Cantidad de Sismos')
plt.title('Cantidad de Sismos por Estación del Año')

# Cambiar las etiquetas en el eje x por nombres de estaciones
plt.xticks(kpi_sismos_estaciones['Estacion'], [etiquetas[estacion] for estacion in kpi_sismos_estaciones['Estacion']])

# Mostrar el gráfico
plt.show()

# Obtener la estación del año con la mayor cantidad de sismos
estacion_max_sismos = sismos_por_estacion.idxmax()
cantidad_max_sismos = sismos_por_estacion.max()

# Configurar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Graficar las barras de cantidad de sismos por estación del año con colores personalizados
plt.bar([etiquetas[estacion] for estacion in estaciones_ordenadas], kpi_sismos_estaciones['Cantidad de Sismos'],
        color=[colores[estacion] for estacion in estaciones_ordenadas])

# Configurar los ejes y etiquetas
plt.xlabel('Estación del Año')
plt.ylabel('Cantidad de Sismos')
plt.title('Cantidad de Sismos por Estación del Año')

# Mostrar el valor del KPI en el gráfico
plt.annotate(f"{etiquetas[estacion_max_sismos]} ({cantidad_max_sismos} sismos)",
             xy=(etiquetas[estacion_max_sismos], cantidad_max_sismos),
             xytext=(10, 10),
             textcoords="offset points",
             ha='center',
             va='center',
             fontsize=12,
             color='black',
             arrowprops=dict(arrowstyle="->"))

# Mostrar el gráfico
plt.show()

"""Aca se puede observar que en el año 2022 hubieron mas sismos de 6 grados en adelante en otoño.Por lo que nos indicaría que en esa época se debería incrementar las aertas de prevención sismica.

Ahora Analisamos año 2021 para comparar si sigue la misma tendencia
"""

# Define los parámetros de la consulta
params = {
    "format": "geojson",
    "starttime": "2021-01-01",
    "endtime": "2022-01-01",
    "minmagnitude": 6
    
}

# Hacer una solicitud HTTP a la API con los parámetros de consulta
response = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query", params=params)

# Obtener la respuesta en formato JSON
data = response.json()

# Crear un DataFrame con los datos relevantes
chile21_6 = pd.DataFrame(
    [
        [
            feature["properties"]["mag"],
            feature["geometry"]["coordinates"][0],
            feature["geometry"]["coordinates"][1],
            feature["geometry"]["coordinates"][2],
            pd.to_datetime(feature["properties"]["time"], unit="ms").date(),
            pd.to_datetime(feature["properties"]["time"], unit="ms").time()
        ]
        for feature in data["features"]
    ],
    columns=["magnitud", "longitud", "latitud", "profundidad", "fecha_local", "hora_local"]
)

chile21_6.info()

sismos_por_estacion22_6

chile21_6['fecha_local'] = pd.to_datetime(chile21_6['fecha_local'])

# Calcular la cantidad de sismos por estación del año
chile21_6['estacion'] = chile21_6['fecha_local'].dt.to_period('Q').dt.strftime('%b')

sismos_por_estacion22_6 = chile21_6['estacion'].value_counts()

# Ordenar las estaciones del año en orden cronológico
estaciones_ordenadas = ['Dec', 'Mar', 'Jun', 'Sep']

# Mapeo de colores por estación del año
colores = {'Dec': 'orange', 'Mar': 'yellow', 'Jun': 'blue', 'Sep': 'green'}

# Mapeo de etiquetas por estación del año
etiquetas = {'Dec': 'Verano', 'Mar': 'Otoño', 'Jun': 'Invierno', 'Sep': 'Primavera'}

# Crearkpi_sismos_estaciones22_6  un DataFrame con los datos de cantidad de sismos por estación del año
KPI21= pd.DataFrame({
    'Estacion': estaciones_ordenadas,
    'Cantidad de Sismos': [sismos_por_estacion[estacion] for estacion in estaciones_ordenadas]
})

# Configurar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Graficar las barras de cantidad de sismos por estación del año con colores personalizados
plt.bar(KPI21['Estacion'], KPI21['Cantidad de Sismos'],
        color=[colores[estacion] for estacion in KPI21['Estacion']])

# Configurar los ejes y etiquetas
plt.xlabel('Estación del Año')
plt.ylabel('Cantidad de Sismos')
plt.title('Cantidad de Sismos por Estación del Año')

# Cambiar las etiquetas en el eje x por nombres de estaciones
plt.xticks(KPI21['Estacion'], [etiquetas[estacion] for estacion in KPI21['Estacion']])

# Mostrar el gráfico
plt.show()

# Obtener la estación del año con la mayor cantidad de sismos
estacion_max_sismos = sismos_por_estacion22_6.idxmax()
cantidad_max_sismos = sismos_por_estacion22_6.max()

# Configurar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Graficar las barras de cantidad de sismos por estación del año con colores personalizados
plt.bar([etiquetas[estacion] for estacion in estaciones_ordenadas], kpi_sismos_estaciones['Cantidad de Sismos'],
        color=[colores[estacion] for estacion in estaciones_ordenadas])

# Configurar los ejes y etiquetas
plt.xlabel('Estación del Año')
plt.ylabel('Cantidad de Sismos')
plt.title('Cantidad de Sismos por Estación del Año')

# Mostrar el valor del KPI en el gráfico
plt.annotate(f"{etiquetas[estacion_max_sismos]} ({cantidad_max_sismos} sismos)",
             xy=(etiquetas[estacion_max_sismos], cantidad_max_sismos),
             xytext=(10, 10),
             textcoords="offset points",
             ha='center',
             va='center',
             fontsize=12,
             color='black',
             arrowprops=dict(arrowstyle="->"))

# Mostrar el gráfico
plt.show()

"""
KPI 4

Podemos concluir que comparando dos años 2021 la estacion del año que mas sismo hay es en otoño, verano

KPI en que horarios ocurren mayor cantidad de sismos
"""

chileH = pd.read_csv('/content/drive/MyDrive/PF_Sismos/chileFrec.csv')

chileH.head(5)

import pandas as pd
import matplotlib.pyplot as plt

# Convertir la columna 'fecha_hora' al tipo de dato datetime
chileH['fecha_hora'] = pd.to_datetime(chileH['fecha_hora'])

# Filtrar los sismos con magnitud mayor a 5 y profundidad menor a 300 km
filtro = (chileH['magnitud'] > 5) & (chileH['profundidad'] < 70)
chileH_filtrado = chileH[filtro]

# Calcular la cantidad de sismos por hora del día
sismos_por_hora = chileH_filtrado['fecha_hora'].dt.hour.value_counts().sort_index()

# Configurar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Graficar las barras de cantidad de sismos por hora del día
plt.bar(sismos_por_hora.index, sismos_por_hora.values)

# Configurar los ejes y etiquetas
plt.xlabel('Hora del Día')
plt.ylabel('Cantidad de Sismos')
plt.title('Cantidad de Sismos por Hora del Día (Magnitud > 6, Profundidad < 70 km)')

# Mostrar el gráfico
plt.show()

"""la mayoria de los sismos de mas de 5 grados a menos de 70 km de profundidad se producen 1am, 10 am y 18 am"""