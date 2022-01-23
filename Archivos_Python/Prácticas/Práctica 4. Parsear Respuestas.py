import requests
from types import resolve_bases
from utilities import guardar_json 
from utilities import leer_json

url = "https://stats.nba.com/stats/playercareerstats?LeagueID=00&PerMode=PerGame&PlayerID=977"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "DNT": "1",
    "Host": "stats.nba.com",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
}

def descargar_json_datos(url):
    """
    -----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es descargarse los datos en formato json
    -----------------------------------------------------------------
    Parámetros:
        - url: Url de la página que contiene los datos
    """
    response = requests.get(url, headers = headers)
    response_json = response.json()
    return response_json

# La función guardar_json() y leer_json() se encuentran en otro archivo .py que es el de utilities

guardar_json(descargar_json_datos(url), file_path= "./Archivos_Python/Prácticas/data/json/kobe.json")

kobe_data = leer_json(file_path= "./Archivos_Python/Prácticas/data/json/kobe.json")

tipos = ['SEASON_ID', 'PLAYER_AGE', 'GP', 'PTS', 'AST', 'REB' ]

def buscar_indices(lista):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es sacar los índices donde se encuentran 
    los datos referentes a nuestra cabecera, es decir, si el SEASON_ID 
    aparece en el tercer elemento esta función nos añadirá a la lista 
    de índices que el SEASON_ID es el número 2.
    ----------------------------------------------------------------
    Parámetros:
        - lista: Lista con la cabecera de nuestros datos
    """
    indices = []
    for i in kobe_data['resultSets'][0]['headers']:
        if i in lista:
            indices.append(kobe_data['resultSets'][0]['headers'].index(i))
    return indices

def sacar_stats(encab, data):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es sacar los datos 
    ----------------------------------------------------------------
    Parámetros:
        - encab: Lista con los elementos de la cabecera
        - data: Json donde se encuentran nuestros datos 
    """
    regular_season_stats = [encab]
    for i in data['resultSets'][0]['rowSet']:
        lista = []
        for j in buscar_indices(encab):
            lista.append(i[j])
        regular_season_stats.append(lista)
    return regular_season_stats

regular_season_stats = sacar_stats(tipos, kobe_data)

def años_anotacion(datos):
    """
    ------------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es sacar el año donde más y menos puntos 
    ha anotado nuestro jugador.
    ------------------------------------------------------------------
    Parámetros:
        - datos: Lista de listas que tenga todos los datos del 
        jugador, en nuestro caso será los datos obtenidos de la función
        sacar_stats().
    ------------------------------------------------------------------
    Return:
    Esta función nos devuelve un diccionario que tiene como claves
    las estadísticas buscadas y como valor el año en el que se 
    han producido.
    """
    lista = []
    dic = {
        'año mas': '',
        'año menos' : ''
        }
    for i in datos:
        if type(i[2]) == str:
            continue
        else:
            lista.append(i[2]*i[3])
    maximo = lista.index(max(lista))
    minimo = lista.index(min(lista))
    season_max_points = regular_season_stats[maximo + 1][0]
    season_min_points = regular_season_stats[minimo + 1][0]
    dic["año mas"] = (season_max_points, max(lista))
    dic["año menos"] = (season_min_points,min(lista))
    return dic

print(años_anotacion(regular_season_stats))

def media_anotacion(datos):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es sacar la media de anotación de toda 
    la carrera del jugador deseado.
    ----------------------------------------------------------------
    Parámetros:
        - datos: Lista de listas que tenga todos los datos del 
        jugador, en nuestro caso será los datos obtenidos de la función
        sacar_stats().
    """
    lista = []
    for i in datos:
        if type(i[2]) == str:
            continue
        else:
            lista.append(i[2]*i[3])
    total_partidos = [i[2] for i in datos if type(i[2]) is not str]
    avg_career_points = sum(lista)/sum(total_partidos)
    return avg_career_points

print(media_anotacion(regular_season_stats))

def media_rebotes(datos):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es sacar la media de rebotes de toda 
    la carrera del jugador deseado.
    ----------------------------------------------------------------
    Parámetros:
        - datos: Lista de listas que tenga todos los datos del 
        jugador, en nuestro caso será los datos obtenidos de la función
        sacar_stats().
    """
    lista = []
    for i in datos:
        if type(i[2]) == str:
            continue
        else:
            lista.append(i[2]*i[4])
    avg_career_rebounds = sum(lista)/sum([i[2] for i in datos if type(i[2]) is not str])
    return(avg_career_rebounds)
        
def media_asist(datos):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es sacar la media de asistencias de toda 
    la carrera del jugador deseado.
    ----------------------------------------------------------------
    Parámetros:
        - datos: Lista de listas que tenga todos los datos del 
        jugador, en nuestro caso será los datos obtenidos de la función
        sacar_stats().
    """
    lista = []
    for i in datos:
        if type(i[2]) == str:
            continue
        else:
            lista.append(i[2]*i[5])
    avg_career_assists = sum(lista)/sum([i[2] for i in datos if type(i[2]) is not str])
    return(avg_career_assists)
        
print(media_rebotes(regular_season_stats))
print(media_asist(regular_season_stats))
