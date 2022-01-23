import requests
import json
from utilities import guardar_json
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Comillas_Pontifical_University"

# Práctica 7a - Beautifulsoup

def descargar_tabla(url):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es descargarse el código html de la 
    tabla deseada
    ----------------------------------------------------------------
    Parámetros:
        - url: Url de la página donde se encuentra la tabla que 
        deseamos descargarnos.
    ----------------------------------------------------------------
    Limitaciones:
    Esta función esta hecha para páginas donde unicamente exista una 
    tabla, en caso de haber más no se ejecuta nada.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        target_tables = soup.find_all("table", class_ = "infobox vcard")
        if len(target_tables) == 1:
            target_table = target_tables[0]
            return target_table
        else:
            print('Hay más de una tabla...')
    else:
        print('Se ha producido un error en la petición')


# Práctica 7b - Extraer Datos

datos = ['seal', 'motto_latin', 'motto_spanish', 'motto_english', 'type', 'established','affilitations', 'chancellor', 'vice_chancellor', 
'rector', 'students', 'location', 'campus', 'colors' , 'website', 'logo' ]

def sacar_datos(url, lista_datos):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es sacar los datos deseados de la tabla
    descargada en la práctica anterior.
    ----------------------------------------------------------------
    Parámetros:
        - url: Url de la página donde se encuentra la tabla que 
        deseamos descargarnos.
        - lista_datos: Lista con los datos que queremos sacar
    ----------------------------------------------------------------
    Return:
    Devuelve un diccionario donde las claves son los datos a sacar y 
    los valores son los datos obtenidos.
    """
    target_table = descargar_tabla(url)
    target_tr = target_table.find_all('tr')
    dic = {}
    for i in range(16):
        if i+1 not in [1,2,3,4,16]:
            dic[lista_datos[i]] = (target_tr[i+1].find('td')).get_text()
        elif i+1 in [1,16]:
            dic[lista_datos[i]] = 'https://es.wikipedia.org' + target_tr[i+1].find('a')['href'] 
        else:
            dic[lista_datos[i]] = (target_tr[i+1].find('i')).get_text()
    return dic

solucion = sacar_datos(url, datos)
print(solucion)

# Práctica 7c - Guardar datos

# La función guardar_json() está dentro del archivo utilities.py

guardar_json(sacar_datos(url, datos), file_path='./Archivos_Python/Prácticas/data/json/Práctica7.json')



