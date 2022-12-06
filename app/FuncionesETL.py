def limpiar_columnas(df):

    #Esta función limpia las columnas que no sirven para las querys

    columns = ['show_id', 'type', 'title', 'cast',
       'release_year', 'duration', 'listed_in', 'platform']

    df = df.drop(columns=[col for col in df if col not in columns])

    return df


def convertir_duracion(df):

    #Esta función divide la columna duration en duration y unit
    # siendo duration = cantidad
    # y unit = unidad de medida de tiempo (minutos, temporadas)

    df = df.join(df.duration.str.split(expand=True))

    df.drop(columns='duration', inplace=True)
    df.rename(columns={0:'duration',
                                1:'unit'}, inplace=True)

    pass
    #return df


def columnas_title(df):

    # Esta función aplica el método title en todas las columnas que no sean duration o release_year

    for n in df:
        if n == 'duration' or n == 'release_year':
            pass
        else:
            df[f'{n}'] = df[f'{n}'].str.title()
    
    return df