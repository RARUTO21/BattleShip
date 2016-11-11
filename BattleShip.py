from tkinter.filedialog import *
from tkinter import *
from tkinter import ttk
from random import randint
import random
import threading
import time
import math
import os.path
import copy

#===================================================

#  VARIABLES DE USO GLOBAL 
nombreJugador = ""
TiempoJuego=0
listaRecord = []
turno = True
ganador = False
nombreGanador = ""
cantBarcos = [None,4,3,2,1]
MatrizUsuario=[ ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0'],
                ['0','0','0','0','0','0','0','0','0','0']]

MatrizUsuario2 = []
matrizCompu =   []
matrizCopiaUsuario = []
matrizCopiaCompu = []
numeroBarco=1
#===================================================

#Funcion que esconde desde el inicio del programa las demas ventanas para que solo se vea la del menu
def iniciar():
        ventanaPonerBarcos.withdraw()
        ventanaJuego.withdraw()
        ventanaRecords.withdraw()
        
#Configuracion de la ventana principal de menu
ventanaMenu = Tk()
ventanaMenu.title("Battleship")
ventanaMenu.geometry("1280x768")
ventanaMenu.config(bg="gray25")
ventanaMenu.resizable(0,0)

#Configuracion de la ventana de nueva partida donde se ponen los barcos
ventanaPonerBarcos = Tk()
ventanaPonerBarcos.title("Juego Nuevo")
ventanaPonerBarcos.geometry("1280x768")
ventanaPonerBarcos.config(bg="dodgerBlue3")
ventanaPonerBarcos.resizable(0,0)
#=====================================


# Configuracion de la ventana del juego que almacenara la matriz de botones
ventanaJuego = Toplevel()
ventanaJuego.title("Juego")
ventanaJuego.config(bg="gray25")
ventanaJuego.resizable(0,0)

# Configuracion de la ventana de registro de los puntajes de los jugadores
ventanaRecords = Toplevel()
ventanaRecords.title("Puntajes")
ventanaRecords.config(bg="white")
ventanaRecords.resizable(0,0)
ventanaRecords.wm_geometry("1066x650")
#=====================================TopLevels

# Frame: Contenedor tipo panel que puede albergar objetos. Se usara para almacenar los botones de las matrices del juego
frameVentanaJuego = Frame(ventanaJuego,bg="black",bd=0)
frameVentanaJuego.pack()
#=======================================


def ord_seleccion(lista):
    """ Ordena una lista de elementos según el método de selección.
        Pre: los elementos de la lista deben ser comparables.
        Post: la lista está ordenada. """
 
    # n = posicion final del segmento a tratar, comienza en len(lista)-1*
    n = len(lista)-1
 
    # cicla mientras haya elementos para ordenar (2 o más elementos)
    
    while n > 0:
        # p es la posicion del mayor valor del segmento
        p = buscar_max(lista, 0, n)
 
        # intercambia el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
 
   
        # reduce el segmento en 1
        n = n - 1
 
def buscar_max(lista, ini, fin):
    """ Devuelve la posición del máximo elemento en un segmento de
        lista de elementos comparables.
        Se trabaja sobre lista, que no debe ser vacía.
        ini es la posición inicial del segmento, debe ser válida.
        fin es la posición final del segmento, debe ser válida. """
 
    pos_max = ini
    for i in range(ini+1, fin+1):
        print(lista[i][1])
        print(lista[pos_max][1])
        if int(lista[i][1]) > int(lista[pos_max][1]):
            pos_max = i
    return pos_max

def agregarNombreRecord():
    global listaRecord
    limite=len(listaRecord)
    contador=0
    while(contador<limite):
      
        if(nombreJugador==listaRecord[contador][0]):# pregunta si el nombre es igual al que se encuentra en la lista de records
            
            if(TiempoJuego<=int(listaRecord[contador][1])):# si el tiempo es menor al que ya existe
             
                listaRecord[contador][1]=str(TiempoJuego)# cambio el tiempo por el nuevo
                ord_seleccion(listaRecord)
       
                return True # returna true si logra hacer el cambio
            else:
                return False# false si el record actual es mejor
        else:
            contador=contador+1
   

    listaRecord.append([nombreJugador,str(TiempoJuego)])# se agrega si es un jugador nuevo
    
    ord_seleccion(listaRecord)

    return True
    
def cargarRecord():
    global listaRecord
    nuevosRecord=[]
    if (existe("puntuaciones.txt")):
        archivo=open("puntuaciones.txt",'r')# se carga de un archivo las puntuaciones
        for linea in archivo.readlines():
            elemento=linea.split() # se separan pues se lee la linea corrida del archivo
            nuevosRecord.append(elemento)# se agrega
    else:
        return ("no archivo")# no existe el archivo
    
    listaRecord=nuevosRecord
    print(listaRecord)
    ord_seleccion(listaRecord)
    print(listaRecord)
    print("aqui estoy")

def guardarRecord():
    archivo=open("puntuaciones.txt",'w')# se guardan los records
    limite=len(listaRecord)
    contador=0
    while(contador<limite):# se guardan todos los elementos de la lista de records en el archivo de puntuaciones
        archivo.write(str(listaRecord[contador][0])+" "+listaRecord[contador][1])
        archivo.write("\n")
        contador=contador+1

def existe(archivo):# pregunta si una archivo existe o no
    if os.path.exists(archivo):
        return True
    else:
        return False


# Cargamos de una vez en la variable global 'listaRecord' lo que hay en el archivo de puntajes, en forma de lista de sublistas.
cargarRecord()

# Este objeto es una especie de tabla que puede modelar columnas e introducir elementos, se usa para ver la lista de puntajes
tablaPuntaje = ttk.Treeview(ventanaRecords, height=36, columns=('Nombre del Jugador', 'Tiempo logrado'))
tablaPuntaje["columns"] = ("Posicion","Nombre del Jugador","Tiempo logrado")
tablaPuntaje.column("Posicion")
tablaPuntaje.heading('#0', text='Posicion', anchor=CENTER)
tablaPuntaje.column("Nombre del Jugador")
tablaPuntaje.heading('#1', text='Nombre del Jugador', anchor=CENTER)
tablaPuntaje.column("Tiempo logrado")
tablaPuntaje.heading('#2', text='Tiempo logrado', anchor=CENTER)
#======================================================================================================

# Escribe en la tabla de puntajes cada elemento que hay en el archivo 'puntajes.txt'
def escribirPuntajes():
        tablaPuntaje.delete(*tablaPuntaje.get_children())
        ord_seleccion(listaRecord)
        for i in range(0,len(listaRecord)):
                h = eval(listaRecord[i][1]) // 3600
                m = eval(listaRecord[i][1]) // 60
                s = eval(listaRecord[i][1]) %  60
                t = str(h) + ":" + str(m) + ":" + str(s)
                tablaPuntaje.insert("" ,i,text=str(i+1),values=(listaRecord[i][0],t))
        
# Colocamos de una vez la tabla con los puntajes actuales del juego
tablaPuntaje.place(x=0,y=0)

#=====================================Frames

#       Acciones de interfaz
# En el menu, al seleccionar "Cerrar Programa" se llamara a la siguiente funcioon
def cerrarPrograma():
        if messagebox.askyesno("Salir","Está seguro que desea salir?"):
                ventanaJuego.destroy()

# Tira una bomba en una posicion (x,y) de la matriz deseada
def tirarBomba(matriz,x,y,botones,jugador):
    pegar(matriz,x,y)
    if jugador: #Verifica si el turno es del jugador
        crearMatrizBotonesJ()
    else:
        crearMatrizBotonesC()


def refrescarBoton(matriz,x,y,botones,jugador): #NO SIRVIO (LASTIMA) Se supone que no habria que crear toda una matriz de botones sino solo refrescar donde se jugo
    btn = 0
    if jugador:
        if matriz[x][y] == "0":
            btn = Button(frameVentanaJuego,image = cuadroCeleste,background="blue3",activebackground="blue",state=DISABLED)
        elif matriz[x][y] == "-1":
            btn = Button(frameVentanaJuego,image = tocado,background="blue3",activebackground="blue",state=DISABLED)
        elif matriz[x][y] == "X":
            btn = Button(frameVentanaJuego,image = derribado,background="blue3",activebackground="blue",state=DISABLED)
        elif matriz[x][y] == "A":
            btn = Button(frameVentanaJuego,image = agua,background="blue3",activebackground="blue",state=DISABLED)
        else:
            btn = Button(frameVentanaJuego,image = barco,background="blue3",activebackground="blue",state=DISABLED)
        btn.grid(row=x+1, column=y+1)
    else:
        if matriz[x][y] == "0":
            btn = Button(frameVentanaJuego,image = cuadroCeleste,background="blue3",activebackground="blue",state=DISABLED)
        elif matriz[x][y] == "-1":
            btn = Button(frameVentanaJuego,image = tocado,background="blue3",activebackground="blue",state=DISABLED)
        elif matriz[x][y] == "X":
            btn = Button(frameVentanaJuego,image = derribado,background="blue3",activebackground="blue",state=DISABLED)
        elif matriz[x][y] == "A":
            btn = Button(frameVentanaJuego,image = agua,background="blue3",activebackground="blue",state=DISABLED)
        btn.grid(row=x-10,column=y+1)
    botones[x][y] = btn
        
#==========================================================Acciones de interfaz


# Opcion del menu donde se guarda el estado de la partida actual y se sale al menu
def salvarYSalir():
        global MatrizUsuario2
        global MatrizUsuario
        global matrizCompu
        global turno
        global ganador
        global cantBarcos
        cantBarcos = [None,4,3,2,1]
        MatrizUsuario2 = []
        Guardar(MatrizUsuario,matrizCompu)
        ventanaJuego.withdraw()
        ventanaPonerBarcos.withdraw()
        ventanaMenu.deiconify()
        MatrizUsuario = [ ['0','0','0','0','0','0','0','0','0','0'],
                          ['0','0','0','0','0','0','0','0','0','0'],
                          ['0','0','0','0','0','0','0','0','0','0'],
                          ['0','0','0','0','0','0','0','0','0','0'],
                          ['0','0','0','0','0','0','0','0','0','0'],
                          ['0','0','0','0','0','0','0','0','0','0'],
                          ['0','0','0','0','0','0','0','0','0','0'],
                          ['0','0','0','0','0','0','0','0','0','0'],
                          ['0','0','0','0','0','0','0','0','0','0'],
                          ['0','0','0','0','0','0','0','0','0','0']]
        matrizCompu = []
        turno = False
        ganador = False
         

def Guardar(lista,lista2):
    global matrizCopiaCompu
    global matrizCopiaUsuario
    limite = len(lista)
    contador=0
    outfile = open((nombreJugador+'.txt'), 'w') # Indicamos el valor 'w' para escribir.
    outfile.write(str(TiempoJuego))
    outfile.write("\n")
   # print(limite)
    while (contador<limite):
         columnas=len(lista[0])-1# se toma la primera lista o matriz y se guarda elemento por elemento en el archivo
         contador2=0
         
         while (contador2<columnas):
             
             outfile.write(str(lista[contador][contador2])+" ")# se escribe en el archivo

             contador2=contador2+1
         outfile.write(str(lista[contador][contador2]))
         outfile.write("\n")# se hace el salto de linea del archivo
         contador=contador+1
    outfile.write("-2")# se pone un divisor para separar las matrices
    outfile.write("\n")
    limite = len(lista2)
    contador=0
    while (contador<limite):
        columnas=len(lista[0])-1# se usa la segunda lista para guardar en el archivo
        contador2=0
       
        while (contador2<columnas):
            outfile.write(str(lista2[contador][contador2])+" ")# se escribe en el archivo las posiciones de la matriz

            contador2=contador2+1
        outfile.write(str(lista2[contador][contador2]))
        outfile.write("\n")# se hace un cambio de linea 
        contador=contador+1

    outfile.write("-3")# se hace un divisor para las matrices que se usaran para reestablecer el juego en caso de reiniciar
    outfile.write("\n")
    limite =len(matrizCopiaCompu)
    contador=0
    print("CopiaCompu")
    print(matrizCopiaCompu)
    while (contador<limite):
        columnas=9
        contador2=0
        
        while (contador2<columnas):# se recorre la matriz inicial de la computadora, la cual se guardó en la copia para poder escribirla luego
           
            outfile.write(str(matrizCopiaCompu[contador][contador2])+" ")

            contador2=contador2+1
        outfile.write(str(matrizCopiaCompu[contador][contador2]))
        outfile.write("\n")
        contador=contador+1

    outfile.write("-4")# se hace un divisor para las matrices que se usaran para reestablecer el juego en caso de reiniciar
    outfile.write("\n")
    limite = len(matrizCopiaUsuario)
    contador=0
    print("CopiaCompu")
    print(matrizCopiaUsuario)
    while (contador<limite):
        columnas=9
        contador2=0
        
        while (contador2<columnas):# se recorre la matriz inicial del usuario, la cual se guardó en la copia para poder escribirla luego
            
            outfile.write(str(matrizCopiaUsuario[contador][contador2])+" ")

            contador2=contador2+1
        outfile.write(str(matrizCopiaUsuario[contador][contador2]))
        outfile.write("\n")
        contador=contador+1
    
    outfile.close()

# Reestablece las matrices a como deberian estar cuando comenzo la partida
##POR AQUI QUEDAMOS#


def reiniciarMatriz():
        global matrizCompu
        global MatrizUsuario
        global matrizCopiaCompu
        global MatrizCopiaUsuario

        matrizCompu = matrizCopiaCompu# se reinicia el juego, pone las matrices de computadora y usuario igual a sus copias originales
        MatrizUsuario = matrizCopiaUsuario
       
# Reinicia el estado de una partida para comenzar desde cero (0)    

def reiniciarJuego():
        global TiempoJuego
        global ganador
        global MatrizUsuario# se llama a reiniciarmatriz, se reinician tambien los tiempos y ganador 
        global matrizCompu

        if messagebox.askyesno("Reiniciar juego","Desea reiniciar el juego?"):
                reiniciarMatriz()
                TiempoJuego = 0
                ganador = False
                crearMatrizBotonesJ()
                crearMatrizBotonesC()
        

#               Menu Ventana Juego: Donde se establece que opciones existira en el menu para salir y/o guardar y/o reiniciar una partida
barraMenu = Menu(ventanaJuego)
menuJuego = Menu(barraMenu)
barraMenu.add_cascade(label="Juego", menu = menuJuego)
menuJuego.add_command(label="Guardar y salir al menú",command = salvarYSalir)
menuJuego.add_command(label="Reiniciar partida",command = reiniciarJuego)
menuJuego.add_separator()
menuJuego.add_command(label="Cerrar",command = cerrarPrograma)

ventanaJuego.config(menu=barraMenu)
#=====================================Menu Ventana Juego

#                       Imagenes
fondoPrincipal = PhotoImage(file = "Images/Battleship.gif")
fondoMenu = PhotoImage(file = "Images/Battleship2.gif")
fondoPonerBarcos = PhotoImage(file= "Images/Battleship3.gif")

cuadroCeleste = PhotoImage(file="Images/celeste2.gif")
cuadroRojo = PhotoImage(file="Images/rojo2.gif")

barco = PhotoImage(file= "Images/barco3.gif")
tocado = PhotoImage(file= "Images/tocado.gif")
derribado = PhotoImage(file= "Images/derribado.gif")
agua = PhotoImage(file = "Images/target.gif")

atacar = PhotoImage(file = "Images/atacar.gif")

indice1 = PhotoImage(file= "Images/indice1.gif")
indice2 = PhotoImage(file= "Images/indice2.gif")
indice3 = PhotoImage(file= "Images/indice3.gif")
indice4 = PhotoImage(file= "Images/indice4.gif")
indice5 = PhotoImage(file= "Images/indice5.gif")
indice6 = PhotoImage(file= "Images/indice6.gif")
indice7 = PhotoImage(file= "Images/indice7.gif")
indice8 = PhotoImage(file= "Images/indice8.gif")
indice9 = PhotoImage(file= "Images/indice9.gif")
indice10 = PhotoImage(file= "Images/indice10.gif")
indiceA = PhotoImage(file= "Images/indiceA.gif")
indiceB = PhotoImage(file= "Images/indiceB.gif")
indiceC = PhotoImage(file= "Images/indiceC.gif")
indiceD = PhotoImage(file= "Images/indiceD.gif")
indiceE = PhotoImage(file= "Images/indiceE.gif")
indiceF = PhotoImage(file= "Images/indiceF.gif")
indiceG = PhotoImage(file= "Images/indiceG.gif")
indiceH = PhotoImage(file= "Images/indiceH.gif")
indiceI = PhotoImage(file= "Images/indiceI.gif")
indiceJ = PhotoImage(file= "Images/indiceJ.gif")
#===========================================================Imagenes

#                 Labels
lblFondoVentanaMenu = Label(ventanaMenu,image=fondoMenu,bg="black")
lblFondoVentanaMenu.place(x=0,y=0)
#===========================================================Labels

#      DataEntry (Input Dialog Box) Y MessageBox de prueba para obtener el nombre del jugador
nombreJugador = simpledialog.askstring("Digite su nombre", prompt = ' ', parent=ventanaMenu)
messagebox.showinfo("Confirmacion","Su nombre es " + nombreJugador)
#==========================================================DataEntry y MessageBox
# ALGORITMO QUE SIRVE PARA JUGAR TANTO EL HUMANO COMO LA MAQUINA Y CALCULA EL GANADOR

def preguntarXY():
    global turno
    global ganador

    if not ganador:
    
            letras = ["A","B","C","D","E","F","G","H","I","J"]
            numeros = [1,2,3,4,5,6,7,8,9,10]
            posicion = simpledialog.askstring("Lanzar bomba",initialvalue='A,1', prompt = ' ', parent=ventanaJuego)
            print(posicion)
            
            try:
                
                posicion = posicion.split(',',1)
                print(posicion)
                print(1)
                print(type(posicion[0]))
                print(type(eval(posicion[1])))
                if(type(eval(posicion[1])) != int):
                    print(2)
                    messagebox.showinfo("Error","Debe ingresar un numero en la segunda posicion.")
                    preguntarXY()
                    
                elif( eval(posicion[1]) < 0 or eval(posicion[1]) > 10 ):
                    print(3)
                    messagebox.showinfo("Error","Debe ingresar un numero entre 1 y 10.")
                    preguntarXY()
                
                if type(posicion[1]) != str:
                    messagebox.showinfo("Error","Debe ingresar una letra en la primera posicion.")
                    preguntarXY()
                    
                try:
                    prueba = letras.index(posicion[0].upper())
                except:
                    messagebox.showinfo("Error","Debe ingresar una letra entre A y J.")
                    preguntarXY()
                
                
                y = numeros.index(eval(posicion[1]))
                x = letras.index(posicion[0].upper())
                tirarBomba(matrizCompu,x,y,matrizBotonesC,False)
                if ganar(matrizCompu):
                        ganador = True
                        messagebox.showinfo("Felicidades " + str(nombreJugador),"Me has ganado!")
                        print("C H E C K P O I N T")
                        if agregarNombreRecord():
                                guardarRecord()
                                print("El record actual es: " +str(listaRecord))
                turno = False
                print(posicion)
                if not ganador:
                        AI()
                        if ganar(MatrizUsuario):
                                ganador = True
                                messagebox.showinfo("Has perdido!","Mejor suerte la proxima " + str(nombreJugador))                                    
                        turno = True
         
            except:
                messagebox.showinfo("Error","Entrada invalida")
                preguntarXY()
        
        

def pegar(matriz,x,y):
    if(matriz[x][y]=='0'):# si pega un0 es agua
        matriz[x][y]='A'
        return "agua"
    elif(destruido(matriz,x,y)and matriz[x][y]!='-1'):# si el barco es destruido lo marca como tal y devuelve "destruido"
        matriz[x][y]='X'
        return "destruido"
    elif (matriz[x][y]=='-1'):
            return "pego uno que ya habia golpeado antes"
    else:
        matriz[x][y]='-1'# si no lo destruye y no pega agua lo marco como pegado y devuelve "pegado"
        return "pegado"
# Sirve para continuar una partida anteriormente guardada
def reanudarPartida():
        if existe(nombreJugador + ".txt"):
                cargarPartida()
                ventanaMenu.withdraw()
                crearMatrizBotonesJ()
                crearMatrizBotonesC()
                ventanaPonerBarcos.withdraw()
                ventanaJuego.deiconify()
        else:
                messagebox.showinfo("Error al cargar partida","No existe una partida guardada de este jugador")

#               Matrices:       Juego y  Botones

# Esto es un boton de control que se ve en el menu
btnCargarPartida = Button(ventanaMenu,text="Cargar Partida",relief=RAISED,command=reanudarPartida)
btnCargarPartida.place(x=100,y=400)

# Funcion que invoca a la ventana de nuevo juego para poner los barcos antes de comenzar el juego
def ubicarBarcos():
        ventanaMenu.withdraw()
        ventanaPonerBarcos.deiconify()

# Boton de control que hace que las ventanas cambien y desaparezcan algunas para aparecer otras. En este caso hace aparecer por medio de la funcion de arriba, lo que dice arriba.
btnNuevoJuego = Button(ventanaMenu,text="Nueva Partida", relief=RAISED,command=ubicarBarcos)
btnNuevoJuego.place(x=100,y=300)

# Configuracion para cambiar de vista en las ventanas 
def mostrarPuntajes():
        ventanaMenu.withdraw()
        ventanaPonerBarcos.withdraw()
        ventanaJuego.withdraw()
        ventanaRecords.deiconify()
        escribirPuntajes()

# Boton de control de la ventana menu para redireccionarse a la ventana que tiene los puntajes
btnVerPuntajes = Button(ventanaMenu,text="Ver Puntajes", relief=RAISED,command=mostrarPuntajes)
btnVerPuntajes.place(x=100,y=500)


# Configuracion para devolverse de una ventana a otra
def volverPuntajesMenu():
        ventanaMenu.deiconify()
        ventanaRecords.withdraw()

# Boton que aplica la configuracion de la funcion de arriba
btnAtrasPuntajes = Button(ventanaRecords,text="Volver",relief=RAISED,command=volverPuntajesMenu)
btnAtrasPuntajes.place(x=900,y=100)

# Configuracion para devolverse de una venta a otra junto con los valores que    P U D I E R O N    haber sido modificados para iniciar un juego nuevo
def volverNuevoJuegoMenu():
        global cantBarcos
        global MatrizUsuario
        
        ventanaPonerBarcos.withdraw()
        ventanaMenu.deiconify()
        cantBarcos = [None,4,3,2,1]

        MatrizUsuario=[ ['0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0'],
                        ['0','0','0','0','0','0','0','0','0','0']]
        actualizarMatrizPreeliminar()
        

# Boton de control para devolverse en caso de no querer iniciar un nuevo juego
btnAtrasNuevoJuego = Button(ventanaPonerBarcos,text="Volver",relief=RAISED,command=volverNuevoJuegoMenu)
btnAtrasNuevoJuego.place(x=10,y=500)
 

#       C O N F I G U R A C I O N   D E L   N U E V O    J U E G O

textoMatriz = ""
for i in MatrizUsuario:
        textoMatriz+=str(i)
        textoMatriz+="\n"
estilo1 = ("Time 32 bold") 
lblMatrizPreeliminar = Label(ventanaPonerBarcos,text=textoMatriz,font=estilo1)
lblMatrizPreeliminar.config(bg="dodgerBlue3")
lblMatrizPreeliminar.place(x=500,y=100)

# Esta funcion cambia la matriz de texto a su contenido actual para que el usuario vea donde van quedando los barcos que va posicionando para ponerlos a jugar

def actualizarMatrizPreeliminar():
        texto = ""
        for i in MatrizUsuario:
                texto+=str(i)
                texto+="\n"
        lblMatrizPreeliminar.config(text=texto,font=estilo1,bg="dodgerBlue3")
# De una vez actualizamos la matriz para que el usuario vaya viendo la matriz aunque sea vacia con puros ceros '0'
actualizarMatrizPreeliminar()

# Objetos de la ventana Partida Nueva, para preparar la matriz de barcos
lblIndicesLetras = Label(ventanaPonerBarcos,text="ABCDEFGHIJ",wraplength=1,font=estilo1)
lblIndicesLetras.config(bg="dodgerBlue3")
lblIndicesLetras.place(x=460,y=100)

lblNumeros = Label(ventanaPonerBarcos,text="1     2     3     4     5     6   7     8     9   10",font=estilo1)
lblNumeros.config(bg="dodgerBlue3")
lblNumeros.place(x=515,y=60)

comboLetras = ttk.Combobox(ventanaPonerBarcos)
comboLetras.config(state="readonly")
comboLetras["values"] = ["A","B","C","D","E","F","G","H","I","J"]
comboLetras.current(0)
comboLetras.place(x=10,y=200,height = 15, width= 50)

comboNumeros = ttk.Combobox(ventanaPonerBarcos)
comboNumeros.config(state="readonly")
comboNumeros["values"] = ["1","2","3","4","5","6","7","8","9","10"]
comboNumeros.current(0)
comboNumeros.place(x=70,y=200,height = 15, width= 50)

comboSize = ttk.Combobox(ventanaPonerBarcos)
comboSize.config(state="readonly")
comboSize["values"] = ["1","2","3","4"]
comboSize.current(0)
comboSize.place(x=130,y=200,height = 15, width= 50)

comboOrientacion = ttk.Combobox(ventanaPonerBarcos)
comboOrientacion.config(state="readonly")
comboOrientacion["values"] = ["Horizontal","Vertical"]
comboOrientacion.current(0)
comboOrientacion.place(x=190,y=200,height = 15, width= 100)



#=================================================================================

# Si ya se han colocado todos los barcos necesarios para jugar, entonces esta funcion devuelve verdadero, para poder asi habilitar el boton de jugar y comenzar el juego
def habilitarBotonJugar():
        if cantBarcos[1] == 0 and cantBarcos[2] == 0 and cantBarcos[3] == 0 and cantBarcos[4] == 0: # Si ya no quedan barcos por poner
                btnJugar.config(state=NORMAL) #Con esto se habilita el boton

# Funcion que ubica o no el barco en la matriz preeliminar para ir viendo como van a quedar posicionados. PD: Una vez puesto el barco, no se puede cambiar. A menos que empiece una nueva partida (otra vez)
def colocarBarco(): 
        letras = ["A","B","C","D","E","F","G","H","I","J"] # Letras validas. Al tenerlo en una lista asi es mas facil de llamar los indices de la matriz, pues estos comienzan de [0,N-1]
        numeros = ["1","2","3","4","5","6","7","8","9","10"] # Numeros validos. Al tenerlo en una lista asi es mas facil de llamar los indices de la matriz, pues estos comienzan de [0,N-1]
        y = numeros.index(comboNumeros.get())   #Posicion numero con valor actual del correspondiente combobox 
        x = letras.index(comboLetras.get())     #Posicion letra con valor actual del correspondiente combobox 
        size = eval(comboSize.get())            #Tamaño del barco de acuerdo con valor actual del correspondiente combobox 
        orientacion = comboOrientacion.get()    #Orientacion definida en el combobox y con valor actual al seleccionado correspondiente
        
        if(cantBarcos[size] != 0):              #Si aun quedan barcos por ponder de ese tamaño: 
                if PosicionarBarco(x,y,size,orientacion): #Si se puede poner el barco ahi:
                        actualizarMatrizPreeliminar()     #Actualizamos la matriz preeliminar para que el usuario lo vea
                        cantBarcos[size]-=1               #Disminuimos la cantidad de barcos restantes de ese tamaño
                        
                        habilitarBotonJugar()             #Verifica si se puede habilitar el boton de jugar o no todavia
                else:
                        messagebox.showinfo("Error","No es posible colocar este barco aqui")
                        
        else:
                messagebox.showinfo("Error","No quedan barcos de "+str(size)+" casilla(s)")
        
        
btnPonerBarco  = Button(ventanaPonerBarcos,text="Poner")  #Boton que va poniendo barcos
btnPonerBarco.config(command=colocarBarco)                #Se le asocia el comando de colocar barcos
btnPonerBarco.place(x=300,y=200)                          #Se ubica el boton en el plano X,Y de la ventana

def comenzarNuevoJuego():                                 #Este algoritmo prepara lo necesario para iniciar una nueva partida de esta manera:
        global TiempoJuego
        global matrizCopiaUsuario
        cargarRecord()                                    #Se carga el archivo con los puntajes y se almacenan en una lista en caso de que haya que agregarle un nuevo puntaje
        cargarArchivo()                                   #Esta funcion le asigna aleatoriamente una matriz de las 4 que hay para que la compu tenga posicionados sus barcos
        crearMatrizBotonesJ()                             #Crea la matriz de botones del jugador 
        crearMatrizBotonesC()                             #Crea la matriz de botones de la compu
        ventanaPonerBarcos.withdraw()                     #DESaparece la ventana de poner barcos
        ventanaJuego.deiconify()                          #APARECE la ventana de jugar
        TiempoJuego = 0                                   #Pone el tiempo de juego en cero (0) para iniciar desde cero por supuesto
        matrizCopiaUsuario =copy.deepcopy(MatrizUsuario)  #Hace un respaldo de la matriz en caso de que el usuario quiera reiniciar la partida
        print(matrizCopiaUsuario)
btnJugar = Button(ventanaPonerBarcos,text="Jugar",command=comenzarNuevoJuego)   #Boton que permite aparecer la ventana de jugar
btnJugar.place(x=100,y=500)
btnJugar.config(state=DISABLED)         #Se establece deshabilitado para poder habilitarlo cuando todos los barcos han sido posicionados en la nueva partida por comenzar



#============================================================================

#============================================================================
matrizBotonesJ= [ [0,0,0,0,0,0,0,0,0,0],                #Inicia en ceros pero luego a cada posicion se le asigna un boton
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0] ]

matrizBotonesC= [ [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],                #Lo mismo pasa aqui que con la matriz de arriba
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0,0] ]

# Funcion que devuelve los botones que se ponen en los bordes de las matrices para saber su Letra,Numero correspondiente
def obtenerBotonIndice(parent,row,column):
        numeros = ["",indice1,indice2,indice3,indice4,indice5,indice6,indice7,indice8,indice9,indice10]
        letras = ["",indiceA,indiceB,indiceC,indiceD,indiceE,indiceF,indiceG,indiceH,indiceI,indiceJ]
        
        if row == 0:
          return Button(parent,image = numeros[column], background="blue3", activebackground = "blue",state=DISABLED)

        if column == 0:
          return Button(parent,image = letras[row], background="blue3", activebackground = "blue",state=DISABLED)


# Esta funcion crea los botones que el jugador va a poder ver pero no tocar con las imagenes de barquitos y todas esas cosas.
def crearMatrizBotonesJ():
    global matrizBotonesJ
    global MatrizUsuario
    
    for i in range(0,10):
        for j in range(0,10):
            if i == 0: #Fila 0 -> Los numeros del borde
                btnIndiceColumna = obtenerBotonIndice(frameVentanaJuego,i,j+1)
                btnIndiceColumna.grid(row = i,column = j+1)
            if j == 0: #Columna 0 -> Las letras del borde
                btnIndiceFila = obtenerBotonIndice(frameVentanaJuego,i+1,j)
                btnIndiceFila.grid(row = i+1,column = j)

            if MatrizUsuario[i][j] == "0": # Este boton es el que se ve con el cuadro celeste (cuadroCeleste)
                btn = Button(frameVentanaJuego,image = cuadroCeleste,background="blue3",activebackground="blue",state=DISABLED)
                btn.grid(row = i+1, column = j+1)
                matrizBotonesJ[i][j] = btn
                
            elif MatrizUsuario[i][j] == "-1": # Este boton es el que se ve cuando se toca un barco (Tocado)
                btn = Button(frameVentanaJuego,image = tocado,background="blue3",activebackground="blue",state=DISABLED)
                btn.grid(row = i+1, column = j+1)
                matrizBotonesJ[i][j] = btn

            elif MatrizUsuario[i][j] == "X":  # Este boton aparece cuando un barco ha sido destruido por completo (Destruido)
                btn = Button(frameVentanaJuego,image = derribado,background="blue3",activebackground="blue",state=DISABLED)
                btn.grid(row = i+1, column = j+1)
                matrizBotonesJ[i][j] = btn
                
            elif MatrizUsuario[i][j] == "A":  # Este boton aparece si se ha bombeado una casilla sin nada mas que agua (Agua)
                btn = Button(frameVentanaJuego,image = agua,background="blue3",activebackground="blue",state=DISABLED)
                btn.grid(row = i+1, column = j+1)
                matrizBotonesJ[i][j] = btn
            
            else:                             # Sino este cuadro equivale a un barco :)
                btn = Button(frameVentanaJuego,image = barco,background="blue3",activebackground="blue",state=DISABLED)
                btn.grid(row = i+1, column = j+1)
                matrizBotonesJ[i][j] = btn

                                


def crearMatrizBotonesC(): # Mismo principio que la de arriba, solo que no muestra los barcos (sino no tendria chiste el juego)
    global matrizBotonesC
    global matrizCompu
    
    for i in range(11,21):
        for j in range(11,21):

            # BOTON ESPECIAL -> ATACAR COMPU
            if i==11 and j==11: #Este es el boton que el usuario presiona para atacar a la computadora
                btnAtacar = Button(frameVentanaJuego,image=atacar,background="blue3",activebackground="blue",command=preguntarXY)
                btnAtacar.grid(row=i-11,column=j)
                
            if i == 11: #Fila 0
                btnIndiceColumna = obtenerBotonIndice(frameVentanaJuego,i%11,(j%11)+1)
                btnIndiceColumna.grid(row = i-11,column = j+1)                

            if j == 11: #Columna 0
                btnIndiceFila = obtenerBotonIndice(frameVentanaJuego,(i%11)+1,j%11)
                btnIndiceFila.grid(row = i-10,column = j)
                
            if matrizCompu[i-11][j-11] == "-1":
                btn = Button(frameVentanaJuego,image = tocado,background="blue3",activebackground="blue",state=DISABLED)
                btn.grid(row = i-10, column = j+1)
                matrizBotonesC[i-11][j-11] = btn

            elif matrizCompu[i-11][j-11] == "X":
                btn = Button(frameVentanaJuego,image = derribado,background="blue3",activebackground="blue",state=DISABLED)
                btn.grid(row = i-10, column = j+1)
                matrizBotonesC[i-11][j-11] = btn


            elif matrizCompu[i-11][j-11] == "A":
                btn = Button(frameVentanaJuego,image = agua,background="blue3",activebackground="blue",state=DISABLED)
                btn.grid(row = i-10, column = j+1)
                matrizBotonesC[i-11][j-11] = btn
                
            else:
                btn = Button(frameVentanaJuego,text=str([i-11,j-11]),image = cuadroCeleste,background="blue3",activebackground="blue",state=DISABLED)
                btn.grid(row = i-10, column = j+1)
                matrizBotonesC[i-11][j-11] = btn
    



#==========================================================Botones

#           ARTIFICIAL INTELLIGENCE
#Este es el algoritmo para que la computadora ataque al jugador
def AI():
    x = randint(0,9)    #Se genera un X,Y random para atacar
    y = randint(0,9)

    #Si no ha sido atacado ese X,Y anteriormente
    if MatrizUsuario[x][y] != "X" and MatrizUsuario[x][y] != "-1" and MatrizUsuario[x][y] != "A":
        tirarBomba(MatrizUsuario,x,y,matrizBotonesJ,True) #A bombardear al humano
        return #Y a terminar el turno
    else: #Sino
        return AI() #Intentenlo de nuevo hasta que lo logre
#==========================================================AI

#==========================================================Archivos
def agregar(linea,matriz):
    linea= linea.split()
    #validar que los datos de la matriz sean los que queremos
    matriz.append(linea)

def cargarArchivo():
    global  matrizCopiaCompu
    global MatrizCompu# selecciona aleatoriamente uno de los 4 siguientes archivos
    lista=["Archivo1.txt","Archivo2.txt","Archivo3.txt","Archivo4.txt"]
    random.shuffle(lista)
   # print (lista[0])
    archivo = open(lista[0], "r")
    # se asigna a archivo el previamente seleccionado y luego se agrega a la matriz de la compu
    for linea in archivo.readlines():
        agregar (linea,matrizCompu)
       
    matrizCopiaCompu =  copy.deepcopy(matrizCompu)# se guarda la copia para poder reiniciar luego si se necesita
    print("impresion a ver qeu" )
    print(matrizCopiaCompu )
   

def cargarPartida():
    global TiempoJuego
    global matrizCompu
    global matrizCopiaCompu
    global matrizCopiaUsuario
    global MatrizUsuario
    
    archivo = open((nombreJugador+".txt"), "r")# se abre el archivo con una r para poder leer
    tiempoJuego=int(archivo.readline(7))
   
    matriz=0
    for linea in archivo.readlines():
        cambio=linea.split()
        if(cambio[0]=='-2'):# ss pregunta si es 2, si lo es se cambia la matriz a la cual se le modificaran los datos
           
            matriz=1
            #linea=linea+1
        elif(cambio[0]=='-3'):
           matriz=2 #ss pregunta si es 2, si lo es se cambia la matriz a la cual se le modificaran los datos
        elif(cambio[0]=='-4'):
            matriz=3 # ss pregunta si es 2, si lo es se cambia la matriz a la cual se le modificaran los datos
            
        if(matriz==0):# si el numero de matriz es igual a 0 se agregan a la matriz de usuario
   
            agregar (linea,MatrizUsuario2)
        elif(matriz==1):# si el numero de matriz es igual a 1 se agregan a la matriz de la computadora
            agregar(linea,matrizCompu)
        elif(matriz==2):# si el numero de matriz es igual a 2 se agregan a la matriz copia de computarora por si se necesita reiniciar
            agregar(linea,matrizCopiaCompu)
        else:
            agregar(linea,matrizCopiaUsuario)# si el numero de matriz es otro se agregan a la matriz copia de usuario por si se necesita reiniciar
            
            
    matrizCompu=matrizCompu[1:]
    matrizCopiaCompu=matrizCopiaCompu[1:]
    matrizCopiaUsuario=matrizCopiaUsuario[1:]
    MatrizUsuario=MatrizUsuario2
 
   # escribir(matriz)


#==========================================================

        
def Cronometro():
    """funcion que realiza el trabajo en el thread"""
    global TiempoJuego #hacer q el ciclo funcione con TiempoJuego
    
    TiempoJuego=0
    horas = TiempoJuego //   3600
    minutos = TiempoJuego // 60
    segundos = TiempoJuego % 60
    while True :
        TiempoJuego+=1
        horas = TiempoJuego //   3600
        minutos = TiempoJuego // 60
        segundos = TiempoJuego % 60
        if segundos == 60:
          segundos = 0
        if minutos == 60:
          minutos = 0
        
        time.sleep(1)
        tiempo = str(horas)+":"+str(minutos)+":"+str(segundos)
        ventanaJuego.title("Battleship -> Jugar | Tiempo del juego: " + tiempo)

#==========================================================

def PosicionarBarco(x,y,tamaño,orientacion):
   
    if(orientacion=="Horizontal"):
        if ((10-y)>=tamaño):#pregunta si el tamaño del barco cabe en posición horizontal
            if(cabe(x,y,tamaño,orientacion)):#si cabe en horizontal pregunta si otro barco impide su colocación
                asignar(x,y,tamaño,orientacion)#si no la impide, es asiganado un nuervo barco
                return True
            else:
                return False
        else:
            return False
    else:
        if((10-x)>=tamaño):#pregunta si el tamaño del barco cabe en posición vertical
            if(cabe(x,y,tamaño,orientacion)):#si cabe en horizontal pregunta si otro barco impide su colocación
                asignar(x,y,tamaño,orientacion)#si no la impide, es asiganado un nuervo barco
                
                return True
            else:
                return False
        else:
            return False

def cabe(x,y,tamaño,orientacion):
    y2=y
    if(orientacion=="Horizontal"):# si el barco es horizontal se recorre las filas de la matriz viendo si no hay un barco existente que estorbe en la colocación del nuevo
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
    print("y")
    print(y)
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
        print("y2")
        print(y2)
        if(y2+tamaño>9):
            if(MatrizUsuario[x-1][y2-1]=='0' and MatrizUsuario[x][y2]=='0' and MatrizUsuario[x-1][y2+tamaño-1]=='0'):
                return True
        elif(x==9):
                if(MatrizUsuario[x][y2]=='0' and MatrizUsuario[x][y2-1]=='0' and MatrizUsuario[x][y2+tamaño]=='0' and MatrizUsuario[x-1][y2]=='0' and MatrizUsuario[x-1][y2-1]=='0' and MatrizUsuario[x-1][y2+tamaño]=='0'):
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
    if(orientacion=="Horizontal"):
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

def ganar(matriz):
        filas=0# pregunta si toda la matriz es igual a 0 , -1, X o A es por que ya se ganó, sino, se retorna false ,si toda tiene estos valores, se retorna true
        while(filas<10):
                columnas=0
                while(columnas<10):
                        if(matriz[filas][columnas]=='0' or matriz[filas][columnas]=='-1' or matriz[filas][columnas]=='X' or matriz[filas][columnas]=='A'):
                                columnas=columnas +1
                        else:
                                return False
                filas=filas+1
        return True



        
#==========================================================

#jugarPartida()
iniciar()


# ___________ Finalmente ___________

Crono = threading.Thread(target=Cronometro)
Crono.start()
Inicio=threading.Thread(target=iniciar)
Inicio.start()

ventanaJuego.mainloop()
#ventanaMenu.mainloop()


Crono.join()
Inicio.join()


