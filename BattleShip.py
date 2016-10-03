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
        

# ___________ Finalmente ___________

Crono = threading.Thread(target=Cronometro)
Crono.start()
Inicio=threading.Thread(target=iniciar)
Inicio.start()
ventanaPrincipal.mainloop()
Crono.join()
Inicio.join()



