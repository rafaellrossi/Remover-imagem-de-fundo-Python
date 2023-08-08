import sys, os, rembg
from PIL import Image

img = Image.open(sys.argv[1])
sem_fundo = rembg.remove(img)
sem_fundo.save('sem_fundo.png', "PNG")
os.system("sem_fundo.png")


