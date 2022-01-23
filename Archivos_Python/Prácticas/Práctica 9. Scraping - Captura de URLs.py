import requests
from bs4 import BeautifulSoup
from utilities import leer_csv
from utilities import guardar_csv

########################################################################
# Obtener las URLs de los países
########################################################################


url = 'https://en.wikipedia.org/wiki/Lists_of_universities_and_colleges_by_country'

def descarga_listado_por_continentes(url):
    """
    ----------------------------------------------------------------
    Explicación: 
    Función que se encarga de descargar un listado de paises por
    continentes.
    ---------------------------------------------------------------- 
    Parámetros:
        - url: Url de donde descargaremos el listado
    ---------------------------------------------------------------- 
    Return:
    Nos devuelve una lista con un listado de Url's de los diferentes
    paises separados por continentes.
    ---------------------------------------------------------------- 
    Limitaciones:
    Esta función unicamente sirve para descargar el listado de una
    única tabla, si hubiese más tendriamos error.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        data_pre = soup.find_all('div',class_ = "mw-parser-output")
        if len(data_pre) == 1:
            data_pre2 = data_pre[0]
            data = data_pre2.find_all('ul')
            data2 = [data[i] for i in range(3,12)]
            return data2
        else:
            print('Tenemos varias tablas...')
    else:
        print('Se ha producido un error en la petición')

def añadir_paises_urls(elemento, lista_paises, lista_urls):
    """
    ----------------------------------------------------------------
    Explicación: 
    Función que se encarga de añadir a diferentes listas los elementos
    obtenidos del html.
    ---------------------------------------------------------------- 
    Parámetros:
        - elemento: Elemento html que contiene la información del 
        país y su Url.
    """
    url_pais_no = elemento.find_all('a')
    url_pais_no2 = url_pais_no[0]
    url_pais = url_pais_no2['href']
    lista_urls.append('https://en.wikipedia.org' + url_pais)
    pais = elemento.get_text()
    lista_paises.append(pais)

def descargar_urls2(url):
    """
    ----------------------------------------------------------------
    Explicación: 
    Función que se encarga de realizar el proceso completo de 
    descarga de las diferentes Urls de los diferentes países.
    ---------------------------------------------------------------- 
    Parámetros:
        - url: Url de la pagina donde está nuestro listado.
    ---------------------------------------------------------------- 
    Return:
    Nos devuelve una lista con las Url's y los nombres de los 
    diferentes paises.
    ---------------------------------------------------------------- 
    Limitaciones:
    Esta función unicamente sirve para descargar el listado de una
    única tabla, si hubiese más tendriamos error.
    """
    data2 = descarga_listado_por_continentes(url)
    urls = []
    paises = []
    for pais_tot in data2:
        data_no = pais_tot.find_all('li')
        for j in data_no:
            añadir_paises_urls(j, paises, urls)
    datos_fase1 = [[paises[i],urls[i]] for i in range(len(urls))]
    return datos_fase1

guardar_csv(descargar_urls2(url), file_path='./Archivos_Python/Prácticas/data/csv/urls_paises2.csv')


########################################################################
# Obtener las URLs de los países
########################################################################

listado2 = leer_csv('./Archivos_Python/Prácticas/data/csv/urls_paises2.csv')

def obtener_url_pais2(datos, nomb_pais):
    """
    ------------------------------------------------------------------
    Explicación: 
    Función que se encarga de obtener la Url del país deseado.
    ------------------------------------------------------------------
    Parámetros:
        - datos: Listado obtenido en el apartado anterior con paises y
        sus respectivas Url's.
        - nomb_pais: Nombre del país del cual queremos obtener la Url.
    ------------------------------------------------------------------
    Return:
    Nos devuelve la Url del país deseado.
    ------------------------------------------------------------------
    Limitaciones:
    La posible limitación que se puede observar es el como se escribe 
    el país (por tema idioma) o si el país en cuestión no se encuentra 
    en los datos.
    """
    for par in datos:
        if par[0] == nomb_pais:
            indice = datos.index(par)
            url_germ = datos[indice][1]
    return url_germ

def descargar_listado_univ_pais(url):
    """
    ----------------------------------------------------------------
    Explicación: 
    Función que se encarga de descargar un listado por zonas 
    geograficas de las universidades del país deseado.
    ---------------------------------------------------------------- 
    Parámetros:
        - url: Url de la pagina donde está nuestro listado.
    ---------------------------------------------------------------- 
    Return:
    Devuelve una lista formada por listas de universidad por 
    zona geografica.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.find_all('div', class_="mw-parser-output")
    data_2 = data[0]
    data_3 = data_2.find_all('ul')
    data4 = [data_3[i] for i in range(3,10,2)]
    return data4

def añadir_elem(elemento, lista_urls_uni, lista_nomb_uni, l_alemania, l_url_alem,nomb_pais, url_pais):
    """
    ----------------------------------------------------------------
    Explicación: 
    Función que se encarga de añadir a diferentes listas los elementos
    obtenidos del html.
    ---------------------------------------------------------------- 
    Parámetros:
        - elemento: Elemento html que contiene la información deseada.
    """
    url_uni_no = elemento.find_all('a')
    url_uni_no2 = url_uni_no[0]
    url_uni = url_uni_no2['href']
    lista_urls_uni.append('https://en.wikipedia.org' + url_uni)
    uni = elemento.get_text()
    lista_nomb_uni.append(uni)
    l_alemania.append(nomb_pais)
    l_url_alem.append(url_pais)

def obtener_urls_univers2(datos, nomb_pais):
    """
    ----------------------------------------------------------------
    Explicación: 
    Función que se encarga de realizar el proceso completo de 
    descarga de las diferentes Urls de las universidades del
    país deseado.
    ---------------------------------------------------------------- 
    Parámetros:
        - datos:
        - nomb_pais: Nombre del país deseado
    ---------------------------------------------------------------- 
    Return:
    Nos devuelve una lista con las Url's y los nombres de las 
    universidades del país seleccionado.
    ---------------------------------------------------------------- 
    Limitaciones:
    La posible limitación que se puede observar es el como se escribe 
    el país (por tema idioma) o si el país en cuestión no se encuentra 
    en los datos.
    """
    url_pais = obtener_url_pais2(datos, nomb_pais)
    data4 = descargar_listado_univ_pais(url_pais)
    urls_uni = []
    nombres_univ = []
    pais_ger = []
    url_pais2 = []
    for pais in data4:
        data_no = pais.find_all('li')
        for j in data_no:
            añadir_elem(j,urls_uni, nombres_univ,pais_ger, url_pais2, nomb_pais, url_pais)
    listado_univ_urls = [[pais_ger[i], url_pais2[i], nombres_univ[i], urls_uni[i]] for i in range(len(pais_ger))]
    return listado_univ_urls

guardar_csv(obtener_urls_univers2(listado2, 'Germany'),file_path='./Archivos_Python/Prácticas/data/csv/UnivAlem2.csv' )
