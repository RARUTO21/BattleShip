from tkinter.filedialog import *
from tkinter import *

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
#===========================================================Labels



#               Botones


#==========================================================Botones



# ___________ Finalmente ___________

iniciar()
ventanaPrincipal.mainloop()
