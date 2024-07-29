from PIL import ImageGrab
import time
import pyautogui

x_inicial = 353
x_final = 516

y_inicial = 582
y_final = 670



def captura_tela():
    screen = ImageGrab.grab()
    return screen
   

def detecta_obj(screen, xi, xf):
    for x in range(xi,y_inicial):
        for y in range(xf, y_final):
            color = screen.getpixel((x,y))
            if color == (172, 172, 172):
                return True
def jump():
    pyautogui.press("up")
    

print("Startting robot")
while True:
    screen = captura_tela()
    
    if detecta_obj(screen ,x_inicial, x_final):
       jump()
       print(f'X Inicial: {x_inicial}')
       print(f'X Finak: {x_final}')
       x_inicial+=1
       x_final+=1
        
    
