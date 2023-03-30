from PIL import Image
from sys import argv

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
    BG.paste(cases, (gap, ht), cases)
    size = cases.width
    height=cases.height
    #print(size)
    gap+=size
    if sheet_width < gap or len(i)*120 >(sheet_width-gap):
        gap = 120
        ht = ht + 200
print(gap)
print(sheet_width)
BG.show()
