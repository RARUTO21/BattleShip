from tkinter.filedialog import *
from tkinter import *
import random
import threading
import time

nombreJugador = ""
TiempoJuego=0
MatrizUsuario=[['0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0','0']]
MatrizCompu=[]
numeroBarco=1


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
    MatrizCompu.append(linea)
    
def cargarArchivo():
    global tiempo
    global MatrizCompu
    #lista=["Archivo1.txt","Archivo2.txt","Archivo3.txt","Archivo4.txt"]
    #random.shuffle(lista)
   # print (lista[0])
    archivo = open("ricardo.txt", "r")
    tiempo=int(archivo.readline(2))
    
    for linea in archivo.readlines():
        agregar (linea)
    MatrizCompu=MatrizCompu[1:]
    print(MatrizCompu)
   # escribir(matriz)

def Guardar(lista):
    limite = len(lista)
    contador=0
    outfile = open('ricardo.txt', 'w') # Indicamos el valor 'w'.
    outfile.write(str(TiempoJuego))
    outfile.write("\n")
    while (contador<limite):
         columnas=len(lista[0])-1
         contador2=0
         
         while (contador2<columnas):
             outfile.write(str(lista[contador][contador2])+" ")

             contador2=contador2+1
         outfile.write(str(lista[contador][contador2]))
         outfile.write("\n")
         contador=contador+1
    
    outfile.close()
#==========================================================

        
def Cronometro():
    """funcion que realiza el trabajo en el thread"""
    TiempoJuego=0
    while TiempoJuego < 10 :
        contador= contador+1
        time.sleep(1)
        lblCronometro.config(text=str(TiempoJuego))
        
        print (TiempoJuego)
#==========================================================

def PosicionarBarco(x,y,tamaño,orientacion):
   
    if(orientacion=="H"):
        if ((10-y)>=tamaño):
            if(cabe(x,y,tamaño,orientacion)):
                asignar(x,y,tamaño,orientacion)
                return "asignado correctamente"
            else:
                return "error barco no cabe"
        else:
            return "error, no cabe"
    else:
        if((10-x)>=tamaño):
            if(cabe(x,y,tamaño,orientacion)):
                asignar(x,y,tamaño,orientacion)
                
                return "asignado correctamente"
            else:
                return "error barco no cabe"
        else:
            return "error, no cabe"

def cabe(x,y,tamaño,orientacion):
    y2=y
    if(orientacion=="H"):
        contador=0
        while(contador<tamaño):
            if(MatrizUsuario[x][y]=='0'):
                y=y+1
                contador=contador+1
                print(contador)
            else:
                 return False
        
        return bordesH(x,y2,tamaño)
    else:
        x2=x
        contador=0
        while(contador<tamaño):
            if(MatrizUsuario[x][y]=='0'):
                x=x+1
                contador=contador+1
            else:
                return False
        
        return bordesV(x2,y,tamaño)

def bordesH(x,y,tamaño):
    y2=y
    if(x==0):# si es igual que 0 solo valida la linea 2
        vacio=0
        while(vacio<tamaño):
            if(MatrizUsuario[x+1][y]=='0'):
                vacio=vacio+1
                y=y+1
                print("while")
            else:
                return False
        
    elif(x==9): # si es igual que 9 solo valida la 8
        vacio=0
        while(vacio<tamaño):
            if(MatrizUsuario[x-1][y]=='0'):
                vacio=vacio+1
                y=y+1
            else:
                return False
    else:
        vacio=0
        while(vacio<tamaño):
            if(MatrizUsuario[x-1][y]=='0' and MatrizUsuario[x+1][y]=='0'):
                vacio=vacio+1
                y=y+1
            else:
                return False
        
    if(y2==0):
        if(x==0):
            if(MatrizUsuario[x][tamaño]=='0' and MatrizUsuario[x+1][tamaño]=='0'):
                return True
            return False
        elif(x==9):
            if(MatrizUsuario[x][tamaño]=='0' and MatrizUsuario[x-1][tamaño]=='0'):
                return True
            return False
        else:
            if(MatrizUsuario[x][tamaño]=='0' and MatrizUsuario[x-1][tamaño]=='0' and MatrizUsuario[x+1][tamaño]=='0'):
                return True
            return False
    elif(y2==9):
        if(x==0):
            if(MatrizUsuario[x][8]=='0' and MatrizUsuario[x+1][8]=='0'):
                return True
            return False
        elif(x==9):
            if(MatrizUsuario[x][8]=='0' and MatrizUsuario[x-1][8]=='0'):
                return True
            return False
        else:
            if(MatrizUsuario[x][8]=='0' and MatrizUsuario[x-1][8]=='0' and MatrizUsuario[x+1][8]=='0'):
                return True
            return False
    else:
        if(y2+tamaño>9):
            if(MatrizUsuario[x-1][y2-1]=='0' and MatrizUsuario[x][y2]=='0' and MatrizUsuario[x-1][y2+tamaño-1]=='0'):
                return True
        else:
            if(MatrizUsuario[x][y2]=='0' and MatrizUsuario[x][y2-1]=='0' and MatrizUsuario[x][y2+tamaño]=='0' and MatrizUsuario[x-1][y2+tamaño]=='0'and MatrizUsuario[x+1][y2+tamaño]=='0'):
                return True
            
        return False
def bordesV(x,y,tamaño):
    x2=x
    if(y==0):
        vacio=0
        while(vacio<tamaño):
            if(MatrizUsuario[x][y+1]=='0'):
                vacio=vacio+1
                x=x+1
                print("while")
            else:
                return False
        
    elif(y==9):
        vacio=0
        x=x-1
        while(vacio<=tamaño):
            if(MatrizUsuario[x][y-1]=='0'):
                vacio=vacio+1
                x=x+1
            else:
                return False
    else:
        vacio=0
        while(vacio<tamaño):
            if(MatrizUsuario[x][y-1]=='0' and MatrizUsuario[x][y+1]=='0'):
                vacio=vacio+1
                x=x+1
            else:
                return False
        
    if(x2==0):
        print(MatrizUsuario[x][tamaño])
        if(MatrizUsuario[tamaño][y]=='0'):
            return True
        return False
    elif(x2==9):
        if(MatrizUsuario[x2][-(tamaño+1)]=='0'):
            return True
        return False
    else:
        if(x2+tamaño>9):
            if(MatrizUsuario[x2-1][y]=='0' and MatrizUsuario[x2+tamaño-1][y]=='0'):
                return True
        else:
            if(MatrizUsuario[x2-1][y]=='0' and MatrizUsuario[x2-1][y-1]=='0' and MatrizUsuario[x2-1][y+1]=='0' and MatrizUsuario[x2+tamaño][y]=='0'and MatrizUsuario[x2+tamaño][y-1]=='0'and MatrizUsuario[x2+tamaño][y+1]=='0'):
                return True
        return False
        
        
    
    
             


def asignar(x,y,tamaño,orientacion):
    global numeroBarco
    if(orientacion=="H"):
        contador=0
        while(contador<tamaño):
            MatrizUsuario[x][y]=str(numeroBarco)
            y=y+1
            contador=contador+1
            print(contador)
           
    else:
        contador=0
        while(contador<tamaño):
            MatrizUsuario[x][y]=str(numeroBarco)
            x=x+1
            contador=contador+1
    numeroBarco=numeroBarco+1



def pegar(matriz,x,y):
    if(matriz[x][y]=='0'):
        return "agua"
    elif(destruido(matriz,x,y)):
        matriz[x][y]='0'
        return "destruido"
    else:
        matriz[x][y]='0'
        return "pegado"
def destruido(matriz,x,y):
    dato=matriz[x][y]
    numero=0
    filas=10
    columnas=10
    contadorFilas=0
    encontrado=0
    while(contadorFilas<filas):
        contadorColumnas=0
        while(contadorColumnas<columnas):
            if(matriz[contadorFilas][contadorColumnas]==dato):
                encontrado=encontrado+1
            
            contadorColumnas=contadorColumnas+1
        
        contadorFilas=contadorFilas+1
    if(encontrado>1):
        return False
    else:
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





