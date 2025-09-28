# Adjustable sensitivity
sensitivity = 50
center = 0  

# Persistent variables
if starting:
    global posX, posY
    posX = center
    posY = center

# Range limit
def clamp(val):
    return max(-16000, min(16000, val))

# Movement accumulation with stop
posX = clamp(posX + mouse.deltaX * sensitivity)
posY = clamp(posY + mouse.deltaY * sensitivity)

# Apply to vJoy
vJoy[0].x = posX
vJoy[0].y = posY

from ctypes import windll
user32 = windll.user32

# Detect middle mouse button
key_centerx = mouse.getButton(2)  # 2 = botón del medio

# Center the stick if the button is pressed
if key_centerx:
    posY = 0
    posX = 0  


#==========CREDITS=========#
#[Copilot](https://copilot.microsoft.com)
