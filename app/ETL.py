import pandas as pd
from FuncionesETL import limpiar_columnas, convertir_duracion, columnas_title


# Extraemos todos los datasets de los csv y los convertimos en dataframes

df_amazon = pd.read_csv('/datasets/amazon_prime_titles.csv')
df_disney = pd.read_csv('/datasets/disney_plus_titles.csv')
df_hulu = pd.read_csv('/datasets/hulu_titles.csv')
df_netflix = pd.read_json('/datasets/netflix_titles.json')


# Agregamos la columna platform para cada dataframe y especificamos a qué
# plataforma pertenece cada uno

df_amazon['platform'] = 'Amazon'
df_disney['platform'] = 'Disney'
df_hulu['platform'] = 'Hulu'
df_netflix['platform'] = 'Netflix'


# Concatenamos los 4 dataframes en uno para poder trabajar de manera más sintética

dataframes = [df_amazon, df_disney, df_hulu, df_netflix]

df_completo = pd.concat(dataframes)

# df_completo.fillna('Sin Dato', inplace=True)


# Aplicamos las funciones del módulo FuncionesETL

df_completo = limpiar_columnas(df_completo)
df_completo = convertir_duracion(df_completo)
df_completo = columnas_title(df_completo)


# Llenamos nulos y convertimos los tipos de datos necesarios

df_completo.duration.fillna(0, inplace=True)

df_completo.cast.fillna('Sin Dato', inplace=True)

df_completo.cast.replace('1','Sin Dato', inplace=True)

df_completo.duration = df_completo.duration.astype('int64')

df_completo.listed_in = df_completo.listed_in.astype(str)

df_completo.cast = df_completo.cast.astype(str)