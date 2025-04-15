# fen

import tkinter as tk
from tkinter import messagebox

def fen_to_board(fen):
    try:
        partes=fen.split()
        if len(partes)!=6: #verifica q el FEN tenga las 6 partes
            return None
        filas_fen=partes[0].split('/')
        if len(filas_fen)!=8: #verifica q el tablero sea 8x8
            return None
        piezas_validas="rnbqkpRNBQKP" #verifica solamente las piezas validas del ajedrez
        tablero=[]
        for fila in filas_fen:
            filas=[]
            t_casillas=0
            for char in fila:
                if char.isdigit():
                    num=int(char)
                    if num<1 or num>8: #verifica q el numero no sea mayor a 8/menor a 1 para las filas
                        return None
                    filas.extend(['ㅤ']*num)
                    t_casillas+=num
                elif char in piezas_validas:
                    filas.append(char)
                    t_casillas+=1
                else:
                    return None
            if t_casillas!=8: #validacion de filas 8 por fila no mas ni menos
                return None
            tablero.append(filas)
        #verificaciones de 6 piezas que cumplan el fen
        #verificacion de turnos w,b white/black [1]
        if partes[1] not in ['w','b']:
            return None
        #verifica enroques o es - o es KQkq [2]
        enroques_validos=set('KQkq')
        if partes[2]!='-':
            for c in partes[2]:
                if c not in enroques_validos:
                    return None
        #verificacion de captura al paso casillas validas a,b,c... [3]
        if partes[3]!='-':
            if len(partes[3])!=2:
                return None
            col=partes[3][0]
            fila=partes[3][1]
            if col not in 'abcdefgh' or fila not in '36':
                return None
        #verificacion de contador de medio movimiento (regla)
        if not partes[4].isdigit() or int(partes[4])<0:
            return None
        #verificacion de contador de movimientos
        if not partes[5].isdigit() or int(partes[5])<1:
            return None

        return tablero
    except:
        return None

def show_tab():
    fen=entrada_fen.get()
    for widget in marco.winfo_children():
        widget.destroy()
    tablero=fen_to_board(fen)
    valido=tablero is not None
    if not valido:
        mensaje.set("el formato FEN es invalido")
        mensaje_color.set("rojo")
        return
    else:
        mensaje.set("el formato FEN es valido")
        mensaje_color.set("azul")
    for i in range(8):
        for j in range(8):
            casilla=tablero[i][j]
            color="#f0eded"if(i+j)%2==0 else "#706f6f"
            texto=casilla
            label=tk.Label(marco, text=texto, width=4, height=2, bg=color, fg="black", font=("Courier", 16, "bold"))
            label.grid(row=i, column=j)

def actualizar_color(*args):
    if mensaje_color.get()=="rojo":
        label_mensaje.config(fg="red")
    else:
        label_mensaje.config(fg="blue")

ventana=tk.Tk()
ventana.title("problema 1")
tk.Label(ventana, text="cadena de formato fen: ").pack(pady=5)
entrada_fen=tk.Entry(ventana, width=60)
entrada_fen.pack()
tk.Button(ventana, text="mostrar validacion", command=show_tab).pack(pady=10)
marco=tk.Frame(ventana)
marco.pack()
mensaje=tk.StringVar()
mensaje_color=tk.StringVar()
mensaje_color.trace_add("write", actualizar_color)
label_mensaje=tk.Label(ventana, textvariable=mensaje, font=("Arial",12))
label_mensaje.pack(pady=10)
ventana.mainloop()