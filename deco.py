# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:21:34 2024

@author: jom
"""
import time
from PIL import ImageGrab
import requests
#r = requests.get('http://192.168.2.88:5000/?numero=1234')

# Bounding box
an=10
cx=1500
cx2=2560
cy=460
cy2=690

# Color a buscar
color=(37,0,0)

# Inicialización de combinaciones
i=1000
while i<=5000:
    # Llamar al servicio con esa combinacion
    numero=('0000'+str(i))[-4:]
    r = requests.get(f'http://192.168.2.88:5000/?numero={numero}')
    time.sleep(0.3)
    
    # Capturar pantalla de referencia
    screenshot = ImageGrab.grab(bbox=(cx, cy, cx2, cy2))
    screenshot.save(f"img\img{numero}.png","PNG")
    
    
    
    # Buscar si hay pixeles de colores diferentes al buscado
    enviado=False
    while not enviado:
        # Capturar pantalla de analisis
        screenshot = ImageGrab.grab(bbox=(1737, 642, 1753, 661))
        px=screenshot.load()
        
        for x in range(an):
            for y in range(an):
                if px[x,y]==color:
                    enviado=True #pasar al siguiente número
        if enviado:
            i+=1
            print(numero)
            break
        else:
            print("avanzando")
            r = requests.get('http://192.168.2.88:5000/?numero=0000')
            time.sleep(0.3)
    screenshot.close()
    time.sleep(0.4)