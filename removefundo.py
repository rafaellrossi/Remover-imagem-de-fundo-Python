from PIL import Image
import sys
import os
import rembg

img = Image.open(sys.argv[1])
sem_fundo = rembg.remove(img)
sem_fundo.save('sem_fundo.png', "PNG")
os.system("sem_fundo.png")
