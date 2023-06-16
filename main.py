import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random

# Función que se ejecuta al seleccionar una 
nivel = 0
def seleccionar_dificultad(dificultad):
    if (dificultad == 'Principiante'):
        nivel = 2
    elif (dificultad == 'Amateur'):  
        nivel = 4
    else:
        nivel = 6       
    print("Dificultad seleccionada:", dificultad)
    print('nivel: ',nivel)
    ventana_dificultad.destroy()

# Crear la ventana de selección de dificultad
ventana_dificultad = tk.Tk()
ventana_dificultad.title("Seleccionar Dificultad")

canvas_width = 450
canvas_height = 420

# Calcula la posición x e y para centrar la ventana en la mitad de la pantalla
ancho_pantalla = ventana_dificultad.winfo_screenwidth()
altura_pantalla = ventana_dificultad.winfo_screenheight()
x = int((ancho_pantalla - canvas_width) / 2)
y = int((altura_pantalla - canvas_height) / 2)

# Configura la posición de la ventana
ventana_dificultad.geometry(f"{canvas_width}x{canvas_height}+{x}+{y}")

# Crear el texto para guiar al usuario en el ventana
cuadro_title = tk.Canvas(ventana_dificultad, width=200, height=50)
cuadro_title.create_text(100, 30, text='Smart Horses', width=400, font=("Arial", 20))
cuadro_title.pack(pady=50)
cuadro_info = tk.Canvas(ventana_dificultad, width=210, height=50)
cuadro_info.create_text(110, 30, text='Seleccione la dificultad:', width=400, font=("Arial", 15))
cuadro_info.pack()


# Función para crear los botones de dificultad
def crear_boton_dificultad(dificultad):
    boton = tk.Button(ventana_dificultad, text=dificultad, width=20, height=2,
                      command=lambda: seleccionar_dificultad(dificultad))
    boton.pack(pady=10)

# Crear los botones de dificultad
crear_boton_dificultad("Principiante")
crear_boton_dificultad("Amateur")
crear_boton_dificultad("Experto")

# Mostrar la ventana de selección de dificultad
ventana_dificultad.mainloop()

# Creamos la matriz con valores aleatorios
matriz = []
lista = []

# LLenamos lista con los posibles varoles del tablero
for i in range(54):
    lista.append('0')
for i in range(8):
    lista.append(str(i))
lista.append('N')
lista.append('B')

# Llenamos la matriz
while len(lista) > 0:
    fila = []
    while len(fila) < 8:
        index = random.randint(0, len(lista)-1)
        fila.append(lista[index])
        lista.pop(index)
    matriz.append(fila)

# Función para mover el caballo
def mover(event):

    #Calculamos el x, y, de la celda selecionada
    global selected_cell
    x = event.x // cell_width
    y = event.y // cell_height

    try:
        # Mensaje por si presiona el caballo del jugador o de la maquina
        if matriz[y][x] == 'N':
            selected_cell = (x, y)
            messagebox.showinfo("Mensaje", "Este es el caballo del jugador.")
        if matriz[y][x] == 'B':
            selected_cell = (x, y)
            messagebox.showinfo("Mensaje", "Este es el caballo de la maquina.")
    except:
        messagebox.showerror("Error", "Error, cierre la ventana")

    # mover derecha arriba
    try:
        if matriz[y+1][x-2] == 'N':
            if matriz[y][x] != 'B':
                selected_cell = (x, y)
                matriz[y+1][x-2] = '0'
                matriz[y][x] = 'N'
    except:
        pass

    # mover derecha abajo
    try:
        if matriz[y-1][x-2] == 'N':
            if matriz[y][x] != 'B':
                selected_cell = (x, y)
                matriz[y-1][x-2] = '0'
                matriz[y][x] = 'N'
    except:
        pass

    # mover izquierda arriba
    try:
        if matriz[y+1][x+2] == 'N':
            if matriz[y][x] != 'B':
                selected_cell = (x, y)
                matriz[y+1][x+2] = '0'
                matriz[y][x] = 'N'
    except:
        pass

    # mover izquierda abajo
    try:
        if matriz[y-1][x+2] == 'N':
            if matriz[y][x] != 'B':
                selected_cell = (x, y)
                matriz[y-1][x+2] = '0'
                matriz[y][x] = 'N'
    except:
        pass

    # mover arriba derecha
    try:
        if matriz[y+2][x-1] == 'N':
            if matriz[y][x] != 'B':
                selected_cell = (x, y)
                matriz[y+2][x-1] = '0'
                matriz[y][x] = 'N'
    except:
        pass

    # mover abajo derecha
    try:
        if matriz[y-2][x-1] == 'N':
            if matriz[y][x] != 'B':
                selected_cell = (x, y)
                matriz[y-2][x-1] = '0'
                matriz[y][x] = 'N'
    except:
        pass

    # mover arriba izquierda
    try:
        if matriz[y+2][x+1] == 'N':
            if matriz[y][x] != 'B':
                selected_cell = (x, y)
                matriz[y+2][x+1] = '0'
                matriz[y][x] = 'N'
    except:
        pass

    # mover abajo izquierda
    try:
        if matriz[y-2][x+1] == 'N':
            if matriz[y][x] != 'B':
                selected_cell = (x, y)
                matriz[y-2][x+1] = '0'
                matriz[y][x] = 'N'
    except:
        pass

    animacion()

#Ventana del tablero
ventana = tk.Tk()
ventana.title("Smart Horse")

# Calcula el tamaño necesario para el canvas basado en el tamaño de la matriz
cell_width = 50
cell_height = 50
canvas_width = len(matriz[0]) * cell_width + 50
canvas_height = len(matriz) * cell_height + 20

# Calcula la posición x e y para centrar la ventana en la mitad de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
altura_pantalla = ventana.winfo_screenheight()
x = int((ancho_pantalla - canvas_width) / 2)
y = int((altura_pantalla - canvas_height) / 2)

# Configura la posición de la ventana
ventana.geometry(f"{canvas_width}x{canvas_height}+{x}+{y}")

# Crea el canvas y dibuja el cuadrado 
canvas = tk.Canvas(ventana, width=cell_width*8, height=canvas_height*8)
canvas.place(x=60, y=60, width=cell_width*8, height=cell_height*8) #Agregar canvas a la ventana
cuadrado_matriz = canvas.create_rectangle(0,0,cell_width*8,cell_height*8)
canvas.itemconfig(cuadrado_matriz, outline="black", width=7)
canvas.pack()

# Dibuja la cuadrícula
for i in range(8):
    canvas.create_line(i*cell_width, 0, i*cell_width, cell_height*8) #Dibuja líneas verticales
    canvas.create_line(0, i*cell_height, cell_width*8, i*cell_height) #Dibuja líneas horizontales

# Dibuja las imagenes
canvas.imagenes = []

def dibujarImagen(url, etiqueta, x, y, width, height):
    imagen = Image.open(url)
    imagen = imagen.resize((x, y))
    imagen = ImageTk.PhotoImage(imagen)
    # Calcula las coordenadas x e y para centrar la imagen en la casilla
    x_center = width + (cell_width - x) // 2
    y_center = height + (cell_height - y) // 2
    # Calcula las coordenadas de anclaje para el centro de la imagen
    anchor_x = x_center + x // 2
    anchor_y = y_center + y // 2
    canvas.create_image(anchor_x, anchor_y, anchor=tk.CENTER, image=imagen, tag=etiqueta)
    canvas.imagenes.append(imagen)

# crea las imagenes
def verMatriz (matriz,url,etiqueta):
     # borramos todo lo dibujado anteriormente
     canvas.delete(etiqueta)
     for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == 'B':
                dibujarImagen(url[0],etiqueta,40,40,j*cell_width, i*cell_height)
            elif valor == 'N':
                dibujarImagen(url[1],etiqueta,40,40,j*cell_width, i*cell_height)
            if valor == '1':
                dibujarImagen(url[2],etiqueta,35,35,j*cell_width, i*cell_height)
            if valor == '2':
                dibujarImagen(url[3],etiqueta,35,35,j*cell_width, i*cell_height)
            if valor == '3':
                dibujarImagen(url[4],etiqueta,35,35,j*cell_width, i*cell_height)
            if valor == '4':
                dibujarImagen(url[5],etiqueta,35,35,j*cell_width, i*cell_height)
            if valor == '5':
                dibujarImagen(url[6],etiqueta,35,35,j*cell_width, i*cell_height) 
            if valor == '6':
                dibujarImagen(url[7],etiqueta,35,35,j*cell_width, i*cell_height) 
            if valor == '7':
                dibujarImagen(url[8],etiqueta,35,35,j*cell_width, i*cell_height)    

# Evento del mouse para mover al caballo
canvas.bind("<Button-1>", mover)

# Lista de las url de las imagenes
urlImagenes = ["./Images/caballoD.webp","./Images/caballoN.webp","./Images/una.png","./Images/dos.png","./Images/tres.png","./Images/cuatro.png","./Images/cinco.png","./Images/seis.png","./Images/siete.png"]

#Función que permitirá visualizar la animación
def animacion ():
    verMatriz(matriz, urlImagenes,'imagen')
    ventana.update()

# Mostramos la matriz incial
verMatriz(matriz, urlImagenes,'imagen')

ventana.mainloop()