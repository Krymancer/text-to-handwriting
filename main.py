from PIL import Image
from sys import argv
import random
import hyphen

h = hyphen.Hyphenator('pt_BR')

fileName = "input.txt" # path of your text file

DEFAULT_GAP = 305
DEFAULT_HT = 100

gap, ht = DEFAULT_GAP, DEFAULT_HT

def get_leter(letter):
    cases = Image.open("images/{}.png".format(str(ord(i))))
    cases.thumbnail((150,75), Image.Resampling.LANCZOS)
    angle = random.randint(-15, 15)
    rt = cases.rotate(angle)
    return rt

def print_letter(image, letter):
    rt = get_leter(i)
    x = random.randint(-20, -20)
    y = random.randint(-20, -20)
    BG.paste(rt, (gap + x, ht + y), rt)
    size = rt.width
    height = rt.height
    return (size, height)


try:
    txt=open(argv[1], "r")
except IndexError:
    print("No file entered. Using default file...")
    txt=open(fileName, "r")
except FileNotFoundError:
    print("Could not find file. Using default file...")
    txt=open(fileName, "r")   

BG=Image.open("images/bg2.png") 
sheet_width=BG.width
brkline = False

for w in txt.read().split():
    w += ' '
    for idx, s in enumerate(h.syllables(w)):
        if sheet_width < 150 or len(s) * 75 > (sheet_width - gap) and idx != 0:
            s = '-' + s
            brkline = True
        for i in s:
            size, height = print_letter(BG, i)
            gap += size
            if sheet_width < 150 or size > (sheet_width - gap) or brkline:
                brkline = False
                ht = ht + DEFAULT_HT
                gap = DEFAULT_GAP
BG.show()

