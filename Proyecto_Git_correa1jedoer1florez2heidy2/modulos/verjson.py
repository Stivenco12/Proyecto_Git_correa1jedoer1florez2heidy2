import json 
def cargar_datos(ruta):
    with open(ruta) as contenido:
        informacion=json.load(contenido)
        print(informacion)
        
