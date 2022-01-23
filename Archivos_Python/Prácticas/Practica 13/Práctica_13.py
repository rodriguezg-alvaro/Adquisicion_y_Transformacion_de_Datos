import sys
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

if __name__=='__main__':
    arguments=sys.argv

year = arguments[1][:4]
mes = arguments[1][4:6]
dia = arguments[1][6:]

def funcion_descarga(nav,dir):
    """
    ----------------------------------------------------------------
    Explicación: 
    Función que se encarga de descargar los PDF's deseados.
    ---------------------------------------------------------------- 
    Parámetros:
        - nav: El tipo de navegador que se usará
        - dir: Directorio donde se desea guardar los archivos.
    ----------------------------------------------------------------
    Origen:
    https://github.com/SeleniumHQ/selenium/issues/5722
    """
    nav.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': dir}}
    nav.execute("send_command", params)

def descarga_pdf(links):
    """
    ----------------------------------------------------------------
    Explicación: 
    Función que se encarga de descargar los PDF's deseados.
    ---------------------------------------------------------------- 
    Parámetros:
        - links: Lista de los links donde se encuentran nuestros
        PDF's que queremos descargar.
    """
    chromeOptions = webdriver.chrome.options.Options()
    chromeOptions.add_argument("--headless")
    dir = '/Users/alvarorodriguezgonzalez/Documents/Estudios/Master/Master Big Data. Tecnologia y  Analitica Avanzada/1ºC/Adquisicion y transformacion de datos (1ºC)/Profesor/Archivos Python/Archivos_Python/Prácticas/Practica 13/{}/'.format(arguments[1])
    prefs = {'download.default_directory': dir, "plugins.always_open_pdf_externally": True}
    chromeOptions.add_experimental_option("prefs",prefs)
    check = 0 
    for i in links:
        try:
            driver = webdriver.Chrome(executable_path="./Chrome_Driver/chromedriver",chrome_options=chromeOptions)
            driver.get(i)
            apartado = driver.find_elements_by_tag_name("dd")[2].text
            funcion_descarga(driver, dir + apartado)
            pdf_file = driver.find_element_by_xpath("//li[@class='puntoPDF']").click()
            time.sleep(6)
            driver.close()

        except:
            check = 1
            driver.close()
            print('Error en la descarga del archivo')
    
    if check == 0:
            print('Descarga de archivos finalizada con éxito.')

def descarga_links(lista):
    """
    ----------------------------------------------------------------
    Explicación: 
    Función que se encarga de descargar los diferents links donde 
    se encuentran los PDF's deseados
    ---------------------------------------------------------------- 
    Parámetros:
        - lista: Lista que contiene el código html donde se 
        encuentran todos los links
    ----------------------------------------------------------------
    Return: 
    Nos devuelve una lista con los diferentes links donde estan 
    los PDF's que queremos.
    """
    links = []
    urls = lista.find_all("a")
    for i in urls:
        if i.get_text() == "Otros formatos":
            links.append("https://www.boe.es/"+i["href"])
    return links

def proceso_completo(year_f,mes_f,dia_f):
    """
    -----------------------------------------------------------------
    Explicación: 
    Función que se encarga de realizar el proceso completo de entrada
    y descarga de los diferentes PDF's
    -----------------------------------------------------------------
    Parámetros:
        - year_f: Año del boletín deseados
        - mes_f: Mes del boletín deseado
        - dia_f: Día del boletín deseado
    -----------------------------------------------------------------
    Observación:
    La idea de este archivo es que sea ejecutado por consola y que 
    la fecha se lea desde la consola en el siguiente formato:
        20210412 (año,mes,dia)
    """
    # Entramos directamente a la página donde se encuentran los PDF's deseados
    url = "https://www.boe.es/borme/dias/{}/{}/{}/index.php?s=C".format(year_f, mes_f, dia_f)
    response = requests.get(url)

    #Si la respues es un exito (codigo 200), es que hay datos (archivos PDF y XML) para esa fecha. Sino, no los hay
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        lista = soup.find("div", class_="sumario")
        links = descarga_links(lista)
        descarga_pdf(links)
    else:
        print("Datos no disponibles en el BORME para la fecha indicada.")

proceso_completo(year,mes,dia)
