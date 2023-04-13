from PIL import Image
from sys import argv
import random
import hyphen
import string
import re

DEFAULT_GAP = 300
DEFAULT_HT = 100
LETTER_WIDTH = 50
LETTER_HEIGHT = 75

h = hyphen.Hyphenator('pt_BR')
fileName = "input.txt" # path of your text file
gap, ht = DEFAULT_GAP, DEFAULT_HT
pages = []
current_page = 0

def get_leter(letter):
    cases = Image.open("images/{}.png".format(str(ord(letter))))
    cases.thumbnail((50,75), Image.Resampling.LANCZOS)
    angle = random.randint(-15, 15)
    rt = cases.rotate(angle)
    return rt

def print_letter(image, letter):
    rt = get_leter(letter)
    x = random.randint(-20, -20)
    y = random.randint(-20, -20)
    image.paste(rt, (gap + x, ht + y), rt)
    size = rt.width
    height = rt.height
    return (size, height)

def breakline(gap, ht):
    gap = DEFAULT_GAP
    ht = ht + DEFAULT_HT
    return gap, ht

def open_file():
    try:
        return open(argv[1], "r")
    except IndexError:
        print("No file entered. Using default file...")
        return open(fileName, "r")
    except FileNotFoundError:
        print("Could not find file. Using default file...")
        return open(fileName, "r")   

def get_background():
    return Image.open("images/bg2.png").convert('RGB')

def syllable_fit_in_line(syllable, gap, sheet_width):
    syllable_length = (len(syllable) * LETTER_WIDTH) + 200
    current_line_width = gap
    return syllable_length < (sheet_width - current_line_width)

def fit_in_page(ht, sheet_height):
    return ht < (sheet_height - DEFAULT_HT * 2)

def new_page(current_page):
    pages.append(background.copy())
    current_page = current_page + 1
    return current_page, DEFAULT_HT, DEFAULT_GAP

def print_pdf():
    pages[0].save("output.pdf", save_all=True, append_images=pages[1:])

def print_space(gap):
    gap = gap + LETTER_WIDTH + random.randint(-5,5)
    return gap
txt = open_file()
background = get_background()
pages.append(background.copy())

lines = txt.readlines()

for line in lines:
    for word in line.split():
        punctuation = None
        if word[-1] in string.punctuation:
            punctuation = word[-1]
            word = word[:-1]

        syllables = None
        if len(h.syllables(word)) < 1:
            syllables = [word]
        else:
            syllables = h.syllables(word)

        for index, syllable in enumerate(syllables):
            if syllable_fit_in_line(syllable, gap, background.width):
                for letter in syllable:
                    print_letter(pages[current_page], letter)
                    gap = print_space(gap)
            else:
                if not fit_in_page(ht, background.height):
                    current_page, ht, gap = new_page(current_page)
                if index == 0 and (len(syllables) > 1):
                    syllabe = syllable + '-'
                else:
                    syllabe = '-' + syllable
                
                for letter in syllabe:
                    print_letter(pages[current_page], letter)
                    gap = print_space(gap)
                
                gap, ht = breakline(gap, ht)

        if punctuation is not None:
            print_letter(pages[current_page], punctuation)
            gap = print_space(gap)
 
        gap = print_space(gap)

    gap, ht = breakline(gap, ht)

print_pdf()