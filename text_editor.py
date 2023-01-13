from tkinter import *
from Edit_tools.file_editing import *

if __name__ == '__main__':
    # Configuracion de la raiz
    root = Tk()
    root.title("My editor")
    root.iconbitmap("Logo.ico")


    # Menu superior
    menubar = Menu(root)
    root.config(menu=menubar)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=lambda: new(root, mensaje, texto))
    filemenu.add_command(label="Open", command=lambda: open_file(root, mensaje, texto))
    filemenu.add_command(label="Save", command=lambda: save(mensaje, texto))
    filemenu.add_command(label="Save as", command=lambda: save_as(mensaje, texto))

    exitmenu = Menu(menubar, tearoff=0)
    exitmenu.add_command(label="Exit", command=root.quit)

    menubar.add_cascade(menu=filemenu, label="File")
    menubar.add_cascade(menu=exitmenu, label="Exit")

    # Caja de texto central
    texto = Text(root)
    texto.pack(fill="both", expand=1)
    texto.config(width=75, height=20,bd = 0, padx=6, pady=4, font=("Consolas", 12), 
        selectbackground="HotPink1", background="grey27", foreground="white")


    # Monitor inferior
    mensaje = StringVar()
    mensaje.set("Welcome to My Editor")
    monitor = Label(root, textvariable=mensaje, justify="left")
    monitor.pack(side="left")

    # Bucle de la aplicacion
    root.mainloop()