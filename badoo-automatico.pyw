import os
from  tkinter import *
import badoo_macht
def maches():
    print('holaaaaa')
    texto = badoo_macht.ejecutar_baboo_mach(number.get())
    Label(root, text= texto).pack()

# Configuración de la raíz
root = Tk()
root.config(bd=30)

number = StringVar()

Label(root, text="Número de machs que desea dar").pack()
Entry(root, justify="center", textvariable=number).pack()

# Label(root, text="Resultado").pack()
# Entry(root, justify="center", textvariable=r, state="disabled").pack()
 
Button(root, text="Iniciar machs", command=maches).pack()

root.mainloop()
badoo_macht.driver.close()
os.system('taskkill /f /im cmd.exe')