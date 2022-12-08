import pandas as pd

def limpiar_columnas(df):

    #Esta función limpia las columnas que no sirven para las querys

    columns = ['type', 'title', 'cast',
       'release_year', 'duration', 'listed_in', 'platform']

    df = df.drop(columns=[col for col in df if col not in columns])

    return df


def convertir_duracion(df_completo):

    #Esta función divide la columna duration en duration y unit
    # siendo duration = cantidad
    # y unit = unidad de medida de tiempo (minutos, temporadas)
    # Luego la une con el dataframe original y las renombra (por default son 0 y 1)

    columnas = df_completo.duration.str.split(expand=True)

    df_completo = pd.concat([df_completo, columnas], axis=1)

    df_completo.drop(columns='duration', inplace=True)

    df_completo.rename(columns={0:'duration', 1:'unit'}, inplace=True)

    return df_completo


def columnas_title(df):
        # Esta función aplica el método title en todas
        # las columnas que no sean duration o release_year

    for n in df:
        if n == 'duration' or n == 'release_year':
            pass
        else:
            df[f'{n}'] = df[f'{n}'].str.title()
    
    return df