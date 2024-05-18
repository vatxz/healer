import pyautogui as pg
import keyboard

def check_battle():
    return pg.locateOnScreen('C:/Users/sanga/OneDrive/Escritorio/ARCHIVOS/maincreo/capturas/battlevacio.PNG', region = (1481, 44, 201, 246))


#is battle =check_battle()  
#print(is_battle)

while True:
  keyboard.wait('h')
  is_battle = check_battle()
  if is_battle == None:
     print("algo pasa aqui")
     pg.press('space')
  print(is_battle)