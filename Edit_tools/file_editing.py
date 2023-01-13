from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from io import open

ruta = "" # Almacena la ruta de un fichero

def new(root, mensaje, texto):
    global ruta
    flag = MessageBox.askokcancel("New File", "If you have not saved the current file all progress will be lost, do you want to continue?")
    if flag:
        mensaje.set("New File")
        ruta = ""
        texto.delete(1.0, "end")
        root.title("My editor")
    return



def open_file(root, mensaje, texto):
    global ruta

    mensaje.set("Open File")

    flag = MessageBox.askokcancel("Open File", "If you have not saved the current file all progress will be lost, do you want to continue?")
    if flag:
        ruta = FileDialog.askopenfilename(initialdir='.', title="Open text file",
            filetypes=(("Text files", "*.txt"),))
        if ruta != "":
            try:
                with open(ruta, 'r') as input:
                    contenido = input.read()
                    texto.delete(1.0, "end")
                    texto.insert('insert', contenido)
            
                root.title(ruta + " - Mi editor")
            except:
                MessageBox.showerror("Error", "Could not open the file")
                mensaje.set("Welcome to My Editor")



def save(mensaje, texto):
    global ruta

    mensaje.set("Save File")

    if ruta != "":
        contenido = texto.get(1.0, "end-1c") # Recupera todo el texto menos el ultimo caracter, que es un salto de linea
        with open(ruta, 'w+') as output:
            output.write(contenido)
        mensaje.set("File saved correctly")
    else:
        save_as(mensaje, texto)



def save_as(mensaje, texto):
    global ruta
    mensaje.set("Saving File as")

    fichero = FileDialog.asksaveasfile(title="Save File", mode='w',
        defaultextension=".txt")

    if fichero is not None:
        ruta = fichero.name # Ruta del fichero
        contenido = texto.get(1.0, "end-1c")

        with open(ruta, "w+") as output:
            output.write(contenido)
        mensaje.set("File saved correctly")
    else:
        mensaje.set("Save canceled")
        ruta = ""