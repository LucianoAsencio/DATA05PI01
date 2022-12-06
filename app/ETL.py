import pandas as pd
import FuncionesETL as fe
import querys as qr


# Extraemos todos los datasets de los csv y los convertimos en dataframes

df_amazon = pd.read_csv('/datasets/amazon_prime_titles.csv')
df_disney = pd.read_csv('/datasets/disney_plus_titles.csv')
df_hulu = pd.read_csv('/datasets/disney_plus_titles.csv')
df_netflix = pd.read_json('/datasets/netflix_titles.json')


# Agregamos la columna platform para cada dataframe y específicamos a qué
# plataforma pertenece cada uno

df_amazon['platform'] = 'Amazon'
df_disney['platform'] = 'Disney'
df_hulu['platform'] = 'Hulu'
df_netflix['platform'] = 'Netflix'


# Concatenamos los 4 dataframes en uno para poder trabajar de manera más sintética

dataframes = [df_amazon, df_disney, df_hulu, df_netflix]

df_completo = pd.concat(dataframes)


# Aplicamos las funciones del módulo FuncionesETL

df_completo = fe.limpiar_columnas(df_completo)
fe.convertir_duracion(df_completo)
df_completo = fe.columnas_title(df_completo)