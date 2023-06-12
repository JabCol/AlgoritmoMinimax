import tkinter as tk
from PIL import Image, ImageTk
from logic import matriz

#Ventana
ventana = tk.Tk()

# Obtener el ancho y la altura de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
altura_pantalla = ventana.winfo_screenheight()

# Calcular la posición x e y de la ventana para centrarla
x = int((ancho_pantalla - 1150) / 2)  # ancho de la ventana es 800
y = int((altura_pantalla - 700) / 2)  # altura de la ventana es 600

# Configurar la posición de la ventana
ventana.geometry(f"1150x700+{x}+{y}")

# Tamaño de cada celda
cell_width = 50
cell_height = 50

# Crear el canvas y dibujar el cuadrado 
canvas = tk.Canvas(ventana, width=cell_width*8, height=cell_height*8) #Ancho del widget canvas
canvas.place(x=60, y=60, width=cell_width*8, height=cell_height*8) #Agregar canvas a la ventana
cuadrado_matriz = canvas.create_rectangle(0,0,cell_width*8,cell_height*8)
canvas.itemconfig(cuadrado_matriz, outline="black", width=7)

# Dibujar la cuadrícula
for i in range(8):
    canvas.create_line(i*cell_width, 0, i*cell_width, cell_height*8) #Dibuja líneas verticales
    canvas.create_line(0, i*cell_height, cell_width*8, i*cell_height) #Dibuja líneas horizontales


imagen = None
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


def verMatriz (matriz,url,etiqueta):
     # borramos todo lo dibujado anteriormente
     canvas.delete(etiqueta)
     for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == 'B':
                dibujarImagen(url[0],etiqueta,40,40,j*cell_width, i*cell_height)
            elif valor == 'N':
                dibujarImagen(url[1],etiqueta,40,40,j*cell_width, i*cell_height)
            if valor == 1:
                dibujarImagen(url[2],etiqueta,35,35,j*cell_width, i*cell_height)
            if valor == 2:
                dibujarImagen(url[3],etiqueta,35,35,j*cell_width, i*cell_height)
            if valor == 3:
                dibujarImagen(url[4],etiqueta,35,35,j*cell_width, i*cell_height)
            if valor == 4:
                dibujarImagen(url[5],etiqueta,35,35,j*cell_width, i*cell_height)
            if valor == 5:
                dibujarImagen(url[6],etiqueta,35,35,j*cell_width, i*cell_height) 
            if valor == 6:
                dibujarImagen(url[7],etiqueta,35,35,j*cell_width, i*cell_height) 
            if valor == 7:
                dibujarImagen(url[8],etiqueta,35,35,j*cell_width, i*cell_height)    

# Lista de las url de las imagenes
urlImagenes = ["./Images/caballoD.webp","./Images/caballoN.webp","./Images/una.png","./Images/dos.png","./Images/tres.png","./Images/cuatro.png","./Images/cinco.png","./Images/seis.png","./Images/siete.png"]

#Función que mostrará la matriz incial
def verMatrizInical():
    verMatriz(matriz, urlImagenes,'imagen')

verMatrizInical()


ventana.mainloop()


