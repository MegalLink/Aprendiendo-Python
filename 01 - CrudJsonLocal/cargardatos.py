import json
def imprimir_cancion(cancion_seleccionada):
    print(f"""
    Cancion seleccionada:
    Id :{cancion_seleccionada['index']})
    Nombre :{cancion_seleccionada['nombre_cancion']}
    Autor/Banda :{cancion_seleccionada['autor_cancion']}
    Genero :{cancion_seleccionada['genero']}
    Acordes :{cancion_seleccionada['acordes']}

    """) 
def set_cancion(index):
    
    print("Ingrese el nombre de la canción")
    nombre_cancion=input()
    print("Ingrese el autor de la cancion")
    autor_cancion=input()
    print("Ingrese el genero o generos de la cancion")
    genero=input()
    print("Ingrese las canciones separadas por una coma (,)")
    acordes_string=input()
    acordes=acordes_string.split(",")
    cancion_nueva = {'index' : index, 'nombre_cancion' : nombre_cancion,'autor_cancion':autor_cancion,'genero': genero,'acordes': acordes }
    return cancion_nueva
def last_index():
    canciones=cargar_datos()
    l_index=canciones[-1]['index']
    return l_index
def guardar_datos(canciones):
    try:
        path="./01 - Deber/datos.json"
        archivo_abierto=open(path,'w')
        lineas=json.dump(canciones,archivo_abierto)
        print("Cancion agregada")
    except:
        print("Error leyendo archivo")


def cargar_datos():
    try:
        path="./01 - Deber/datos.json"
        archivo_abierto=open(path,'r')
        lineas=json.loads(archivo_abierto.read())
        archivo_abierto.close
        return lineas
    except:
        print("Error leyendo archivo")
    
def seleccionar_cancion(id):
    try:
        path="./01 - Deber/datos.json"
        archivo_abierto=open(path,'r')
        lineas=json.loads(archivo_abierto.read())
        archivo_abierto.close
        return lineas[id]
    except:
        print("Error leyendo archivo")

def menu_principal():
    print("Menu principal")
    print("Porfavor seleccione una opción");
    print("""
    [L]istar canciones
    [A]gregar cancion
    [E]scoger cancion
    [S]alir
    """)
    eleccion=input().upper()
    def listar_canciones():
        lista=cargar_datos()
        print("Lista de canciones:")
        for cancion in lista:
            print(f"{cancion['index']}) {cancion['nombre_cancion']} - {cancion['autor_cancion']} ")
        
        return menu_principal()
    def agregar_cancion():
        lista=cargar_datos()
        
        cancion_nueva = set_cancion(int(last_index()+1))
        lista.append(cancion_nueva)
        guardar_datos(lista)
        return listar_canciones()
    def escoger_cancion():
        print("Ingrese el id de la cancion que desea seleccionar")
        id=int(input())
        cancion_seleccionada=seleccionar_cancion(id) 
        
        return menu_cancion(cancion_seleccionada)
    def salir():
        return print("salir")
    def devolver_respuesta():
        opciones={
            "L":listar_canciones,
            "A":agregar_cancion,
            "E":escoger_cancion,
            "S":salir
        }
        return opciones[eleccion]()
    return devolver_respuesta()
def menu_cancion(cancion):
    imprimir_cancion(cancion)
    print("Menu canción:")
    print("Porfavor seleccione una opción");
    print("""
    [E]eliminar cancion
    [M]odificar cancion
    [V]olver menu principal""")
    eleccion=input().upper()
    def eliminar_cancion():
        print("Esta seguro que desa eliminar la canción? (S/N)")
        confirmar=input().upper()
        if confirmar == "S":
            index=cancion['index']
            lista=cargar_datos();
            lista.pop(index)
            guardar_datos(lista);
        return menu_principal()
    def modificar_cancion():
        lista=cargar_datos()
        index=cancion['index']
        cancion_modificar=set_cancion(int(index))
        lista[index]=cancion_modificar
        guardar_datos(lista)
        return menu_principal()

    def editar_acordes():
        lista=cargar_datos()
        index=cancion['index']
        cancion_modificar=set_acordes(int(index),cancion)
        lista[index]=cancion_modificar
        guardar_datos(lista)
        return menu_cancion(cancion_modificar)
    def eliminar_acordes():
        lista=cargar_datos()
        index=cancion['index']
        cancion_modificar=set_eliminar_acordes(int(index),cancion)
        lista[index]=cancion_modificar
        guardar_datos(lista)
        return menu_cancion(cancion_modificar)


    def volver_al_menu():
        return menu_principal()
    def devolver_respuesta():
        opciones_cancion={
            "E":eliminar_cancion,
            "M":modificar_cancion,  
            "V":volver_al_menu          
        }
        return opciones_cancion[eleccion]()
    return devolver_respuesta()

menu_principal()
