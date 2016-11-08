import os.path 
def buscar_max(lista, ini, fin):
    """ Devuelve la posición del máximo elemento en un segmento de
        lista de elementos comparables.
        Se trabaja sobre lista, que no debe ser vacía.
        ini es la posición inicial del segmento, debe ser válida.
        fin es la posición final del segmento, debe ser válida. """
 
    pos_max = ini
    for i in range(ini+1, fin+1):
        if lista[i][1] > lista[pos_max][1]:
            pos_max = i
    return pos_max
listaRecord=[]
def agregarNombreRecord():
    limite=len(listaRecord)
    contador=0
    while(contador<limite):
        if(nombreJugador==listaRecord[contador][0]):
            if(tiempo<=int(listaRecord[contador][1])):
                listaRecord[contador][1]=str(tiempoJuego)
                ord_seleccion(listaRecord)
                print(listaRecord)
                return True
            else:
                contador=contador+1
        else:
            contador=contador+1
    listaRecord.append([nombreJugador,str(tiempoJuego)])
    ord_seleccion(listaRecord)
    print(listaRecord)
def cargarRecord():
    if (existe("puntuaciones.txt")):
        archivo=open("puntuaciones.txt",'r')
        for linea in archivo.readlines():
            elemento=linea.split()
            listaRecord.append(elemento)
    else:
        print("no archivo")

def guardarRecord():
    archivo=open("puntuaciones.txt",'w')
    limite=len(listaRecord)
    contador=0
    while(contador<limite):
        archivo.write(str(listaRecord[contador][0])+" "+listaRecord[contador][1])
        archivo.write("\n")
        contador=contador+1

def existe(archivo):
    if os.path.exists(archivo):
        return True
    else:
        return False
