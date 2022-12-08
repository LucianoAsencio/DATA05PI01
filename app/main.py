from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import querys as qr

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
async def index():
    return '''
    <html>
    <head>
    </head>
    <body>
    <h1> Proyecto Individual 01 - Data engineer </h1>
    <h3> /docs para ver la documentación </h3>
    </body>
    </html>'''


@app.get('/get_max_duration({anio}_{plataforma}_{unidad})')
async def duracion_maxima(anio:int, plataforma:str, unidad:str):
    return qr.get_max_duration(anio, plataforma, unidad)


@app.get('/get_count_plataform({plataforma})')
async def cantidad_plataforma(plataforma:str):
    return qr.get_count_platform(plataforma)


@app.get('/get_listedin({genero})')
async def genero_plataforma(genero:str):
    return qr.get_listedin(genero)

@app.get('/get_actor({plataforma}_{anio})')
async def actor_repetido(plataforma:str, anio:int):
    return qr.get_actor(plataforma, anio)