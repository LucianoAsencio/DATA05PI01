from ETL import df_completo
import pandas as pd

# Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season])
def get_max_duration(año, plataforma, tipo):
 
    id = df_completo.reset_index(drop=True).query(f"release_year == {año} and platform == '{plataforma.capitalize()}' and unit == '{tipo.capitalize()}'").duration.idxmax()

    titulo = df_completo.reset_index(drop=True).title[id]
    duracion = df_completo.reset_index(drop=True).duration[id]

    if tipo.lower() == 'min':
        return f"La película es {titulo} y dura {duracion} minutos"
    elif tipo.lower() == 'season':
        return f"La serie es: {titulo} y dura {duracion} temporadas"
    else:
        return f"Algún dato no fue ingresado correctamente, vuelva al inicio para ver el formato"


# Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)
def get_count_platform(plataforma):
 
    tvShow_Movies = df_completo.query(f"platform == '{plataforma.capitalize()}'").groupby(['type', 'platform']).count()

    titulos = tvShow_Movies.title

    titulos = titulos.reset_index(drop=True)

    cantidad_peliculas = titulos[0]
    cantidad_series = titulos[1]

    return f"La plataforma {plataforma} tiene {cantidad_peliculas} películas y {cantidad_series} series"

# Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')
# Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.
def get_listedin(genero):
 
    cantidad_por_plataforma = df_completo[df_completo.listed_in.str.contains(genero.title())].groupby(['platform']).title.count().sort_values(ascending=False)

    cantidad = cantidad_por_plataforma[0]
    plataforma = cantidad_por_plataforma.index[0]

    return f"La plataforma {plataforma} es la que más veces se repite el género {genero}. Se repite {cantidad} veces"

# Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)

def get_actor(plataforma, año):

    df_func = df_completo.query(f"platform == '{plataforma.capitalize()}' and release_year == {año}")
    
    lista_actores = []

    for lista_de_listas in df_func.cast.to_list():
        lista_de_listas = lista_de_listas.replace(', ',',').split(",")
        for actor in lista_de_listas:
            lista_actores.append(actor)


    dict_ocurrencias = pd.Series(lista_actores).value_counts().to_dict()
    
    dict_ocurrencias.pop('Sin Dato')
    

    actor_2 = max(dict_ocurrencias, key=dict_ocurrencias.get)
    apariciones = dict_ocurrencias[actor_2]

    return f"El actor con más apariciones es {actor_2} con un total de {apariciones} apariciones"