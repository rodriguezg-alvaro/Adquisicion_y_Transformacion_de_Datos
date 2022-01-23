import time
import csv
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from utilities import guardar_csv

driver = webdriver.Chrome(executable_path="./Archivos_Python/Prácticas/Chrome_Driver/chromedriver")

def entrar_pag(postal_code):
    url = 'https://comparador.cnmc.gob.es'
    driver.get(url=url)
    time.sleep(2)
    cookies = driver.find_element_by_xpath('//*[@id="cookiesSize"]/div[2]/button[1]')
    cookies.click()
    time.sleep(2)
    dropdown = driver.find_element_by_xpath('//*[@id="principal"]/div/form/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div/i')
    dropdown.click()
    time.sleep(2)
    electr = driver.find_element_by_xpath('//*[@id="list-item-53-0"]/div/div')
    electr.click()
    time.sleep(2)
    iniciar = driver.find_element_by_xpath('//*[@id="Iniciar"]/span')
    iniciar.click()
    time.sleep(2)
    input_field = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/main/div/div/div/form/div/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/input')
    input_field.send_keys(postal_code)
    time.sleep(2)
    continuar = driver.find_element_by_xpath('//*[@id="Continuar"]/span')
    continuar.click()
    return 'Todo bien'

def obt_cab():
    cabecera = []
    c1 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/section/div/div/div/div[1]/span[1]')
    cabecera.append(c1.text)
    c2 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/section/div/div/div/div[2]/span[1]')
    cabecera.append(c2.text)
    c3 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/section/div/div/div/div[3]/span[1]')
    cabecera.append(c3.text)
    c4 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/section/div/div/div/div[9]/span[1]')
    cabecera.append(c4.text)
    c5 = driver.find_element_by_xpath('//*[@id="listadoOfertas"]/div/table/thead/tr/th[1]/span')
    cabecera.append(c5.text)
    c6 = driver.find_element_by_xpath('//*[@id="listadoOfertas"]/div/table/thead/tr/th[2]/span')
    cabecera.append(c6.text)
    c7 = driver.find_element_by_xpath('//*[@id="listadoOfertas"]/div/table/thead/tr/th[3]/span')
    cabecera.append(c7.text)
    c8 = driver.find_element_by_xpath('//*[@id="listadoOfertas"]/div/table/thead/tr/th[4]/span')
    cabecera.append(c8.text)
    c9 = driver.find_element_by_xpath('//*[@id="listadoOfertas"]/div/table/thead/tr/th[5]/span')
    cabecera.append(c9.text)
    c10 = driver.find_element_by_xpath('//*[@id="listadoOfertas"]/div/table/thead/tr/th[6]/span[1]')
    cabecera.append(c10.text)
    c11 = driver.find_element_by_xpath('//*[@id="listadoOfertas"]/div/table/thead/tr/th[7]/span[1]')
    cabecera.append(c11.text)
    c12 = driver.find_element_by_xpath('//*[@id="listadoOfertas"]/div/table/thead/tr/th[8]/span[1]')
    cabecera.append(c12.text)
    cabecera.append('URL ' + c6.text)
    return cabecera

def obt_datos():
    datos = []
    d1 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/section/div/div/div/div[1]/span[2]')
    d2 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/section/div/div/div/div[2]/span[2]')
    d3 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/section/div/div/div/div[3]/span[2]')
    d4 = driver.find_element_by_xpath('//*[@id="app"]/div[1]/main/div/section/div/div/div/div[9]/span[2]')
    items = driver.find_elements_by_tag_name('tr')
    for i in range(4,len(items)):
        caso = []
        caso.append(d1.text)
        caso.append(d2.text)
        caso.append(d3.text)
        caso.append(d4.text)
        caso.append(items[i].text)
        caso.append(items[i].get_attribute('href'))
        datos.append(caso)
    return datos

def obt_cabecera_datos(postal_code):
    entrar_pag(postal_code)
    time.sleep(6)
    cabecera = obt_cab()
    datos = obt_datos()
    return (cabecera,datos)

def obt_todo(postal_code):
   lista_csv = []
   cabecera = obt_cabecera_datos(postal_code)
   lista_csv.append(cabecera[0])
   for dato in cabecera[1]:
       lista_csv.append(dato)
   return lista_csv

def datos_csv(postal_code):
    lista_csv = obt_todo(postal_code)
    guardar_csv(lista_csv, './Archivos_Python/Prácticas/data/csv/Práctica12.csv')

datos_csv('45000')

