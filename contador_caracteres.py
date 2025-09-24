import unicodedata, operator
from os import strerror

def eliminar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

nombre_archivo = input("Escribe el nombre del archivo de texto a analizar: ")
#Creamos diccionario ordenando por nº de ocurrencias todos los caracteres del texto:
try:
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        data = archivo.read()

    data = eliminar_tildes(data.lower())

    dicc = {}
   
    for ch in data:
        if 'a' <= ch <= 'z':
            dicc[ch] = dicc.get(ch, 0) + 1
    
    for letra, valor in sorted(dicc.items(), key=operator.itemgetter(1), reverse = True):
        print(letra, '->', valor)
    
except IOError as e:
    print("No se ha podido acceder al archivo:", strerror(e.errno))
    exit(e.errno)
#Creamos archivo que contenga dicho historial de ocurrencias de los caracteres del texto:
try:
    with open(nombre_archivo + '.hist', 'wt') as hist:
        for key, value in sorted(dicc.items(), key=operator.itemgetter(1), reverse = True):
            hist.write(key + " -> " + str(value) + "\n")
except Exception as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)


