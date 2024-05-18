import pytesseract
import pyautogui as pg
import cv2
import numpy as np

# Coordenadas de la región donde se encuentra el texto "rat"
rat_x, rat_y, rat_w, rat_h = 1507, 107, 173, 20

def read_text(x, y, w, h):
    screenshot = pg.screenshot(region=(x, y, w, h))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    median = cv2.medianBlur(binary, 3)
    inverted = cv2.bitwise_not(median)
    
    text = pytesseract.image_to_string(inverted)
    return text

while True:
    rat_found = read_text(rat_x, rat_y, rat_w, rat_h)
    print("Detected text:", rat_found)

