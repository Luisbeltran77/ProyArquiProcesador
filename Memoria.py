class Memoria:
    def __init__(self, listInstrucciones, listDato):
        self.listInstrucciones = listInstrucciones
        self.listDato = listDato

    def leer_archivo(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
            return contenido
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
            return None
    url = leer_archivo("nombre.txt")
    