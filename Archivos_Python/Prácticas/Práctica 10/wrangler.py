from utilities import leer_csv, leer_json

listado_spider = leer_csv(file_path='./Archivos_Python/Prácticas/data/csv/Práctica10Univ.csv')
listado_scraper = leer_json(file_path='./Archivos_Python/Prácticas/data/json/Práctica10Fin.json')
long_spider = len([t[0] for t in listado_spider])
long_scraper = len([t[0] for t in listado_scraper])

if long_scraper == long_spider:
    print('Ok')
else:
    print('Algo pasa')