import csv
import json

def guardar_csv(matrix, file_path):
    with open(file_path, 'w') as output_file:
        writer = csv.writer(output_file, delimiter = ';')
        for row in matrix:
            writer.writerow(row)

def anadir_a_csv(matrix, file_path):
    with open(file_path, 'a') as output_file:
        writer = csv.writer(output_file, delimiter = ';')
        for row in matrix:
            writer.writerow(row)

def leer_csv(file_path):
    with open(file_path, 'r') as input_file:
        reader = csv.reader(input_file, delimiter = ";")
        matrix = [row for row in reader]
    return matrix

def leer_json(file_path):
    with open(file_path, 'r') as input_file:
        dic = json.load(input_file)
    return dic

def guardar_json(dic, file_path):
    with open(file_path, 'w') as output_file:
        json.dump(dic, output_file)



