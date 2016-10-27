from tkinter.filedialog import *
from tkinter import *
import random
import threading
import time
matriz=[]# para guardar los datos cuando se cargue el archivo
nombreJugador = ""


def iniciar():
        #ventanaPrincipal.withdraw()
        None


#Configuracion de la ventana principal
ventanaPrincipal = Tk()
ventanaPrincipal.title("BattleShip")
ventanaPrincipal.geometry("1280x768")
ventanaPrincipal.config(bg="gray25")
ventanaPrincipal.resizable(0,0)


#=====================================

#               TopLevels
tpIngreseNombre = Toplevel()
tpIngreseNombre.title("Ingrese el nombre")
tpIngreseNombre.config(bg="black")
tpIngreseNombre.resizable(0,0)
tpIngreseNombre.protocol("WM_DELETE_WINDOW",iniciar)#falta conectar bien la f:iniciar()

#=====================================TopLevels


#                       Imagenes
fondoPrincipal = PhotoImage(file = "Images/Battleship.gif")

#===========================================================Imagenes



#                 Labels
lblFondoVentanaPrincipal = Label(ventanaPrincipal,image=fondoPrincipal,bg="black")
lblFondoVentanaPrincipal.place(x=0,y=0)
lblCronometro=Label(height=3,width=10,bg="white")
lblCronometro.place(x=10,y=10)
#===========================================================Labels



#               Botones


#==========================================================Botones
#==========================================================Archivos
def agregar(linea):
    linea= linea.split()
    #validar que los datos de la matriz sean los que queremos
    matriz.append(linea)
    
def cargarArchivo():
  # hay que crear los archivos xD pero la vara si agarra las cosas de un archivo
    lista=["Archivo1.txt","Archivo2.txt","Archivo3.txt","Archivo4.txt"]
    random.shuffle(lista)
    archivo = open(lista[0], "r")
    for linea in archivo.readlines():
        agregar (linea)
    print (matriz)
#==========================================================
#==========================================================Archivos
def agregar(linea):
    linea= linea.split()
    #validar que los datos de la matriz sean los que queremos
    matriz.append(linea)
    
def cargarArchivo():
  # hay que crear los archivos xD pero la vara si agarra las cosas de un archivo
    lista=["Archivo1.txt","Archivo2.txt","Archivo3.txt","Archivo4.txt"]
    random.shuffle(lista)
    archivo = open(lista[0], "r")
    for linea in archivo.readlines():
        agregar (linea)
    print (matriz)
#==========================================================

        
def Cronometro():
    """funcion que realiza el trabajo en el thread"""
    contador=0
    while contador < 10 :
        contador= contador+1
        time.sleep(1)
        lblCronometro.config(text=str(contador))
        
        print (contador)
#==========================================================

def PosicionarBarco(x,y,tamaño,orientacion):
   
    if(orientacion=="H"):
        if ((10-y)>=tamaño):#pregunta si el barco cabe en el limite Horizontal
            if(cabe(x,y,tamaño,orientacion)):#si el barco cabe sin chocar con otro lo asigna
                asignar(x,y,tamaño,orientacion)
                return "asignado correctamente"
            else:
                return "error barco no cabe"
        else:
            return "error, no cabe"
    else:
        if((10-x)>=tamaño):#pregunta si el barco cabe en el limite vertical
            if(cabe(x,y,tamaño,orientacion)):#si el barco cabe sin chocar con otro lo asigna
                asignar(x,y,tamaño,orientacion)
                
                return "asignado correctamente"
            else:
                return "error barco no cabe"
        else:
            return "error, no cabe"

def cabe(x,y,tamaño,orientacion):
    if(orientacion=="H"):
        contador=0#busca en la matriz X=tamaño cantidad de lugares disponibles para asignar Horizontal
        while(contador<tamaño):
            if(matriz[x][y]=='0'):
                y=y+1#si encuentra agua entonces sigue sigue buscando disponible
                contador=contador+1
                print(contador)
            else:#si encontró uno ocupado entonces sale del ciclo
                break
        if(contador==tamaño):
            return True# si termina el ciclo es porque hay campo para asignar y devuelve True
        else:# si no hay campo devuelve False
            return False
    else:
        contador=0#busca en la matriz X=tamaño cantidad de lugares disponibles para asignar Vertical
        while(contador<tamaño):
            if(matriz[x][y]=='0'):
                x=x+1#si encuentra agua entonces sigue sigue buscando disponible
                contador=contador+1
            else:
                break#si encontró uno ocupado entonces sale del ciclo
        if(contador==tamaño):
            return True# si termina el ciclo es porque hay campo para asignar y devuelve True
        else:# si no hay campo devuelve False
            return False

def asignar(x,y,tamaño,orientacion):
    global numeroBarco
    if(orientacion=="H"):
        contador=0
        while(contador<tamaño):#asigna los lugares x,y desde el punto establecido hasta el tamaño del barco horizontal
            matriz[x][y]=str(numeroBarco)
            y=y+1
            contador=contador+1
            print(contador)
           
    else:
        contador=0
        while(contador<tamaño):#asigna los lugares x,y desde el punto establecido hasta el tamaño del barco vertical
            matriz[x][y]=str(numeroBarco)
            x=x+1
            contador=contador+1
    numeroBarco=numeroBarco+1#aumenta el numero de barcos ya que al asignarlos se les pone el numero de barco por el cual va este contador



def pegar(matriz,x,y):
    if(matriz[x][y]=='0'):#si le pega a un 0 es agua
        return "agua"
    elif(destruido(matriz,x,y)):#si destruye el barco pone un 0 en esa posición e indica que ha sido destruido
        matriz[x][y]='0'
        return "destruido"
    else:
        matriz[x][y]='0'# si solo pega al barco indica que ha sudo pegado y pone un 0 en esa posicion
        return "pegado"
def destruido(matriz,x,y):
    dato=matriz[x][y]
    numero=0
    filas=10
    columnas=10
    contadorFilas=0
    encontrado=0
    while(contadorFilas<filas):#revisa toda la matriz en busca de un numero igual al de barco acertado
        contadorColumnas=0
        while(contadorColumnas<columnas):
            if(matriz[contadorFilas][contadorColumnas]==dato):
                encontrado=encontrado+1#si lo encuentra suma 1 a encontrados
            
            contadorColumnas=contadorColumnas+1
        
        contadorFilas=contadorFilas+1
    if(encontrado>1):# si encuentra mas de 1 entonces el barco no ha sido destruido
        return False
    else:# si encuentra 1 lo destruye
        return True
        
#==========================================================

# ___________ Finalmente ___________

Crono = threading.Thread(target=Cronometro)
Crono.start()
Inicio=threading.Thread(target=iniciar)
Inicio.start()
ventanaPrincipal.mainloop()
Crono.join()
Inicio.join()



