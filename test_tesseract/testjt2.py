
from PIL import ImageGrab
    
 
im =ImageGrab.grab((300, 100, 1400, 600))
im.save('save3.jpeg','jpeg')