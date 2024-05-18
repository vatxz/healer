import cv2
import numpy as np
import pytesseract
import pyautogui as pg
import time


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

while True:
    life_number = read_number(life_x, life_y, life_w, life_h)
    mana_number = read_number(mana_x, mana_y, mana_w, mana_h)
    
    print(f"Vida: {life_number} - Mana: {mana_number}")
    
    if life_number is not None and int(life_number) < 500:
        pg.press('f1')
        print("Presionando F1")
    if mana_number is not None and int(mana_number) < 150:
        pg.press('f2')
        print("Presionando F2")
    
    time.sleep(1)
