#notacion E

import tkinter as tk
from tkinter import messagebox
import re

def evaluar_expr(expr):
    try:
        pasos=[]
        expr_original=expr.replace(" ","")
        expr=expr_original.replace("E","e")
        pasos.append("expresion original: "+expr_original)
        resultado=eval(expr) #expresion en python
        pasos.append("resultado final: "+str(resultado))
        return pasos
    except Exception as e:
        return ["expresion invalida: "+str(e)]

def mostrar_resultado():
    expr=entrada_expr.get()
    pasos=evaluar_expr(expr)
    caja_texto.delete("1.0",tk.END)
    for paso in pasos:
        caja_texto.insert(tk.END, paso+"\n")

ventana=tk.Tk()
ventana.title("problema 3")
tk.Label(ventana, text="expresion a evaluar:").pack(pady=5)
entrada_expr=tk.Entry(ventana, width=60)
entrada_expr.pack()
tk.Button(ventana, text="evaluar expresion", command=mostrar_resultado).pack(pady=10)
caja_texto=tk.Text(ventana, height=10, width=70, font=("Courier",10))
caja_texto.pack(pady=10)
ventana.mainloop()