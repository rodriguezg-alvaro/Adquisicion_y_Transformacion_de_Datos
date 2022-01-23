import requests
import keys

##################################
# Observación: Como las keys están en otro archivo .py que no incluyo en el .zip es lógico que no funcione el código
# cuando este se ejecute.
##################################

claves = {
    "api_key": keys.claves["aemet_api_key"]
}

def obtener_idema(lugar):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es sacar el idema del lugar que se 
    desea.
    ----------------------------------------------------------------
    Parámetros:
        - lugar: Localización de donde quieras sacar el idema
    ----------------------------------------------------------------
    Limitaciones:
    Esta función solo es útil para sacar el idema de una 
    única estación.
    """
    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones"
    response = requests.get(url, params = claves)
    if response.json()["estado"] == 200:
        response_data = requests.get(response.json()["datos"],params = claves)
        for elem in (response_data.json()):
            if elem["nombre"] == lugar.upper():
                print("El indicativo de " + lugar + " es " + str(elem["indicativo"]))
    else:
        print('Se ha producido un error en la petición')

obtener_idema("Madrid, Ciudad Universitaria")

fechaIni = '2019-10-01T00:00:00UTC'
fechaFin = '2019-10-30T23:59:59UTC'
estacion = '3194U'

def obtener_clim_dia(fechaIni,fechaFin, estacion):
    """
    ----------------------------------------------------------------
    Explicación: 
    Esta función lo que hace es sacar las climatologias diarias 
    durante el periodo deseado de una estación concreta.
    ----------------------------------------------------------------
    Parámetros:
        - fechaIni: Fecha de inicio del periodo deseado
        - fechaFin: Fecha final del periodo deseado 
        - estacion: Idema de la estación deseada
    ----------------------------------------------------------------
    Limitaciones:
    Esta función solo es útil para sacar la climatología diaria para 
    una única estación.
    """
    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{}/fechafin/{}/estacion/{}"
    response = requests.get(url.format(fechaIni,fechaFin,estacion), params = claves)
    if response.json()["estado"] == 200:
        response_data = requests.get(response.json()["datos"])
        print(response_data.text)
    else: 
        print('Se ha producido un error en la petición')

obtener_clim_dia(fechaIni,fechaFin, estacion)



