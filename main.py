from PIL import Image
from sys import argv
import random

fileName = "input.txt" # path of your text file

try:
    txt=open(argv[1], "r")
except IndexError:
    print("No file entered. Using default file...")
    txt=open(fileName, "r")
except FileNotFoundError:
    print("Could not find file. Using default file...")
    txt=open(fileName, "r")   

BG=Image.open("images/bg.png") 
sheet_width=BG.width
gap, ht = 120, 200

for i in txt.read():
    if i == '\n':
        gap = 120;
        ht = ht + 200
        continue

    cases = Image.open("images/{}.png".format(str(ord(i))))
    x = random.randint(-20, -20)
    y = random.randint(-20, -20)
    angle = random.randint(-15, 15)
    rt = cases.rotate(angle)
    BG.paste(rt, (gap + x, ht + y), rt)
    size = cases.width
    height=cases.height
    #print(size)
    gap+=size
    if sheet_width < gap or len(i)*115 > ((sheet_width-gap) - 120):
        gap = 120
        ht = ht + 200
BG.show()

