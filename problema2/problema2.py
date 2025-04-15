# triangulo de pascal
import tkinter as tk
from tkinter import messagebox
import math

def obtener_fila_pascal(n):
    if n<0: return []
    if n==0: return [1]
    if n==1: return [1,1]
    fila_anterior=obtener_fila_pascal(n-1)
    nueva_fila=[0]*(n+1)
    nueva_fila[0]=1
    nueva_fila[n]=1
    for i in range(1,n): nueva_fila[i]=fila_anterior[i-1]+fila_anterior[i]
    return nueva_fila # fila de coeficientes y recursividad

def crear_polinomio(n):
    coeficientes=obtener_fila_pascal(n) #genera el polinomio extrayendo datos de la funcion anterior
    polinomio=""
    for i in range(n,-1,-1):
        coef=coeficientes[i]
        if coef==0: continue
        if coef==1 and i!=0: # construye una cadena mayor a menor grado y omite coeficientes
            polinomio+="x^"+str(i) if i==n else "+x^"+str(i)
        elif coef==-1:
            polinomio+="-x^"+str(i)
        else:
            if i==n: polinomio+=str(coef)+"x^"+str(i)
            elif i==0: polinomio+=str(coef)
            else: polinomio+=str(coef)+"x^"+str(i)
        if i>0: polinomio+=" + "
    return polinomio 

def calcular_resultado(n,valor_x): # evalua el polimonio generado
    coeficientes=obtener_fila_pascal(n)
    total=0
    for i in range(n,-1,-1): total+=coeficientes[i]*(valor_x**i)
    return total # devuelve el valor total de todos los resultados

def mostrar_pasos(n,valor_x):
    coeficientes=obtener_fila_pascal(n)
    pasos=[]
    suma=0
    for i in range(n,-1,-1):
        potencia=valor_x**i
        multiplicacion=coeficientes[i]*potencia
        pasos.append(f"termino ({coeficientes[i]})*{valor_x}^{i} = {multiplicacion}")
        suma+=multiplicacion
    return pasos,suma # realiza lo anterior pero paso por paso y va guardando y se coloca

def procesar(): # main
    for widget in contenedor_pasos.winfo_children(): widget.destroy()
    try:
        grado=int(caja_grado.get())
        valor=int(caja_valor.get())
    except:
        mensaje_final.set("valores inválidos")
        color_mensaje.set("rojo")
        return
    if grado<0:
        mensaje_final.set("gl grado debe ser mayor o igual a 0")
        color_mensaje.set("rojo")
        return
    expresion=crear_polinomio(grado)
    resultado=calcular_resultado(grado,valor)
    pasos,resultado_final=mostrar_pasos(grado,valor)
    mensaje_final.set(f"(x+1)^{grado} = {expresion}\n\nf({valor}) = {resultado}\n")
    color_mensaje.set("azul")
    for paso in pasos: tk.Label(contenedor_pasos,text=paso,font=("Arial",10)).pack()

def actualizar_color(*args):
    if color_mensaje.get()=="rojo": etiqueta_resultado.config(fg="red")
    else: etiqueta_resultado.config(fg="blue")

ventana=tk.Tk()
ventana.title("problema 2")
tk.Label(ventana,text="ingresa el grado n (entero≥0):").pack(pady=5)
caja_grado=tk.Entry(ventana,width=20)
caja_grado.pack()
tk.Label(ventana,text="ingresa el valor de x:").pack(pady=5)
caja_valor=tk.Entry(ventana,width=20)
caja_valor.pack()
tk.Button(ventana,text="calcular",command=procesar).pack(pady=10)
contenedor_pasos=tk.Frame(ventana)
contenedor_pasos.pack()
mensaje_final=tk.StringVar()
color_mensaje=tk.StringVar()
color_mensaje.trace_add("write",actualizar_color)
etiqueta_resultado=tk.Label(ventana,textvariable=mensaje_final,font=("Arial",12))
etiqueta_resultado.pack(pady=10)
ventana.mainloop()