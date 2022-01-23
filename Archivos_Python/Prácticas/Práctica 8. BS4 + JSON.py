import requests
import json
from utilities import guardar_json
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/World_population'

def descargar_target_data(url):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es descargarse el código html de la 
    tabla deseada
    ----------------------------------------------------------------
    Parámetros:
        - url: Url de la página donde se encuentra la tabla que 
        deseamos descargarnos.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    target_tables = soup.find_all("table", class_ = 'wikitable')
    target_table = target_tables[0]
    target_data = target_table.find_all('tr')
    return target_data

def añadir_header(elemento, dic, lista):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es añadir a un diccionario los 
    diferentes headers que queremos.
    ----------------------------------------------------------------
    Parámetros:
        - elemento: El header en formato html
        - dic: El diccionario que usaremos
        - lista: Lista a la que se le irán añadiendo los diferentes 
        headers.
    """
    header_no = elemento.get_text()
    header = header_no.replace('\n', '')
    dic[header] = ''
    lista.append(header)

def limpieza(num_no1):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es limpiar el texto obtenido de un 
    código html
    ----------------------------------------------------------------
    Parámetros:
        - num_no1: Elemento de texto sacado del html
    """
    num_no2 = num_no1.replace('\n', '')
    num_no3 = num_no2.replace('\xa0','')
    num_no4 = num_no3.replace('[note 1]','')
    num_no5 = num_no4.replace('[18]','')
    num_no6 = num_no5.replace('[19]','')
    num_no7 = num_no6.replace('[note 2]','')
    num_no8 = num_no7.replace('[note 3]','')
    num = num_no8.replace('[17]','')
    return num

def añadir_elem(elemento, elementos, lista):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es añadir los diferentes elementos a 
    una lista que será los valores de nuestro diccionario.
    ----------------------------------------------------------------
    Parámetros:
        - elemento: Elemento de la lista de html
        - elementos: Lista que contiene todos los elementos html
        - lista: Lista donde se añaden el texto de los html
    """
    num_no1 = elemento.get_text()
    num = limpieza(num_no1)
    if elementos.index(elemento) == 0:
        lista[0].append(num)
    elif elementos.index(elemento) == 1:
        lista[1].append(num)
    elif elementos.index(elemento) == 2:
        lista[2].append(num)
    elif elementos.index(elemento) == 3:
        lista[3].append(num)
    else:
        lista[4].append(num)

def descargar_datos(url):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es descargarse los datos de la tabla 
    deseada.
    ----------------------------------------------------------------
    Parámetros:
        - url: Url de la página donde se encuentra la tabla que 
        deseamos descargarnos.
    ----------------------------------------------------------------
    Return:
    Diccionario con los datos descargados.
    """
    target_data = descargar_target_data(url)
    data = {}
    datos = [[],[],[],[],[]]
    headers = []
    for i in target_data:
        if target_data.index(i) == 0:
            target_header = i.find_all('th')
            for j in target_header:
                    añadir_header(j, data, headers)
        else:
            data_no = i.find_all('td')
            for j in data_no:
                añadir_elem(j,data_no,datos)
    for i in data.keys():
        data[i] = datos[headers.index(i)]
    return data

sol = descargar_datos(url)
print(sol)

guardar_json(sol, file_path='./Archivos_Python/Prácticas/data/json/Práctica8.json')