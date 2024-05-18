import cv2
import numpy as np
import pytesseract
import pyautogui as pg
import tkinter as tk
from tkinter import ttk
import time

# Variables globales para vida y mana
vida = 500
mana = 150
running = False

# Función para leer los números
def read_number(x, y, w, h):
    screenshot = np.array(pg.screenshot(region=(x, y, w, h)))
    
    # Invierte los colores de la imagen
    inverted = cv2.bitwise_not(screenshot)
    gray = cv2.cvtColor(inverted, cv2.COLOR_BGR2GRAY)
    
    # Aplica un filtro gaussiano para suavizar la imagen
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Aplica umbralización adaptativa
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 2)
    
    # Configuración para números
    config = '--psm 6 outputbase digits'
    text = pytesseract.image_to_string(binary, config=config)
    
    # Filtrar solo dígitos
    numbers = ''.join(filter(str.isdigit, text))
    
    # Si no se encontraron dígitos, devuelve None
    if not numbers:
        return None
    
    return numbers

# Coordenadas de la región donde se encuentra el número de vida
life_x, life_y, life_w, life_h = 1857, 377, 33, 18
# Coordenadas de la región donde se encuentra el número de mana
mana_x, mana_y, mana_w, mana_h = 1855, 392, 38, 23

def start_program():
    global running
    running = True
    run_program()

def pause_program():
    global running
    running = False

def update_values():
    global vida, mana
    vida = int(vida_entry.get())
    mana = int(mana_entry.get())
    vida_label.config(text=f"Vida: {vida}")
    mana_label.config(text=f"Mana: {mana}")

def run_program():
    global running
    if not running:
        return
    
    life_number = read_number(life_x, life_y, life_w, life_h)
    mana_number = read_number(mana_x, mana_y, mana_w, mana_h)
    print(f"Vida: {life_number} - Mana: {mana_number}")
    
    if life_number is not None and int(life_number) < vida:
        pg.press('f1')
        print("Presionando F1")
    if mana_number is not None and int(mana_number) < mana:
        pg.press('f2')
        print("Presionando F2")
    
    root.after(100, run_program)  ###################### Tiempo de espera reducido a 0.5 segundos ##################################

# Crear la ventana principal
root = tk.Tk()
root.title("Control de Programa")
root.geometry("300x200")

# Botones de control
start_button = ttk.Button(root, text="Start", command=start_program)
start_button.pack()

pause_button = ttk.Button(root, text="Pause", command=pause_program)
pause_button.pack()

# Entradas para editar los valores de vida y mana
vida_label = ttk.Label(root, text="Vida:")
vida_label.pack()
vida_entry = ttk.Entry(root)
vida_entry.insert(0, str(vida))
vida_entry.pack()

mana_label = ttk.Label(root, text="Mana:")
mana_label.pack()
mana_entry = ttk.Entry(root)
mana_entry.insert(0, str(mana))
mana_entry.pack()

update_button = ttk.Button(root, text="Update Values", command=update_values)
update_button.pack()

# Ejecutar la aplicación
root.mainloop()