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
    global TiempoJuego
    while TiempoJuego < 10 :
        TiempoJuego= TiempoJuego+1
        time.sleep(1)
        lblCronometro.config(text=str(TiempoJuego))
        
        print (TiempoJuego)
#==========================================================

def PosicionarBarco(x,y,tamaño,orientacion):
   
    if(orientacion=="H"):
        if ((10-y)>=tamaño):#pregunta si el tamaño del barco cabe en posición horizontal
            if(cabe(x,y,tamaño,orientacion)):#si cabe en horizontal pregunta si otro barco impide su colocación
                asignar(x,y,tamaño,orientacion)#si no la impide, es asiganado un nuervo barco
                return "asignado correctamente"
            else:
                return "error barco no cabe"
        else:
            return "error, no cabe"
    else:
        if((10-x)>=tamaño):#pregunta si el tamaño del barco cabe en posición vertical
            if(cabe(x,y,tamaño,orientacion)):#si cabe en horizontal pregunta si otro barco impide su colocación
                asignar(x,y,tamaño,orientacion)#si no la impide, es asiganado un nuervo barco
                
                return "asignado correctamente"
            else:
                return "error barco no cabe"
        else:
            return "error, no cabe"

def cabe(x,y,tamaño,orientacion):
    y2=y
    if(orientacion=="H"):# si el barco es horizontal se recorre las filas de la matriz viendo si no hay un barco existente que estorbe en la colocación del nuevo
        contador=0
        while(contador<tamaño):
            if(MatrizUsuario[x][y]=='0'):
                y=y+1
                contador=contador+1
                print(contador)
            else:# si lo encontrado no es un 0(agua) entonces se retorna false
                 return False
        # si habia solo agua, se llama a una función que se fija si hay limite de agua que impida su colocación
        return bordesH(x,y2,tamaño)
    else:# si el barco es vertical se recorre las columnas de la matriz viendo si no hay un barco que impida la colocación del nuevo
        x2=x
        contador=0
        while(contador<tamaño):
            if(MatrizUsuario[x][y]=='0'):
                x=x+1
                contador=contador+1
            else:
                # si lo encontrado no es un 0(agua) entonces se retorna false
                return False
        # si habia solo agua, se llama a una función que se fija si hay limite de agua que impida su colocación
        return bordesV(x2,y,tamaño)

def bordesH(x,y,tamaño):#esta funcion revisa todos los casos en los cuales los se pueden dar los bordes del agua en un barco
    y2=y
    if(x==0):# si es igual que 0 solo valida la fila1 ya el barco está situado en la 0
        vacio=0#variable que recorre la matriz solo la cantidad de veces que el tamaño lo indica
        while(vacio<tamaño):
            if(MatrizUsuario[x+1][y]=='0'):# si es agua entonces no hay problema pues el limite se respeta
                vacio=vacio+1
                y=y+1
               
            else:# si no retorna falso
                return False
        
    elif(x==9): # si es igual que 9 solo valida la fila 8
        vacio=0#variable que recorre la matriz solo la cantidad de veces que el tamaño lo indica
        while(vacio<tamaño):
            if(MatrizUsuario[x-1][y]=='0'):# si es agua entonces no hay problema pues el limite se respeta
                vacio=vacio+1
                y=y+1
            else:# si no, retorna falso
                return False
    else:# si no es 0 o 9 entonces debe revisar tanto la fila anterior como la fila superior
        vacio=0
        while(vacio<tamaño):
            if(MatrizUsuario[x-1][y]=='0' and MatrizUsuario[x+1][y]=='0'):# pregunta si tanto la superior como la inferior son 0
                vacio=vacio+1
                y=y+1
            else: # si no lo es retorna false
                return False
        
    if(y2==0):#pregunta si la posición y es 0 entonces solo debe revisar un limite, ya sea el inferior o superior
        if(x==0):
            if(MatrizUsuario[x][tamaño]=='0' and MatrizUsuario[x+1][tamaño]=='0'):# pregunta si la fila de 0 en tamaño y la fila 1 en tamaño son 0 para ver las diagonales en el agua
                return True
            return False
        elif(x==9):
            if(MatrizUsuario[x][tamaño]=='0' and MatrizUsuario[x-1][tamaño]=='0'):# pregunta si la fila de 9 en tamaño y la fila 1 en tamaño son 8 para ver las diagonales en el agua
                return True
            return False
        else:
            if(MatrizUsuario[x][tamaño]=='0' and MatrizUsuario[x-1][tamaño]=='0' and MatrizUsuario[x+1][tamaño]=='0'):# si está en cualquier otra fila entonces debe ver tanto la diagonal anterior como la superior
                return True
            return False
    elif(y2==9):
        if(x==0):
            if(MatrizUsuario[x][8]=='0' and MatrizUsuario[x+1][8]=='0'):#hace lo mismo que anterior pero buscando limites izquierdos
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
        while(vacio<tamaño):# recorre la matriz hacia abajo para buscar si en la columna 1 solo hay 0
            if(MatrizUsuario[x][y+1]=='0'):
                vacio=vacio+1
                x=x+1
                print("while")
            else:
                return False
        
    elif(y==9):
        vacio=0
        x=x-1# recorre la matriz hacia abajo para buscar si en la columna 8 solo hay 0
        while(vacio<=tamaño):
            if(MatrizUsuario[x][y-1]=='0'):
                vacio=vacio+1
                x=x+1
            else:
                return False
    else:
        vacio=0
        while(vacio<tamaño):# recorre la columna Y-1 y Y+1 para ver si a los lados del barco solo hay agua
            if(MatrizUsuario[x][y-1]=='0' and MatrizUsuario[x][y+1]=='0'):
                vacio=vacio+1
                x=x+1
            else:
                return False
        
    if(x2==0):
        print(MatrizUsuario[x][tamaño])# si la x es 0 entonces solo revisa el limite inferior
        if(MatrizUsuario[tamaño][y]=='0'):
            return True
        return False
    elif(x2==9):# si la x es 9 entonces solo revisa el limite superior
        if(MatrizUsuario[x2][-(tamaño+1)]=='0'):
            return True
        return False
    else:
        if(x2+tamaño>9):#revisa que no se salga de la matriz para la validación y revisa arriba y abajo (ver si entra xD)
            if(MatrizUsuario[x2-1][y]=='0' and MatrizUsuario[x2+tamaño-1][y]=='0'):
                return True
        else: # revisa todo 
            if(MatrizUsuario[x2-1][y]=='0' and MatrizUsuario[x2-1][y-1]=='0' and MatrizUsuario[x2-1][y+1]=='0' and MatrizUsuario[x2+tamaño][y]=='0'and MatrizUsuario[x2+tamaño][y-1]=='0'and MatrizUsuario[x2+tamaño][y+1]=='0'):
                return True
        return False
        
        
    
    
             


def asignar(x,y,tamaño,orientacion):
    global numeroBarco
    if(orientacion=="H"):
        contador=0
        while(contador<tamaño):
            MatrizUsuario[x][y]=str(numeroBarco)#recorre la matriz horizontalmente y le asigna a cada balor el numero de barco por el que se va
            y=y+1
            contador=contador+1
            print(contador)
           
    else:
        contador=0
        while(contador<tamaño):
            MatrizUsuario[x][y]=str(numeroBarco)#recorre la matriz verticalmente y le asigna a cada balor el numero de barco por el que se va
            x=x+1
            contador=contador+1
    numeroBarco=numeroBarco+1



def pegar(matriz,x,y):
    if(matriz[x][y]=='0'):# si pega un0 es agua
        return "agua"
    elif(destruido(matriz,x,y)and matriz[x][y]!='-1'):# si el barco es destruido lo marca como tal y devuelve "destruido"
        matriz[x][y]='x'
        return "destruido"
    elif (matriz[x][y]=='-1'):
            return "pego uno que ya habia golpeado antes"
    else:
        matriz[x][y]='-1'# si no lo destruye y no pega agua lo marco como pegado y devuelve "pegado"
        return "pegado"
def destruido(matriz,x,y):
    dato=matriz[x][y]# toma el numero de barco al cual se le está pegando y lo asigna a dato
    numero=0
    filas=10
    columnas=10
    contadorFilas=0
    encontrado=0
    while(contadorFilas<filas):#recorre la matriz, si no hay un numero igual al dato, es por que ha sido destruido el bardo y retorna true, si hay entonces no ha sido destruido, solo golpeado
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
''' Prueba de Barcos
cargarArchivo()
#print(pegar(8,1))
#print(pegar(9,1))
print(PosicionarBarco(0,0,4,"H"))
print(PosicionarBarco(0,7,2,"H"))
print(PosicionarBarco(0,9,1,"H"))
print(PosicionarBarco(1,0,4,"H"))
print(PosicionarBarco(2,0,4,"H"))
print(PosicionarBarco(2,5,4,"H"))
print(PosicionarBarco(4,8,1,"V"))
print(PosicionarBarco(6,4,2,"V"))
print(PosicionarBarco(9,0,4,"H"))
print(PosicionarBarco(9,8,2,"H"))
print(PosicionarBarco(6,7,2,"V"))
print(PosicionarBarco(5,2,6,"V"))
#print(tiempo)

print(MatrizCompu)
print(len(MatrizCompu))
print(pegar(MatrizUsuario,0,5))
print(pegar(MatrizUsuario,0,8))
print(pegar(MatrizUsuario,0,8))
print(pegar(MatrizUsuario,0,7))
Guardar(MatrizUsuario)
x=0
while(x<10):
    print(MatrizUsuario[x])
    x=x+1
print("numero barco "+str(numeroBarco))
'''



