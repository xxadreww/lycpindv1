# currencias

import tkinter as tk
from tkinter import messagebox

def contar_subcadena():
    cadena=entrada_cadena.get()
    palabra=entrada_palabra.get()
    for widget in marco.winfo_children():
        widget.destroy()
    if not cadena or not palabra:
        mensaje.set("no se ingreso ninguna cadena")
        mensaje_color.set("rojo")
        return
    cantidad=cadena.count(palabra)
    mensaje.set(f"la palabra '{palabra}' aparece {cantidad} veces")
    mensaje_color.set("azul")

def actualizar_color(*args):
    if mensaje_color.get()=="rojo":
        label_mensaje.config(fg="red")
    else:
        label_mensaje.config(fg="blue")

ventana=tk.Tk()
ventana.title("problema 4")
tk.Label(ventana, text="ingresa la cadena:").pack(pady=5)
entrada_cadena=tk.Entry(ventana, width=60)
entrada_cadena.pack()
tk.Label(ventana, text="ingresa la palabra a buscar:").pack(pady=5)
entrada_palabra=tk.Entry(ventana, width=30)
entrada_palabra.pack()
tk.Button(ventana, text="ver ocurrencias", command=contar_subcadena).pack(pady=10)
marco=tk.Frame(ventana)
marco.pack()
mensaje=tk.StringVar()
mensaje_color=tk.StringVar()
mensaje_color.trace_add("write", actualizar_color)
label_mensaje=tk.Label(ventana, textvariable=mensaje, font=("Arial", 12))
label_mensaje.pack(pady=10)
ventana.mainloop()
