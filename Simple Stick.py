# Sensibilidad ajustable
sensitivity = 50
center = 0  # ← tu centro real

# Variables persistentes
if starting:
    global posX, posY
    posX = center
    posY = center

# Limitar al rango de vJoy
def clamp(val):
    return max(-16000, min(16000, val))

# Acumulación de movimiento con tope
posX = clamp(posX + mouse.deltaX * sensitivity)
posY = clamp(posY + mouse.deltaY * sensitivity)

# Aplicar a vJoy
vJoy[0].x = posX
vJoy[0].y = posY

from ctypes import windll
user32 = windll.user32

# Detectar botón central del mouse
key_centerx = mouse.getButton(2)  # 2 = botón del medio

# Centrar el volante si se presiona el botón
if key_centerx:
    posY = 0
    posX = 0  # reinicia el eje de dirección